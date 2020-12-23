#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pathlib import Path

from utility import use_project_path
from model.TextSimilarity import *

if __name__ == '__main__':
    use_project_path()

    sample1 = Path('data/sample1.txt').read_text()
    sample2 = Path('data/sample2.txt').read_text()
    sample3 = Path('data/sample3.txt').read_text()

    compare1to2 = TextSimilarity(sample1, sample2)
    compare1to3 = TextSimilarity(sample1, sample3)
    compare2to3 = TextSimilarity(sample2, sample3)

    print("Similarity Score 1&2: " + str(compare1to2.calculate_similarity_score()))
    print("Similarity Score 1&3: " + str(compare1to3.calculate_similarity_score()))
    print("Similarity Score 2&3: " + str(compare2to3.calculate_similarity_score()))