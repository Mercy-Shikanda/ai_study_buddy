# 🧠 AI Study Buddy - Flashcard Generator

Transform your study notes into interactive flashcards using AI! This project perfectly demonstrates how to build a practical AI-powered web application that solves real student problems.

## 🚀 Features

- **AI-Powered Question Generation**: Automatically generates 5 quiz questions from any study material
- **Interactive Flashcards**: Flip cards with smooth CSS animations
- **Previous Flashcards**: View and manage previously generated flashcard sets
- **Modern UI**: Beautiful, responsive design with gradients and animations
- **Real-time State Management**: Dynamic content updates without page refresh
- **Database Integration**: Persistent storage for flashcard reuse

## 🛠 Tech Stack

### Frontend
- **HTML5**: Semantic structure with modern elements
- **CSS3**: Advanced animations, gradients, and responsive design
- **JavaScript**: Interactive flip cards, state management, and API calls

### Backend
- **Python Flask**: RESTful API server
- **Supabase**: Cloud database for flashcard storage
- **AI Integration**: Hugging Face Question-Answering API

### AI Model
- **Hugging Face Router API**: GPT-OSS-120B model for high-quality question generation

## 📋 How It Works

1. **User Input**: Student pastes study notes into HTML textarea
2. **AI Processing**: Python sends text to Hugging Face API with prompt: *"Generate 5 quiz questions"*
3. **Database Storage**: Generated flashcards saved to Supabase for reuse
4. **Interactive Display**: JavaScript creates flip cards with CSS animations
5. **State Management**: Tab system for new vs. previous flashcards

## 🎯 Why It's Perfect for Learning

- **No Complex UI**: Simple text input/output interface
- **Teaches Core Concepts**:
  - **State Management** (JavaScript)
  - **Database Relationships** (Supabase)
  - **API Integration** (Hugging Face)
  - **Responsive Design** (CSS)
- **Solves Real Problems**: Instantly useful for students
- **Modern Patterns**: RESTful APIs, async/await, modern CSS

## 🚀 Quick Start

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Set Up Environment**:
   ```bash
   # Copy .env.example to .env and fill in your keys
   SUPABASE_URL=your_supabase_url
   SUPABASE_KEY=your_supabase_key
   HF_API_KEY=your_hugging_face_api_key
   ```

3. **Run the Application**:
   ```bash
   python app.py
   ```

4. **Open in Browser**:
   Navigate to `http://localhost:5000/ui`

## 🔧 API Endpoints

- `POST /generate` - Generate new flashcards from notes
- `GET /flashcards/<user_id>` - Get all flashcards for user
- `GET /flashcards/recent/<user_id>` - Get recent flashcards
- `GET /ui` - Serve the main interface

## 📚 Learning Outcomes

After building this project, you'll understand:

1. **Frontend Development**:
   - Modern CSS with animations and responsive design
   - JavaScript state management and DOM manipulation
   - Asynchronous programming with fetch API

2. **Backend Development**:
   - RESTful API design with Flask
   - Database integration and relationships
   - Error handling and validation

3. **AI Integration**:
   - Working with external AI APIs
   - Prompt engineering for better results
   - Handling API responses and errors

4. **Full-Stack Concepts**:
   - Client-server communication
   - Data persistence and retrieval
   - User experience design

## 🎨 UI Features

- **Modern Design**: Gradient backgrounds and card-based layout
- **Smooth Animations**: CSS transitions and keyframe animations
- **Responsive Layout**: Works on desktop, tablet, and mobile
- **Interactive Elements**: Hover effects and loading states
- **Tab System**: Organized navigation between new and saved content

## 🔮 Future Enhancements

- User authentication system
- Flashcard sharing between users
- Study session tracking and analytics
- Export flashcards to PDF or Anki
- Voice-to-text note input
- Spaced repetition algorithm

---

**Perfect for**: Students learning web development, AI integration, and full-stack programming patterns.

**Built with ❤️ for the learning community**
