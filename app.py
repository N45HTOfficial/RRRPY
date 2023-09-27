import os
from flask import Flask

app = Flask(__name__)

port = int(os.environ.get("PORT", 8080))

@app.route("/")
def app_s():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port)
