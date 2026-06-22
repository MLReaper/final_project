import json
import requests

def emotion_detector(text_to_analyze):
    # URL for the Watson NLP Emotion Predict function
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Headers
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Input JSON format using the text_to_analyze variable
    input_json = {"raw_document": {"text": text_to_analyze}}
    
    # Send a POST request to the Watson NLP service
    response = requests.post(url, json=input_json, headers=headers)
    
    # Convert the response text into a dictionary using the json library
    response_dict = json.loads(response.text)
    
    # Content formatting
    emotions = response_dict['emotionPredictions'][0]['emotion']
    
    # Emotions and their scores
    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']
    
    # Write the code logic to find the dominant emotion (emotion with the highest score)
    emotion_scores = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }
    
    # The max() function finds the dictionary key with the highest value
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)
    
    # Return formatted dictionary
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }
