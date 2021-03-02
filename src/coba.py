import os
from os import listdir
from os.path import isfile, join
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
from extraction import *


app = Flask('ibnu_apps')
path = os.getcwd() + '/direktori'
app.config['UPLOAD_FOLDER'] = path

@app.route('/')
def upload_file():
    findFiles = [file for file in listdir(path) if isfile(join(path, file))]
    for element in findFiles:
        os.remove(path+'/'+element)
    return render_template('upload_file.html')

@app.route('/select_algorithm', methods=['POST'])
def select_algorithm():
    files = request.files.getlist("file")
    for file in files:
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return render_template('select_algorithm.html')

@app.route('/perihal')
def perihal():
    return render_template('perihal.html')

@app.route('/results', methods=['POST'])
def results():
    text = request.form['keyword']
    option = request.form['pilihan']
    findFiles = [file for file in listdir(path) if isfile(join(path, file))]
    direktori=""
    for element in findFiles:
        direktori=path+'/'+element
    algo=extraction(direktori, text, option)
    result=[algo.getHasil(), text]
    return render_template('results.html', hasil=result)

if __name__ == '__main__':
    app.run(debug=True)

