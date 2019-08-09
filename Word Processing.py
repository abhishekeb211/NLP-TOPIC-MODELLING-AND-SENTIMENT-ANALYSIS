import pandas as Pd
import numpy as Np
import simplejson
import nltk
import spacy
import matplotlib.pyplot as plt
import gensim
import pyLDAvis.gensim
import os,re,operator,warnings
import pickle
import pyLDAvis.gensim
import string
import random
import re

from nltk.tokenize import word_tokenize
from spacy.lang.en import English
from nltk.corpus import wordnet as wn
from nltk.stem.wordnet import WordNetLemmatizer
from gensim import corpora
from gensim.models import TfidfModel
from gensim.models import CoherenceModel ,LdaModel,DataModel,HdpModel
from gensim.models.wrappers import LdaMallet
from gensim.corpora import Dictionary
from gensim.models.coherencemodel import CoherenceModel

nlp=spacy.load('en_core_web_sm')
warnings.filterwarnings('ignore')


nltk.download('stopwords')

from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))

en_stop = set(nltk.corpus.stopwords.words('english'))
nltk.download('wordnet')
spacy.load('en_core_web_sm')
parser = English()


def tokenize(text):
    Data_tokens = []
    tokens = parser(text)
    for token in tokens:
        if token.orth_.isspace():
            continue
        elif token.like_url:
            Data_tokens.append('URL')
        elif token.orth_.startswith('@'):
            Data_tokens.append('SCREEN_NAME')
        else:
            Data_tokens.append(token.lower_)
    return Data_tokens

def get_lemma(word):
    lemma = wn.morphy(word)
    if lemma is None:
        return word
    else:
        return lemma

def get_lemma2(word):
    return WordNetLemmatizer().lemmatize(word)



def prepare_text_for_Data(text):
    words=[]
    tokens = tokenize(text)
    tokens = [token for token in tokens if len(token) > 4]
    tokens = [token for token in tokens if token not in en_stop]
    tokens = [get_lemma(token) for token in tokens]
        
    for i in tokens:
           
        tokens1 = word_tokenize(i)
                # convert to lower case
        tokens1 = [w.lower() for w in tokens1]
                # remove punctuation from each word
        table = str.maketrans('', '', string.punctuation)
        stripped = [w.translate(table) for w in tokens1]
                # remove remaining tokens that are not alphabetic
        words = [word for word in stripped if word.isalpha()]
                # filter out stop words
        
        words = [w for w in words if not w in stop_words]
        
    for i in range(len(words)):
        if words[i]=='[]':
            del words[i]
        if words[i]=='':
            del words[i]
    
    
     f = open(file, 'w')
     simplejson.dump(text_data, f)
     f.close()        



def Files(file):
    file1=file+'.txt'
    i=0
    text_data = []
    with open(file1) as f3:
        for line in f3:
            eth=line.split(']',100000)
            for wrd in eth:
                tokens = prepare_text_for_Data(wrd)
                if random.random() > .80:
    #                     print(tokens)
                    text_data.append(tokens)

    file=file+"_Token.txt"
    
    for i in range(len(text_data)):
        if text_data[i]=='[]':
            del text_data[i]
        if text_data[i]=='':
            del text_data[i]
    
    print(text_data)
    
     f = open(file, 'w')
     simplejson.dump(text_data, f)
     f.close()        

EFiles=['4_5_WEEK','3_2_WEEK','3_3_WEEK','3_4_WEEK','3_5_WEEK',
       '4_1_WEEK','4_2_WEEK','4_3_WEEK','4_4_WEEK','4_5_WEEK',
       '5_1_WEEK','5_2_WEEK','5_3_WEEK','5_4_WEEK','5_5_WEEK',
       '6_1_WEEK','6_2_WEEK','6_3_WEEK','6_4_WEEK','6_5_WEEK',
       '7_1_WEEK','7_2_WEEK','7_3_WEEK','7_4_WEEK','7_5_WEEK',
       '8_1_WEEK','8_2_WEEK']

for E in EFiles:
    print(E)
    F=Files(E)
    
