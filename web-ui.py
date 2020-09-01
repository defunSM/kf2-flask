from flask import Flask
from flask import render_template, send_from_directory, request
app = Flask(__name__)

mods = []

@app.route('/')
def hello_world():
    return render_template('index.html', mods=mods)

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['name']
    processed_text = text.upper()
    mods.append(processed_text)
    return render_template('index.html', mods=mods)