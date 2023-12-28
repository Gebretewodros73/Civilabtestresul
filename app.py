#!/usr/bin/python3
from flask import Flask, render_template, request

app = Flask(__name__)

# Sample data for laboratory test results
test_results = [
    {"sample_id": 1, "test_name": "Compressive Strength", "result": 25.6},
    {"sample_id": 2, "test_name": "Flexural Strength", "result": 12.3},
    {"sample_id": 3, "test_name": "Water Absorption", "result": 0.5},
    # Add more test results here
]

@app.route("/")
def home():
    return render_template("index.html", test_results=test_results)

@app.route("/submit", methods=["POST"])
def submit():
    sample_id = request.form.get("sample_id")
    test_name = request.form.get("test_name")
    result = request.form.get("result")

    # Process the submitted test result (e.g., store it in a database)
    # Add your code here

    return "Test result submitted successfully!"

if __name__ == "__main__":
    app.run(debug=True)
