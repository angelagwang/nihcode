import nltk
import string
import re
import csv
import sklearn
import pandas as pd
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from sklearn import model_selection, preprocessing, linear_model, naive_bayes, metrics, svm
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import decomposition, ensemble
import xgboost as xgb
import joblib
from sklearn.metrics import confusion_matrix



stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()

#Load data
data = pd.read_csv("4000Tweets Codingedit - CC.csv")

#Preprocessing of data
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

df = data[data['Content'].notnull()]
df["Content"]= df["Content"].apply(cleanData)
text = df["Content"]
category = df["Code"]

#Feature engineering:Fit TF-IDF vectors
def dummy_fun(doc):
    return doc

tfidf_vect = TfidfVectorizer(analyzer='word',tokenizer=dummy_fun, preprocessor=dummy_fun, token_pattern=None)  
tfidf_vect.fit(text)

#Train/Test split
train_x, test_x, train_y, test_y = model_selection.train_test_split(text, category, test_size = .3)

#Feature engineering:Transform using TF-IDF vectors
xtrain_tfidf = tfidf_vect.transform(train_x)
xtest_tfidf =  tfidf_vect.transform(test_x)

#Fit algorithm on test data
classifier = ensemble.RandomForestClassifier(n_estimators = 200, max_features = 600, max_depth = 35, random_state = 42, n_jobs = -1)
classifier.fit(xtrain_tfidf, train_y)
predictions = classifier.predict(xtest_tfidf)
conf_mat = confusion_matrix(test_y, predictions)
print(conf_mat)

print(metrics.accuracy_score(predictions, test_y))

#Save classifier and vector into files 
#joblib.dump(classifier, "final_model.model")
#joblib.dump(tfidf_vect, "token.pkl")
