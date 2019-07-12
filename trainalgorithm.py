import nltk
import string
import re
import csv
import sklearn
import pandas as pd
import json
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from pandas.io.json import json_normalize
from sklearn import model_selection, preprocessing, linear_model, metrics
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import decomposition, ensemble
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.externals import joblib

#Clean Tweets
stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()

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

#Load Train Data"
train_data = pd.read_csv("Tweets Coding - CC.csv")
train_df = train_data[train_data['Content'].notnull()]
train_df["Content"]= train_df["Content"].apply(cleanData)
train_df["label"] = "test"

#Load Test Data"
with open('tweets_xaa1.jsonl') as f:
    test_data = pd.DataFrame(json_normalize(json.loads(line) for line in f))

test_data["full_text"]= test_data["full_text"].apply(cleanData)
test_data["label"] = "train"

#Combine Data
concat_df = pd.concat([train_df, test_data], axis = 1)

#Vectorization
def dummy_fun(doc):
    return doc
tfidf_vect = TfidfVectorizer(analyzer='word',tokenizer=dummy_fun, preprocessor=dummy_fun, token_pattern=None)  
tfidf_vect.fit(concat_df["Content"].values.astype("U"))
tfidf_vect.fit(concat_df["full_text"])
                             
#Split Combined Data
training_data = concat_df[concat_df['label'] == "test"]
testing_data = concat_df[concat_df['label'] == "train"]

#Drop Labels
training_data = training_data.drop('label', axis=1)
testing_data = testing_data.drop('label', axis=1)

#Split Test Data into Testing Groups
tftraintext = training_data["Content"]
traincategory = training_data["Code"]

train_x, test_x, train_y, test_y = model_selection.train_test_split(tftraintext, traincategory, test_size = .4)

#Transform Text
xtrain_tfidf = tfidf_vect.transform(train_x)
xtest_tfidf = tfidf_vect.transform(test_x)

#Run Algorithm
classifier = ensemble.RandomForestClassifier()
classifier.fit(xtrain_tfidf, train_y)
predictions = classifier.predict(xtest_tfidf)

print(metrics.accuracy_score(predictions, test_y))

joblib.dump(classifier, "final_model.model")
joblib.dump(tfidf_vect, "token.pkl")

