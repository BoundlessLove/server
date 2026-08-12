import sys
import os

# 1. Force Python to look in your current folder for code 
sys.path.insert(0, os.path.dirname(__file__)) 

# 2. Force Passenger/LiteSpeed to use your exact virtual environment packages
venv_packages = '/home/systema1/virtualenv/privateapps.systematicdefence.tech/server/3.10/lib/python3.10/site-packages'
sys.path.insert(0, venv_packages)

# 3. Import your FastAPI app object from main.py 
from main import app 

# 4. Convert ASGI to WSGI using the correct AsgiToWsgi class from asgiref
from asgiref.wsgi import AsgiToWsgi

application = AsgiToWsgi(app)
