from textblob import TextBlob
import re
import csv
import pandas as pd
import nltk
import json
from pandas.io.json import json_normalize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()

data = pd.read_csv("CodedNewTweets1.csv")

#Clean tweets
def cleanData(tweets):
    final = []
    for item in tweets.split():
        x = item.lower()
        x2 = re.sub('[^ a-zA-Z0-9]', '', x)
        x3 = x2.strip()
        final.append(x3)
    return " ".join(final)

#Get sentiment
def tweetSentiment(tweet): 
    analysis = TextBlob(tweet) 
    if analysis.sentiment.polarity > 0: 
        return 'positive'
    elif analysis.sentiment.polarity == 0: 
        return 'neutral'
    else: 
        return 'negative'
    
df = data[data['full_text'].notnull()]
df['full_text']= df['full_text'].apply(cleanData)
text = df['full_text']

#Assign sentiment to each tweet
tweets = []
for item in text:
    tweetanalysis = {}
    tweetanalysis["text"]= item
    tweetanalysis["sentiment"] = tweetSentiment(item)
    tweets.append(tweetanalysis)

#List of positive/negative/neutral tweets
postweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
negtweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
neuttweets = [tweet for tweet in tweets if tweet['sentiment'] == 'neutral']

#Percentage of positive/negative/neutral tweets
print("Positive tweets percentage: {} %".format(100*len(postweets)/len(tweets))) 
print("Negative tweets percentage: {} %".format(100*len(negtweets)/len(tweets))) 
print("Neutral tweets percentage: {} %".format(100*len(neuttweets)/len(tweets)))

print(postweets)
print(negtweets)
print(neuttweets)

