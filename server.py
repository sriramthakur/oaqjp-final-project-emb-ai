from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def emo_detector():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    emotions = response['all_scores']
    dominant_emotion = response['dominant_emotion']

    if emotions is None or dominant_emotion is None:
        return "Invalid input! Try again."
    else:
        # Format all scores into a string
        scores_str = ", ".join([f"'{emo}': {score}" for emo, score in emotions.items()])
        return f"For the given statement, the system response is {scores_str}. The dominant emotion is {dominant_emotion}."


@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    #TODO
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)