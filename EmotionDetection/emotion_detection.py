import requests

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    payload = {"raw_document": {"text": text_to_analyze}}
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    response = requests.post(url, json=payload, headers=headers)
    if response.status_code != 200:
        return None

    data = response.json()

    # Extract the first prediction’s emotion scores
    emotions = data['emotionPredictions'][0]['emotion']

    # Find the dominant emotion
    dominant_emotion = max(emotions, key=emotions.get)
    dominant_score = emotions[dominant_emotion]

    return {
        "all_scores": emotions,
        "dominant_emotion": dominant_emotion,
        "dominant_score": dominant_score
    }