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
from sklearn.svm import SVC


stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()

data = pd.read_csv("4000Tweets Codingedit - CC.csv")

#Preprocesing data
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

#Model building
def train_model(classifier, feature_vector_train, label, feature_vector_valid, is_neural_net=False):
    classifier.fit(feature_vector_train, label)
    predictions = classifier.predict(feature_vector_valid)
    if is_neural_net:
        predictions = predictions.argmax(axis=-1)
    return metrics.accuracy_score(predictions, test_y)

#Accuracy of different models
"1. Native Bayes on Word Level TF IDF Vectors"
accuracynb = train_model(naive_bayes.MultinomialNB(), xtrain_tfidf, train_y, xtest_tfidf)
print("NB, WordLevel TF-IDF: ", accuracynb)

"2. Linear Classifier on Word Level TF IDF Vectors"
accuracylc = train_model(linear_model.LogisticRegression(), xtrain_tfidf, train_y, xtest_tfidf)
print("LR, WordLevel TF-IDF accuracy: ", accuracylc)

"3. Random Forest on Word Level TF IDF Vectors"
accuracyrf = train_model(ensemble.RandomForestClassifier(), xtrain_tfidf, train_y, xtest_tfidf)
print("RF, WordLevel TF-IDF: ", accuracyrf)

"4. Extreme Gradient Boosting on Word Level TF IDF Vectors"
accuracyxgb = train_model(xgb.XGBClassifier(), xtrain_tfidf.tocsc(), train_y, xtest_tfidf.tocsc())
print("XGB, WordLevel TF-IDF: ", accuracyxgb)

"5. Support Vector Machine on Word Level TF IDF Vectors"
accuracysvm = train_model(svm.SVC(), xtrain_tfidf, train_y, xtest_tfidf)
print("SVM, WordLevel TF-IDF: ", accuracysvm)
