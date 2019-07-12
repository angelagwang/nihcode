import joblib
import nltk
import string
import re
import json
import pandas as pd
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from pandas.io.json import json_normalize
from sklearn import ensemble
from sklearn.datasets.samples_generator import make_blobs
from sklearn.feature_extraction.text import TfidfVectorizer
import practicepredictold 
from practicepredictold import dummy_fun

stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()

"Open File"
with open('tweets_xaa1.jsonl') as f:
    data = pd.DataFrame(json_normalize(json.loads(line) for line in f))

"Clean Tweets"
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

data["full_text"]= data["full_text"].apply(cleanData)

"Predict Category from Model"
clf = joblib.load('final_model.model')
token = joblib.load('token.pkl')

#token.fit(data["full_text"])
newtext = token.transform(data["full_text"])
newcategory = [clf.predict(newtext)]                    

"Make DataFrame"
list_of_tuples = list(zip(data["full_text"], newcategory))  
df = pd.DataFrame(list_of_tuples)
print(df.head())

