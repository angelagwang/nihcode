import botometer
import tweepy
import requests
import json
import pandas as pd

mashape_key = "d57aae6b38mshcf009c305cb1879p18955djsn5a1e9d4545b1"
twitter_app_auth = {
    'consumer_key': 'MWsghMJdDgnEl4nsOBq04L64n',
    'consumer_secret': 'UhkoYodgkRXE0RkvwWRHfkIoZHEQAHCEfBepCwk3XJ7ybrk08V',
    'access_token': '2832787137-Yr7lRfCFasRyEQ6jYHTonSAHDY29NMNisYIlP39',
    'access_token_secret':'nzN3HZlkFZhuyfXrrbzW80SGbzzkH1pBLFiokDvsGhE3U',
  }

bom = botometer.Botometer(wait_on_ratelimit=True,
                          mashape_key=mashape_key,
                          **twitter_app_auth)

data = pd.read_csv("Code6Tweets4.csv", engine = "python", error_bad_lines=False)
accounts = data["user.id"]

tally = 0
for screen_name, result in bom.check_accounts_in(accounts):
    try:
        if result["scores"]["english"] > .5:
            tally +=1
    except KeyError:
        continue

print(tally)
