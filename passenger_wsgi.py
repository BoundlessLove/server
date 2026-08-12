import sys
import os
import asyncio

# 1. Force Python to look in your current folder for code 
sys.path.insert(0, os.path.dirname(__file__)) 

# 2. Force Passenger/LiteSpeed to use your exact virtual environment packages
venv_packages = '/home/systema1/virtualenv/privateapps.systematicdefence.tech/server/3.10/lib/python3.10/site-packages'
sys.path.insert(0, venv_packages)

# 3. Secure a stable asyncio event loop for this worker process thread
try:
    loop = asyncio.get_event_loop()
except RuntimeError:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

# 4. Import your FastAPI app object from main.py 
from main import app 

# 5. Convert ASGI to WSGI using ASGIMiddleware from a2wsgi
from a2wsgi import ASGIMiddleware

application = ASGIMiddleware(app)