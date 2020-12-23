#!/usr/bin/env python
# -*- coding: utf-8 -*-
import string

from utility import use_project_path

class TextSimilarity:
    ''' 
    Class that is used to calculate a similarity score between two texts
    ...
    Attributes
    ----------
    text1: str
        The first text we wish to compare in the calculating of the similarity score
    text2: str
        The second text we wish to compare in the calculation of the similarity score

    Methods
    ----------
    calculate_similarity_score()
        Modifies the two input texts by adjusting casing, removing punctuation & stopwords, tokenizing texts, 
        and then calculates/returns the jaccard_score as the similarity score.
    '''
    def __init__(self, text1, text2):
        self.text1 = text1
        self.text2 = text2
    
    def calculate_similarity_score(self):
        '''Modifies the two input texts and then calculates/returns the jaccard_score as the similarity score.'''
        self.__make_lower_case()
        self.__remove_punctuation()
        self.__tokenize_texts()
        self.__remove_stop_words()
        return(self.__calculate_jaccard())

    def __make_lower_case(self):
        self.text1 = self.text1.lower()
        self.text2 = self.text2.lower()
    
    def __remove_punctuation(self):
        for punct_mark in string.punctuation:
            self.text1.replace(punct_mark, '')
            self.text2.replace(punct_mark, '')

    def __tokenize_texts(self):
        self.text1 = self.text1.split()
        self.text2 = self.text2.split()
    
    def __remove_stop_words(self):
        '''Reads all stop words from model/stop_words.txt and removes them from both texts. Must be called after __tokenize_texts()'''
        use_project_path()
        with open('model/stop_words.txt', 'r') as f:
            stop_words = [stop_word.rstrip() for stop_word in f]

        self.text1 = [word for word in self.text1 if word not in stop_words]
        self.text2 = [word for word in self.text2 if word not in stop_words]
    
    def __calculate_jaccard(self):
        # Combine both tokens to find union.
        both_tokens = self.text1 + self.text2
        union = set(both_tokens)

        # Calculate intersection.
        intersection = set()
        for w in self.text1:
            if w in self.text2:
                intersection.add(w)

        jaccard_score = len(intersection)/len(union)
        return jaccard_score
