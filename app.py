import os
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

port = int(os.environ.get("PORT", 8080))

@app.route("/")
def index():
    return "Hello, World!"

@app.route("/api/statusCheck", methods=["GET"])
def status_check():
    url = request.args.get("url")

    if not url:
        return jsonify({"error": "Missing 'url' parameter"}), 400
    try:
        response = requests.get(url)
        status_code = response.status_code
        response_data = {
            "url": url,
            "status_code": status_code,
            "message": "Success" if response.ok else "Failed"
        }
        return jsonify(response_data), status_code

    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port)
