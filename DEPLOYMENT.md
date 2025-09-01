# AI Study Buddy - Deployment Instructions

## 🚀 Quick Deployment Guide for Markers/Testers

### Option 1: Local Testing (Easiest)
1. **Download the project folder**
2. **Install Python 3.8+**
3. **Set up environment variables:**
   ```bash
   cp .env.example .env
   # Edit .env file with your API keys
   ```
4. **Open terminal in project folder and run:**
   ```bash
   pip install -r requirements.txt
   python app.py
   ```
5. **Visit:** `http://localhost:5000/ui`

### Option 2: Online Demo (If deployed)
- **Live Demo:** [Your deployment URL here]
- **Test Credentials:** User ID is auto-generated

## 🔑 Environment Setup for Markers

### Required API Keys (Set up in .env file):
- 🔑 **Supabase URL & Key** - Get from your Supabase project dashboard
- 🔑 **Hugging Face API Key** - Get from huggingface.co/settings/tokens
- ✅ **Database Table** - Use the provided SQL schema

### Test Data Examples:
Use any of these sample study notes for testing:

**Sample 1 - Computer Networks:**
```
A computer network is a system that allows computers to communicate and share resources. Networks can be classified by size: LAN (Local Area Network) covers a small area like a building, MAN (Metropolitan Area Network) covers a city, and WAN (Wide Area Network) covers large geographical areas. Network devices include routers that direct traffic between networks, switches that connect devices within a network, and hubs that broadcast data to all connected devices. Network topologies include star topology where devices connect to a central hub, bus topology with a shared backbone, and ring topology where devices form a circular connection.
```

**Sample 2 - World War II:**
```
World War II began in 1939 with Germany's invasion of Poland. The United States entered the war in 1941 after the attack on Pearl Harbor. Key events include the Battle of Britain where the UK resisted German air attacks, D-Day invasion on June 6, 1944 when Allied forces landed in Normandy, and the atomic bombs dropped on Hiroshima and Nagasaki in 1945. The war ended with the unconditional surrender of the Axis powers in 1945.
```

## ✅ Features to Test:

1. **AI Question Generation:**
   - Paste study notes → Click "Generate 5 Quiz Questions"
   - Should create 5 interactive flashcards

2. **Interactive Flashcards:**
   - Hover over cards to flip and see answers
   - Modern UI with smooth animations

3. **Database Persistence:**
   - Generated flashcards are saved automatically
   - Click "Previous Flashcards" tab to view saved cards

4. **Responsive Design:**
   - Works on desktop, tablet, and mobile
   - Modern gradient design with Font Awesome icons

## 🛠 Technical Stack Verification:

- ✅ **Frontend:** HTML5 + CSS3 + JavaScript (flip cards, state management)
- ✅ **Backend:** Python Flask (RESTful API)
- ✅ **Database:** Supabase PostgreSQL (flashcard storage)
- ✅ **AI:** Hugging Face GPT-OSS-120B (question generation)

## 📊 Expected Behavior:

1. **Input:** User pastes study notes
2. **Processing:** AI generates 5 quiz questions
3. **Output:** Interactive flip cards displayed
4. **Storage:** Questions saved to database for reuse
5. **Retrieval:** Previous flashcards accessible via tabs

## 🔍 Success Criteria:

- [ ] Application loads without errors
- [ ] Can paste text and generate flashcards
- [ ] Cards flip on hover with smooth animation
- [ ] Questions are relevant to input text
- [ ] Previous flashcards load correctly
- [ ] Responsive design works on mobile

## 📞 Contact Information:
- **GitHub Repository:** [Your GitHub URL]
- **Demo Video:** [If you have one]
- **Documentation:** This README.md file

---
**Note:** This project demonstrates full-stack web development with AI integration, perfect for educational assessment!
