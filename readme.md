# Sample Python Server

## 1.0 Setup

~/eclipse-workspace/MicronManagement] └─$ python3 -m venv venv

~/eclipse-workspace/MicronManagement] └─$ source venv/bin/activate

~/eclipse-workspace/MicronManagement] └─$ pip install -r requirements.txt

### a. Start server

~/eclipse-workspace/MicronManagement] └─$ uvicorn main:app --reload --port 8002

### b. Acceess virtual environment remotely (if needed)

server] source /home/systema1/virtualenv/privateapps.systematicdefence.tech/server/3.10/bin/activate && cd /home/systema1/privateapps.systematicdefence.tech/server

#### i. Create a restart file that Passenger looks for
mkdir -p tmp && touch tmp/restart.txt

#### ii. Kill any stuck background Python workers for your user
pkill -u systema1 -f python

#### iii. Clear your browser cache and refresh your app URL


### b. Test

i. Navigate to :

http://127.0.0.1:8000/api/v1/convert-hex



## 2.0 Versions

### 0.01 Various teething issues as below

![Teething issues](./screenshots/SyntaxError.jpg)

Resolved via moving 'application = ASCIToWSGI(app)' to new line.

### 0.02 App using incorrect virtual environment

Issue:

![Virtual Environment issues](./screenshots/VirtualEnvironmentBug.jpg)
 
Investigation:
 
![Virtual Environment check](./screenshots/VirtualEnvironmentCheck.jpg)

Resolution:

The console shows that a2wsgi version 1.10.1 is successfully installed in your virtual environment. That version definitely contains ASGIToWSGI, meaning the package itself is fine.
The problem is that  terminal prompt shows virtual environment activated after the error occurred. Passenger (cPanel's application manager) is likely running script using the server's global system Python instead of server's specific virtual environment. When it does that, it falls back to a different or broken version of a2wsgi hosted globally.
So, need to explicitly tell passenger_wsgi.py to use your virtual environment's packages before it tries to import anything.

The Fix:

Open your passenger_wsgi.py file and update Section 2. The standard environment variable check can sometimes fail under Passenger, so should explicitly add the hardcoded path from your terminal screen to sys.path.

Updated code

import sys

import os 

venv_packages = '/home/systema1/virtualenv/privateapps.systematicdefence.tech/server/3.10/lib/python3.10/site-packages'

sys.path.insert(0, os.path.dirname(__file__)) 

venv_packages = '/home/systema1/virtualenv/privateapps.systematicdefence.tech/server/3.10/lib/python3.10/site-packages'
 
sys.path.insert(0, venv_packages)

from main import app 

from a2wsgi import ASGIToWSGI 

application = ASGIToWSGI(app)

### 0.03 App using incorrect virtual environment

Issue:

![Virtual Environment issues- wsgi](./screenshots/wsgi.jpg)
 
Investigation:

That command output solves the mystery! The package a2wsgi does not export ASGIToWSGI directly from its main module root in this version. Instead, it exposes ASGIMiddleware and WSGIMiddleware.To convert your ASGI FastAPI application into a WSGI application using this package, you need to use ASGIMiddleware instead.
 
### 0.04 App 

#### Issue:

[systema1@s4710 server]$ python passenger_wsgi.py
Traceback (most recent call last):
  File "/home/systema1/privateapps.systematicdefence.tech/server/passenger_wsgi.py", line 13, in <module>
    from main import app
  File "/home/systema1/privateapps.systematicdefence.tech/server/main.py", line 1, in <module>
    from fastapi import FastAPI
  File "/home/systema1/virtualenv/privateapps.systematicdefence.tech/server/3.10/lib/python3.10/site-packages/fastapi/__init__.py", line 7, in <module>
    from .applications import FastAPI as FastAPI
  File "/home/systema1/virtualenv/privateapps.systematicdefence.tech/server/3.10/lib/python3.10/site-packages/fastapi/applications.py", line 7, in <module>
    from fastapi import routing
  File "/home/systema1/virtualenv/privateapps.systematicdefence.tech/server/3.10/lib/python3.10/site-packages/fastapi/routing.py", line 42, in <module>
    import anyio
  File "/home/systema1/virtualenv/privateapps.systematicdefence.tech/server/3.10/lib/python3.10/site-packages/anyio/__init__.py", line 29, in <module>
    from ._core._fileio import AsyncFile as AsyncFile
  File "/home/systema1/virtualenv/privateapps.systematicdefence.tech/server/3.10/lib/python3.10/site-packages/anyio/_core/_fileio.py", line 29, in <module>
    from ..abc import AsyncResource
  File "/home/systema1/virtualenv/privateapps.systematicdefence.tech/server/3.10/lib/python3.10/site-packages/anyio/abc/__init__.py", line 3, in <module>
    from ._eventloop import AsyncBackend as AsyncBackend
  File "/home/systema1/virtualenv/privateapps.systematicdefence.tech/server/3.10/lib/python3.10/site-packages/anyio/abc/_eventloop.py", line 11, in <module>
    from typing import (
ImportError: cannot import name 'TypeAlias' from 'typing' (/usr/lib64/python3.9/typing.py)
[systema1@s4710 server]$
 
#### Resolution:

The traceback exposes exactly why your app is failing: 

- your server is executing the script using Python 3.9 (/usr/lib64/python3.9/typing.py), but your FastAPI packages require Python 3.10.

Because TypeAlias was only introduced in Python 3.10, the older Python 3.9 interpreter crashes when trying to load your modern packages. Simply changing sys.path isn't enough because the core Python language itself is the wrong version.The FixYou need to force Phusion Passenger to stop using the system's default Python 3.9 and completely restart your script using your virtual environment's Python 3.10 binary.

1. Open your passenger_wsgi.py file and place an interpreter check right at the very top (before any other imports).

2. In your terminal, clear any stuck tasks again:
   
pkill -u systema1 -f python
   
3. Refresh your website in your browser.

The os.execl command will instantly hijack the process and force the entire environment to swap over to Python 3.10, resolving the ImportError completely.

