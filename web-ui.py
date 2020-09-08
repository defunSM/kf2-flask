from flask import Flask
from flask import render_template, send_from_directory, request, flash, redirect
import flask_login
from getMutatorInfo import getWorkShopInfo
from getId import getWorkShopId
from selectDir import selectDir

import os
import platform
import subprocess

def open_file(path):
    if platform.system() == "Windows":
        os.startfile(path)
    elif platform.system() == "Darwin":
        subprocess.Popen(["open", path])
    else:
        subprocess.Popen(["xdg-open", path])

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Remember to change this in production

login_manager = flask_login.LoginManager()
login_manager.init_app(app)

mods = []
kf_path_folder = "undefined"
mod_folder = "undefined"

user_id = 123
cwd = os.getcwd()  # Current working directory

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

@app.route('/')
def hello_world():
    return render_template('index.html', mods=mods)

@app.route('/', methods=['POST'])
def my_form_post():
    if request.form['name']:
        text = request.form['name']
        if text == "path":
            pass
        id = getWorkShopId(text)
        if id==0:
            flash('Looks like you entered an invalid Workshop ID or URL! ')
            return render_template('index.html', mods=mods)
            
        mod_info = getWorkShopInfo(id)

        # processed_text = text.upper()
        mods.append(mod_info)
        return render_template('index.html', mods=mods)
    elif 'mods' in request.form:
        return render_template('index.html', mods=mods)
    else:
        return redirect('/settings')

@app.route('/settings', methods=['POST', 'GET'])
def my_settings():
    global kf_path_folder
    global mod_folder
    if request.method == 'POST':
        kf_path_folder = selectDir()
        return render_template('settings.html', kf_path=kf_path_folder, mod_path=mod_folder)
    else:
        return render_template('settings.html', kf_path=kf_path_folder, mod_path=mod_folder)