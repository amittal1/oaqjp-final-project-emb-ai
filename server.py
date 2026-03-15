from flask import Flask, request, jsonify
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['GET'])
def get_emotion():
    sentence = request.args.get('sentence')
    return jsonify(emotion_detector(sentence))
