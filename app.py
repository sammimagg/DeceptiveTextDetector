from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    text = request.json['text']
    classifier = pipeline('text-classification', model='model')
    result = classifier(text)
    label = result[0]['label']
    score = result[0]['score']
    response = {'label': label, 'score': score}
    return jsonify(response)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
