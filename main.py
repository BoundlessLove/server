from fastapi import FastAPI
from a2wsgi import ASGIMiddleware

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "success", "message": "Hello from FastAPI on FastComet!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

# ====== ADD THIS AT THE VERY BOTTOM OF YOUR MAIN.PY ======
# This creates the exact WSGI wrapper cPanel is looking for!
application = ASGIMiddleware(app)
