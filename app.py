import json
import os
import requests
from sys import stderr
from flask import Flask, request, jsonify

app = Flask(__name__)

api_key = os.environ.get("API_KEY", "")
if api_key == "":
    print("api key is required", file=stderr)

api_base_url = "https://api.stagingv3.microgen.id/query/api/v1/" + api_key

@app.route('/')
def handler(request):
    result = {"statusCode": 200, "message": sys.version}

    return jsonify(result)
if __name__ == "__main__":
    app.run(debug=True)
