import nltk
from flask import Flask, render_template, request, jsonify
from chat import get_response  # Ensure this module is correctly implemented
from flask_cors import CORS

nltk.download('punkt')

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes, allowing requests from any domainquit

@app.route("/", methods=['GET'])  # Home page route that renders a template
def index_get():
    return render_template("base.html")

@app.route("/predict", methods=['POST'])
def get_chat_response():  # Function renamed for clarity and improved functionality
    data = request.get_json()
    if not data or "message" not in data:
        return jsonify({"error": "No message provided"}), 400  # Error handling for missing message
    text = data["message"]
    response = get_response(text)  # Generate response using the chat module
    return jsonify({"answer": response})  # Return the chat response in JSON format

# def download_nltk_resources():
#   nltk.download('punkt')  # Download the 'punkt' tokenizer models from NLTK

if __name__ == "__main__":
    download_nltk_resources()  # Ensure NLTK resources are downloaded before starting the app
    app.run()  # Start the Flask application