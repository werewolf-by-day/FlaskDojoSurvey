from flask import Flask, render_template, redirect, request,
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['Post'])
def process():
    comment = request.form['textarea']
    return render_template('results.html', comment = comment)

@app.route('/back', methods=['Post'])
def back():

    return render_template('index.html')

app.run(debug=True)
