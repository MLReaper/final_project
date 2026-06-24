from flask import Flask, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector')
def emotion_detector_route():
    text_to_analyze = request.args.get('textToAnalyze')
    
    if not text_to_analyze:
        return "Invalid text! Please try again!"
    
    result = emotion_detector(text_to_analyze)
    
    if result.get('dominant_emotion') is None:
        return "Invalid text! Please try again!"
        
    anger = result.get('anger')
    disgust = result.get('disgust')
    fear = result.get('fear')
    joy = result.get('joy')
    sadness = result.get('sadness')
    dominant_emotion = result.get('dominant_emotion')

    formatted_response = (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )
    
    return formatted_response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)