# Sample Python Server

## 1.0 Setup

~/eclipse-workspace/MicronManagement] └─$ python3 -m venv venv

~/eclipse-workspace/MicronManagement] └─$ source venv/bin/activate

~/eclipse-workspace/MicronManagement] └─$ pip install -r requirements.txt

### a. Start server

~/eclipse-workspace/MicronManagement] └─$ uvicorn main:app --reload --port 8002

### b. Test

i. Navigate to :

http://127.0.0.1:8000/api/v1/convert-hex

## 2.0 Versions

### 0.01 Various teething issues as below

![Teething issues](./screenshots/SyntaxError.jpg)

Resolved via moving 'application = ASCIToWSGI(app)' to new line.

 