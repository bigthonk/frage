from flask import Flask, render_template, request
import time
import logging
import search
import requests

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search/results', methods=['GET', 'POST'])
def search_request():
    start_time = time.time()
    search_term = request.form["input"]
    res = requests.get('http://frage_backend:3000/search?search_term='+search_term).json()
    finish_time = time.time()
    elapsed_time = finish_time - start_time
    return render_template('results.html', res=res )

if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(host='0.0.0.0', port=5000)