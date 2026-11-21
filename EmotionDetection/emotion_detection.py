import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header)
    if response.status_code == 200:
        formatted_response = json.loads(response.text)
        output = formatted_response["emotionPredictions"][0]
        res = {
                'anger': output["emotion"]["anger"],
                'disgust': output["emotion"]["disgust"],
                'fear': output["emotion"]["fear"],
                'joy': output["emotion"]["joy"],
                'sadness': output["emotion"]["sadness"],
                'dominant_emotion': dominant_emotion(output["emotion"])
                }
    elif response.status_code == 400:
        res = {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None
                }
    else:
        res = {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None
                }
    return res

def dominant_emotion(jsonData):
    dominant_key = None
    for key in jsonData:
        if dominant_key is None or jsonData[key] > jsonData[dominant_key]:
            dominant_key = key

    return dominant_key