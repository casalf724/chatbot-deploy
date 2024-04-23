import nltk
from flask import Flask, render_template, request, jsonify
from chat import get_response
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# shut off get to use API with Cors
@app.get("/") # Go to home page and render template
def index_get():
    return render_template("base.html")


@app.post("/predict")
def predict(): # Get messages
    text = request.get_json().get("message")
    # TODO: check if test is valid
    response = get_response(text) # gets response from text
    message = {"answer": response} # messages user
    return jsonify(message) # message returned in json format


def download_nltk_resources():
    nltk.download('punkt')

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
