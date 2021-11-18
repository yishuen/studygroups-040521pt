from flask import Flask, request, render_template

from functions import *

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods = ['GET'])
def render_classifier():
    return render_template('classifier.html')

@app.route('/', methods = ['POST'])
def predict():
    text = request.form.get('text')
    prediction = classify_text(text)
    if prediction == 0:
        return render_template('nope.html', variable = text)
    if prediction == 1:
        return render_template('twss.html', variable = text)

@app.route('/test')
def test():
    return 'hi this is a test'


@app.route('/test2')
def test2():
    return 'hi this is another test'

if __name__ == '__main__':
    app.run()
