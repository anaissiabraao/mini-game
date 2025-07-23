#!/bin/bash
# This script sets up the environment for the quiz application

# Create virtual environment
python -m venv venv

# Activate virtual environment
source venv/bin/activate  # On Windows, use: .\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create necessary directories
mkdir -p static

echo "Setup complete! Activate the virtual environment and run 'python server.py' to start the server."
