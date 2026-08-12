import sys
import os

# 1. Force Passenger to relaunch this script using Python 3.10 from your venv
INTERP = "/home/systema1/virtualenv/privateapps.systematicdefence.tech/server/3.10/bin/python"
if sys.executable != INTERP:
    os.execl(INTERP, INTERP, *sys.argv)

# ====================================================================
# Everything below here will safely run inside the Python 3.10 environment
# ====================================================================

# 2. Force Python to look in your current folder for code 
sys.path.insert(0, os.path.dirname(__file__)) 

# 3. Force Passenger to use your exact virtual environment packages
venv_packages = '/home/systema1/virtualenv/privateapps.systematicdefence.tech/server/3.10/lib/python3.10/site-packages'
sys.path.insert(0, venv_packages)

# 4. Import your FastAPI app object from main.py 
from main import app 

# 5. Convert ASGI to WSGI for Passenger using ASGIMiddleware
from a2wsgi import ASGIMiddleware

application = ASGIMiddleware(app)
