from flask import Flask, jsonify, request

# 1. Initialize the native WSGI application
app = Flask(__name__)

@app.route("/")
def read_root():
    return jsonify({"status": "success", "message": "Hello from Flask on FastComet!"})

@app.route("/items/<int:item_id>")
def read_item(item_id):
    # Retrieve the query parameters (equivalent to q: str = None in FastAPI)
    q = request.args.get('q', None)
    return jsonify({"item_id": item_id, "q": q})

# 2. Expose the exact object cPanel expects to run the website
application = app
