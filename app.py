import os
import re
import json
import uuid
from flask import Flask, request, jsonify, render_template
from supabase import create_client, Client
from dotenv import load_dotenv
import requests
from openai import OpenAI

# Load environment variables
load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
HF_API_KEY = os.getenv("HF_API_KEY")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Initialize OpenAI client for Hugging Face
client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=HF_API_KEY,
)

app = Flask(__name__)

# --- Question generation using OpenAI-compatible API ---
def generate_questions(text: str):
    try:
        # Create a prompt for generating exactly 5 study questions
        prompt = f"""Based on the following study material, create exactly 5 quiz questions with their answers in JSON format.

Study Material:
{text[:800]}

Please respond with a JSON array containing exactly 5 questions in this format:
[
  {{"question": "What is...", "answer": "The answer is..."}},
  {{"question": "How does...", "answer": "It works by..."}},
  {{"question": "Why is...", "answer": "Because..."}},
  {{"question": "When does...", "answer": "It occurs when..."}},
  {{"question": "Where can...", "answer": "It can be found..."}}
]

JSON Response:"""

        completion = client.chat.completions.create(
            model="openai/gpt-oss-120b:together",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            max_tokens=800,  # Increased to prevent cutoff
            temperature=0.7
        )
        
        response_text = completion.choices[0].message.content
        print(f"AI Response: {response_text}")
        
        # Clean the response text - remove any markdown formatting
        cleaned_response = response_text.strip()
        if cleaned_response.startswith('```json'):
            cleaned_response = cleaned_response.replace('```json', '').replace('```', '').strip()
        
        # Try to parse JSON from the response
        try:
            # Look for JSON array in the response
            json_match = re.search(r'\[.*?\]', cleaned_response, re.DOTALL)
            if json_match:
                json_str = json_match.group()
                questions = json.loads(json_str)
                
                # Validate that we have proper question/answer pairs
                valid_questions = []
                for q in questions:
                    if isinstance(q, dict) and 'question' in q and 'answer' in q:
                        # Clean up incomplete answers
                        question_text = q['question'].strip()
                        answer_text = q['answer'].strip()
                        
                        # Skip if answer is too short or incomplete
                        if len(answer_text) > 10 and not answer_text.endswith(('...', '.')):
                            answer_text += '.'
                        
                        if len(question_text) > 5 and len(answer_text) > 5:
                            valid_questions.append({
                                "question": question_text,
                                "answer": answer_text
                            })
                
                if len(valid_questions) > 0:
                    return valid_questions[:5]  # Return up to 5 questions
                
        except json.JSONDecodeError as e:
            print(f"JSON parsing error: {e}")
        
        # If JSON parsing fails, try to extract questions manually
        return parse_text_response(cleaned_response, text)
        
    except Exception as e:
        print(f"Error in generate_questions: {e}")
        return try_fallback_model(text)

def parse_text_response(response_text: str, original_text: str):
    """Parse non-JSON response to extract questions and answers"""
    questions = []
    
    # Try to extract question-answer pairs from the text
    lines = response_text.split('\n')
    current_question = ""
    current_answer = ""
    
    # Look for patterns in the response
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # Clean up common formatting
        line = line.replace('"', '').replace(',', '').strip()
        
        # Look for question patterns
        if (line.startswith(('question:', 'Question:', '"question":', 'What', 'How', 'Why', 'When', 'Where', 'Who')) or
            any(pattern in line.lower() for pattern in ['question":', '"question"', 'q:'])):
            
            if current_question and current_answer:
                questions.append({
                    "question": current_question,
                    "answer": current_answer
                })
                
            # Extract the question text
            if ':' in line:
                current_question = line.split(':', 1)[-1].strip()
            else:
                current_question = line.strip()
            current_answer = ""
            
        # Look for answer patterns  
        elif (line.startswith(('answer:', 'Answer:', '"answer":', 'The', 'It', 'Because', 'A ', 'An ')) or
              any(pattern in line.lower() for pattern in ['answer":', '"answer"', 'a:'])):
            
            # Extract the answer text
            if ':' in line:
                current_answer = line.split(':', 1)[-1].strip()
            else:
                current_answer = line.strip()
                
        # If we have a question but no answer yet, this might be the answer
        elif current_question and not current_answer and len(line) > 10:
            current_answer = line.strip()
    
    # Add the last question if exists
    if current_question and current_answer:
        questions.append({
            "question": current_question,
            "answer": current_answer
        })
    
    # If we still don't have questions, create some basic ones from the original text
    if not questions and original_text:
        sentences = [s.strip() for s in original_text.split('.') if len(s.strip()) > 20][:3]
        for i, sentence in enumerate(sentences):
            questions.append({
                "question": f"What can you tell me about: {sentence[:50]}...?",
                "answer": sentence
            })
    
    return questions[:5]  # Return up to 5 questions
    
    # Add the last question if exists
    if current_question and current_answer:
        questions.append({
            "question": current_question,
            "answer": current_answer
        })
    
    return questions[:5]

