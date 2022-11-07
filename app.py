import json
import os
import requests
from sys import stderr
from flask import Flask, request, jsonify

app = Flask(__name__)

api_key = os.environ.get("API_KEY", "")
if api_key == "":
    print("api key is required", file=stderr)

api_base_url = "https://dev-bhagaskarash4zl.microgen.id/api" + api_key

@app.get("/products")
def handler():
    return "<h1>test</h1>"
@app.post("/products")
def handler():
    limit = posts['limit']
    keyword = posts['keyword']
    return keyword

if __name__ == "__main__":
    app.run(debug=True)
