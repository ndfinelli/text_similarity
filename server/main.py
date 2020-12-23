#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask import render_template, jsonify, request, session
import json

from model.TextSimilarity import TextSimilarity

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html.j2')

@app.route('/text_similarity_comparison', methods=['POST'])
def text_similarity_comparison():
    # We are able to assume that the request is a json dictionary coming in.
    texts = json.loads(request.data)['texts']

    compare = TextSimilarity(texts[0], texts[1])
    return str(compare.calculate_similarity_score())

def run():
    app.run(host ='0.0.0.0', port = 5000)

if __name__ == '__main__':
    run()