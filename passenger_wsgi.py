import sys
import os 

#1. Force Python to look in your current folder for code 

sys.path.insert(0, os.path.dirname(file)) 

#2. Point to your virtual environment packages so it can find FastAPI 

#(cPanel usually manages this, but adding it explicitly guarantees it works) 

if 'VIRTUAL_ENV' in os.environ:  

    sys.path.insert(0, os.path.join(os.environ['VIRTUAL_ENV'], 'lib', 'python3.10', 'site-packages')) 

#3. Import your FastAPI app object from main.py 

from main import app 

#4. Convert ASGI to WSGI for Passenger 

from a2wsgi import ASGIToWSGI application = ASGIToWSGI(app) 

 