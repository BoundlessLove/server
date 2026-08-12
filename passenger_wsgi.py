import sys
import os

# 1. Force Python 3.10 with a strict guard to prevent infinite looping
INTERP = "/home/systema1/virtualenv/privateapps.systematicdefence.tech/server/3.10/bin/python"
if os.environ.get('PYTHON_SWITCHED') != '1':
    os.environ['PYTHON_SWITCHED'] = '1'
    os.execl(INTERP, INTERP, *sys.argv)

# ====================================================================
# Everything below here will safely execute exactly once in Python 3.10
# ====================================================================

# 2. Force Python to look in your current folder for code 
sys.path.insert(0, os.path.dirname(__file__)) 

# 3. Force Passenger to use your exact virtual environment packages
venv_packages = '/home/systema1/virtualenv/privateapps.systematicdefence.tech/server/3.10/lib/python3.10/site-packages'
sys.path.insert(0, venv_packages)

# 4. Import your FastAPI app object from main.py 
from main import app 

# 5. Convert ASGI to WSGI using the lightweight asgiref adapter
from asgiref.wsgi import WsgiToAsgi

application = WsgiToAsgi(app)
