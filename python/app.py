from flask import Flask, render_template, jsonify, request
import os
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", now=datetime.utcnow().isoformat() + "Z")

@app.route("/api/hello", methods=["GET"])
def hello():
    name = request.args.get("name", "world")
    return jsonify({
        "message": f"Hello, {name}!",
        "time": datetime.utcnow().isoformat() + "Z",
        "env": dict(os.environ)  # remove or limit in production
    })

# Health endpoint
@app.route("/healthz", methods=["GET"])
def health():
    return jsonify(status="ok"), 200

if __name__ == "__main__":
    # For local debugging only. In Docker we use gunicorn.
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)), debug=True)