def try_fallback_model(text: str):
    """Fallback to a different model if the primary one fails"""
    try:
        # Use a simpler prompt for fallback
        prompt = f"Create 5 study questions about this text:\n\n{text[:400]}"

        completion = client.chat.completions.create(
            model="microsoft/DialoGPT-medium",
            messages=[
                {
                    "role": "user", 
                    "content": prompt
                }
            ],
            max_tokens=300,
            temperature=0.6
        )
        
        response_text = completion.choices[0].message.content
        print(f"Fallback AI Response: {response_text}")
        
        # Parse the fallback response
        return parse_text_response(response_text, text)
        
    except Exception as e:
        print(f"Error in fallback model: {e}")
        return []


# --- Routes ---
@app.route("/")
def home():
    return {"message": "AI Study Buddy Flask API is running 🚀"}


@app.route("/generate", methods=["POST"])
def generate_flashcards():
    data = request.json
    notes = data.get("notes", "")
    user_id = data.get("user_id")

    if not notes:
        return jsonify({"error": "Missing notes"}), 400

    # Handle UUID validation - use provided UUID or default
    if not user_id or user_id == "replace-with-a-valid-user-uuid":
        user_id = "aebef574-006b-4231-8880-362dce742514"
        print(f"Using default user_id: {user_id}")

    # Validate UUID format
    try:
        uuid.UUID(user_id)
    except ValueError:
        user_id = "aebef574-006b-4231-8880-362dce742514"
        print(f"Invalid UUID provided, using default: {user_id}")

    # Generate Q&A
    questions = generate_questions(notes)
    
    print(f"Generated {len(questions)} questions")  # Debug log
    
    if not questions:
        return jsonify({"error": "AI failed to generate questions. Please try again with different notes or check if the AI service is available."}), 500

    flashcards = []

    # Process the questions array
    for i, qa in enumerate(questions):
        # Handle different possible formats
        if isinstance(qa, dict):
            question = qa.get("question", f"Question {i+1}")
            answer = qa.get("answer", "Answer not available")
        else:
            # If qa is a string, create a simple Q&A
            question = f"Question {i+1}"
            answer = str(qa)

        try:
            # Save to Supabase - let the database handle id and created_at defaults
            result = supabase.table("flashcards").insert({
                "user_id": user_id,
                "question": question,
                "answer": answer
            }).execute()
            print(f"Saved flashcard {i+1} to database")
        except Exception as e:
            print(f"Error saving to database: {e}")
            # Continue even if database save fails

        flashcards.append({"question": question, "answer": answer})

    return jsonify({"flashcards": flashcards, "user_id": user_id})


@app.route("/flashcards/<user_id>", methods=["GET"])
def get_flashcards(user_id):
    try:
        response = supabase.table("flashcards").select("*").eq("user_id", user_id).order("created_at", desc=True).execute()
        return jsonify({"flashcards": response.data})
    except Exception as e:
        print(f"Error fetching flashcards: {e}")
        return jsonify({"error": "Failed to fetch flashcards"}), 500

@app.route("/flashcards/recent/<user_id>", methods=["GET"])
def get_recent_flashcards(user_id):
    """Get the most recent flashcard sets for the user"""
    try:
        response = supabase.table("flashcards").select("*").eq("user_id", user_id).order("created_at", desc=True).limit(20).execute()
        return jsonify({"flashcards": response.data})
    except Exception as e:
        print(f"Error fetching recent flashcards: {e}")
        return jsonify({"error": "Failed to fetch flashcards"}), 500

@app.route("/ui")
def ui():
    return render_template("index.html")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
