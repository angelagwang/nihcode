import pandas as pd
import csv

#Load data into dataframe
data = pd.read_csv("CodedNewTweets1.csv", dtype = object)


cat1=data.loc[data['Code']=="1.0"]
cat2=data.loc[data['Code']=="2.0"]
cat3=data.loc[data['Code']=="3.0"]
cat4=data.loc[data['Code']=="4.0"]
cat5=data.loc[data['Code']=="5.0"]
cat6=data.loc[data['Code']=="6.0"]


#Write data frame to csv file 
cat1.to_csv(r"C:\Users\wangang\Documents\Python Code\Code 1 Tweets1.csv")
cat2.to_csv(r"C:\Users\wangang\Documents\Python Code\Code 2 Tweets1.csv")
cat3.to_csv(r"C:\Users\wangang\Documents\Python Code\Code 3 Tweets1.csv")
cat4.to_csv(r"C:\Users\wangang\Documents\Python Code\Code 4 Tweets1.csv")
cat5.to_csv(r"C:\Users\wangang\Documents\Python Code\Code 5 Tweets1.csv")
cat6.to_csv(r"C:\Users\wangang\Documents\Python Code\Code 6 Tweets1.csv")
