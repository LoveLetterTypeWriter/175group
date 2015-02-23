import json
import pandas as pd
import matplotlib.pyplot as ply
import re

tweets_data_path = 'twitter_data.txt'
companies = ['apple','microsoft','amazon','google']

#Check if tweet relates to a certain company
def group_by_company(hashtags, text):
	text = text.lower()
	for hashtag in hashtags:
		hashtag = hashtag.lower()
		match = re.search(re.escape(hashtag), text)
		if match:
			return True
	return False
	
#Add to score if match found
def weight_text(word, value, text):
    word = word.lower()
    text = text.lower()
    match = re.search(word, text)
    if match:
        return value
    return 0
	
#Get the score for a group of hashtags
def analyze_column(col, list):
	#Not done
	score = 0
	for tweet in col:
		for word in list:
			score += weight_text(word,2,tweet) #todo
	return score
	
#PROGRAM STARTS HERE
#
	# working from http://pandas.pydata.org/pandas-docs/dev/generated/pandas.DataFrame.html
    # http://adilmoujahid.com/posts/2014/07/twitter-analytics/
    #we are using tweepy (google tweepy)
	
	
#Read the file
tweets_data = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        print("herp")
    
#Create the tweet structure
tweets = pd.DataFrame()
tweets['text'] = list(map(lambda tweet: tweet['text'], tweets_data))
    
#Assemble the hashtag lists
#Make sure there is a corresponding text file for each company (e.g. if apple is a company, there must be an apple.txt file)
hashtag_dict = {}
for company in companies:
	try:
		file_path = company + ('.txt')
		print(file_path)
		hashtag_file = open(file_path, "r")
		hashtag_list = []
		for line in hashtag_file:
			hashtag_list.append(line)
		hashtag_dict[company] = hashtag_list
	except:
		print("derp")

#Use group by company to create proper colums
for company in companies:
	tweets[company] = tweets['text'].apply(lambda tweet: group_by_company(hashtag_dict[company], tweet))

#TODO grab the word map from a file and create a list of words and a dictionary mapping words to values


input("Hit return to continue")
