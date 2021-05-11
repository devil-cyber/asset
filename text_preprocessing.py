import csv
import numpy as np
from nltk.corpus import stopwords
from tqdm import tqdm
import pandas as pd
import dask.dataframe as dd
from nltk.tokenize import word_tokenize
class TextPreProcessing:
    def __init__(self,path):
        self.path = path
        self. STOPWORDS = set(stopwords.words('english'))

    def PreProcess(self):
        df = pd.read_csv(self.path,chunksize=100)
        df = pd.concat(df)
        article = ""
        articles = df['text']
        article_list = []
        for i in tqdm(range(len(df))):
            words = word_tokenize(articles[i])
            for word in words:
                if word not in self.STOPWORDS:
                    article = article + " " + word
                    article_list.append(article)




tp = TextPreProcessing('./bbc-text.csv')

tp.PreProcess()




