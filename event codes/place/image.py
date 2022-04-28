from flask import Flask, send_from_directory
from threading import Thread
app=Flask(__name__)
@app.route('/full.png')
def raw():
    return send_from_directory('.', 'full.png')
@app.route('/')
def index():
    return send_from_directory('.', 'raw.png')
def run():
  app.run(host='0.0.0.0',port=8080)

def image_run():  
    t = Thread(target=run)
    t.start()