# Render Deployment Guide for AI Study Buddy

## 🚀 Quick Deploy to Render

### Step 1: Prepare Your Repository
Your GitHub repository is already set up correctly at:
**https://github.com/Mercy-Shikanda/ai_study_buddy**

### Step 2: Deploy on Render

1. **Go to Render Dashboard**
   - Visit: https://render.com
   - Sign up/Login with your GitHub account

2. **Create New Web Service**
   - Click "New +" → "Web Service"
   - Connect your GitHub repository: `Mercy-Shikanda/ai_study_buddy`

3. **Configure Service Settings**
   ```
   Name: ai-study-buddy
   Region: Oregon (US West) or closest to you
   Branch: main
   Runtime: Python 3
   Build Command: ./build.sh
   Start Command: python app.py
   ```

4. **Set Environment Variables**
   In the "Environment" section, add:
   ```
   SUPABASE_URL=your_supabase_url_here
   SUPABASE_KEY=your_supabase_anon_key_here
   HF_API_KEY=your_hugging_face_api_key_here
   ```

5. **Deploy**
   - Click "Create Web Service"
   - Wait for deployment (takes 2-3 minutes)
   - Your app will be available at: `https://ai-study-buddy-xxxx.onrender.com`

### Step 3: Update Your App URL
Once deployed, your live app will be accessible at:
- **Main App**: `https://your-app-name.onrender.com/ui`
- **API Endpoint**: `https://your-app-name.onrender.com/generate`

### Step 4: Test Your Deployment
1. Visit your Render URL + `/ui`
2. Paste some study notes
3. Click "Generate 5 Quiz Questions"
4. Verify flashcards are created and saved

## 📋 Deployment Checklist

- [ ] GitHub repository is public and up-to-date
- [ ] build.sh file is executable
- [ ] Environment variables are set in Render
- [ ] Supabase database is accessible from external sources
- [ ] Hugging Face API key is valid
- [ ] App responds at `/ui` endpoint

## 🔧 Troubleshooting

**If deployment fails:**
1. Check Render build logs
2. Verify all environment variables are set
3. Ensure Supabase allows external connections
4. Check that all dependencies are in requirements.txt

**If flashcards don't save:**
1. Verify Supabase credentials
2. Check that your table exists and has correct schema
3. Look at Render service logs for database errors

## 🎯 For Markers/Testers

Once deployed, provide this information:

**Live Demo URL**: `https://your-app-name.onrender.com/ui`
**GitHub Repository**: https://github.com/Mercy-Shikanda/ai_study_buddy
**Test Credentials**: User ID is auto-generated

**Sample Test Data**: Use the examples in DEPLOYMENT.md

---
**Note**: Render free tier may have cold starts (30-60 seconds delay if inactive). This is normal for free hosting.
