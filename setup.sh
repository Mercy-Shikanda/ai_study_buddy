#!/bin/bash
# Quick setup script for markers/testers

echo "🚀 Setting up AI Study Buddy for testing..."

# Check if Python is installed
if ! command -v python &> /dev/null; then
    echo "❌ Python not found. Please install Python 3.8+ first."
    exit 1
fi

# Install dependencies
echo "📦 Installing dependencies..."
pip install -r requirements.txt

# Check if .env file exists
if [ ! -f .env ]; then
    echo "⚠️  Warning: .env file not found. Using default configuration."
fi

echo "✅ Setup complete!"
echo "🌐 Starting the application..."
echo "📱 Open your browser to: http://localhost:5000/ui"
echo ""

# Start the application
python app.py
