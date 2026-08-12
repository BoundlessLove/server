import sys
import os

# 1. Force Python to look in your current folder for code 
sys.path.insert(0, os.path.dirname(__file__)) 

# 2. Force the server to use your virtual environment packages
venv_packages = '/home/systema1/virtualenv/privateapps.systematicdefence.tech/server/3.10/lib/python3.10/site-packages'
sys.path.insert(0, venv_packages)

# 3. Direct bridge to your Flask application inside main.py
from main import application
