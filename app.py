from flask import Flask, request, jsonify
from chat import get_response
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.post("/predict")
def predict():commit
    # TODO: check if test is valid
    response = get_response(text)
    message = {"answer", response}
    return jsonify(message)


if __name__ == "__main__":
    app.run(debug=True)
