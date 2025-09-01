@echo off
REM Quick setup script for Windows markers/testers

echo 🚀 Setting up AI Study Buddy for testing...

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python not found. Please install Python 3.8+ first.
    pause
    exit /b 1
)

REM Install dependencies
echo 📦 Installing dependencies...
pip install -r requirements.txt

REM Check if .env file exists
if not exist .env (
    echo ⚠️  Warning: .env file not found. Using default configuration.
)

echo ✅ Setup complete!
echo 🌐 Starting the application...
echo 📱 Open your browser to: http://localhost:5000/ui
echo.

REM Start the application
python app.py

pause
