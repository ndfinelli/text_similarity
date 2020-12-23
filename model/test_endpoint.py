#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
from pathlib import Path

from utility import use_project_path

if __name__ == "__main__":
    use_project_path()

    #Load sample data
    sample1 = Path('data/sample1.txt').read_text()
    sample2 = Path('data/sample2.txt').read_text()
    sample3 = Path('data/sample3.txt').read_text()

    data = {'texts': [sample1, sample2]}

    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    response = requests.post('http://localhost:5000/text_similarity_comparison', data=json.dumps(data), headers=headers)
    print("Text Comparison Samples 1 & 2: " + response.text)

    data = {'texts': [sample1, sample3]}
    response = requests.post('http://localhost:5000/text_similarity_comparison', data=json.dumps(data), headers=headers)
    print("Text Comparison Samples 1 & 3: " + response.text)

    data = {'texts': [sample2, sample3]}
    response = requests.post('http://localhost:5000/text_similarity_comparison', data=json.dumps(data), headers=headers)
    print("Text Comparison Samples 2 & 3: " + response.text)