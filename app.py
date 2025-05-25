from flask import Flask, render_template, request
from emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/form')
def form():
    return render_template('form.html')

from flask import request  # en üstte bu da olmalı

@app.route('/greet', methods=['POST'])
def greet():
    name = request.form['username']
    return f'<h1>Merhaba, {name}!</h1>'

@app.route('/analyze')
def show_analyze_page():
    return render_template('analyze.html')

@app.route('/emotionDetector')
def emotion_analyzer():
    text_to_analyze = request.args.get('textToAnalyze')

    if not text_to_analyze:
        return "Invalid text! Please try again!"

    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    return (
        f"For the given statement, the system response is:<br>"
        f"Anger: {response['anger']}<br>"
        f"Disgust: {response['disgust']}<br>"
        f"Fear: {response['fear']}<br>"
        f"Joy: {response['joy']}<br>"
        f"Sadness: {response['sadness']}<br><br>"
        f"<b>Dominant emotion is: {response['dominant_emotion']}</b>"
    )


if __name__ == '__main__':
    app.run(debug=True)
