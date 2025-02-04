from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

# List of quotes
QUOTES = [
    "Dream big, work hard, and stay focused.",
    "Success is not final, failure is not fatal.",
    "Believe in yourself and all that you are.",
    "Do something today that your future self will thank you for.",
    "Opportunities don’t happen, you create them."
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get-quote")
def get_quote():
    return jsonify({"quote": random.choice(QUOTES)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
