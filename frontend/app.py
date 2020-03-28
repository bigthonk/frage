from flask import Flask, render_template, request
from elasticsearch import Elasticsearch
import time
import logging
import search

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
es = Elasticsearch(
    ['localhost'],
    port=9200

)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search/results', methods=['GET', 'POST'])
def search_request():
    start_time = time.time()
    search_term = request.form["input"]
    res = search.search(search_term)
    finish_time = time.time()
    elapsed_time = finish_time - start_time
    logging.debug("Query took : " + str(elapsed_time) + " seconds to run.")

    return render_template('results.html', res=res )

if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(host='0.0.0.0', port=5000)