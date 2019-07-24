import joblib
import nltk
import string
import re
import csv
import json
import pandas as pd
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from pandas.io.json import json_normalize
from sklearn import ensemble
from sklearn.feature_extraction.text import TfidfVectorizer
import trainalgorithm
from trainalgorithm import dummy_fun

stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()

#Open file
with open('tweets_xah4.jsonl') as f:
    data = pd.DataFrame(json_normalize(json.loads(line) for line in f))

#Clean tweets
def cleanData(tweets):
    final = []
    for item in tweets.split():
        x = item.lower()
        x2 = re.sub('[^ a-zA-Z0-9]', '', x)
        x3 = x2.strip()
        tokens = word_tokenize(x3)
        wordlst = [stemmer.stem(word) for word in tokens if word not in stop_words and not word.isdigit()]
        final.extend(wordlst)
    return final

tokentext = data["full_text"].apply(cleanData)

#Predict code of new tweets from loaded models
clf = joblib.load('final_model.model')
token = joblib.load('token.pkl')

newtext = token.transform(tokentext)
newcategory = clf.predict(newtext).tolist()                   

#Add code for new tweets to existing dataframe
data["Code"] = newcategory

#Only save tweets with code 1-6
data = data[data.Code != 0.0]

#Save new dataframe with specific columns
newdf = data[['full_text','Code', "user.id", "user.location", "retweet_count", "favorite_count"]]

#Write dataframe to csv file
newdf.to_csv(r"C:\Users\wangang\Documents\Python Code\Coded New Tweets28.csv")

