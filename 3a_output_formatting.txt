import requests
import json

URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

def emotion_detector(text_to_analyse):
    input_json= { "raw_document": { "text": text_to_analyse } }
    response = requests.post(URL, json=input_json, headers=HEADERS)
    res = response.json()
    emotions = res['emotionPredictions'][0]['emotion']
    dominant = max(emotions, key=emotions.get)
    emotions['dominant_emotion'] = dominant

    formatted_json_string = json.dumps(emotions, indent=4)

    return formatted_json_string
