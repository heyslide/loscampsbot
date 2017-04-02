import time, tweepy, os
from linereader import copen
from random import randint

"""tweepy doing its magic"""
CONSUMER_KEY = os.environ['CKEY']
CONSUMER_SECRET = os.environ['CSECRET']
ACCESS_KEY = os.environ['AKEY']
ACCESS_SECRET = os.environ['ASECRET']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

lyrics = copen('lyrics.txt')
lines = lyrics.count('\n')

while True:
    tweet_text = lyrics.getline(randint(1, lines))
    if len(tweet_text) <= 140 and tweet_text != '\n':
	api.update_status(status=tweet_text)
	print tweet_text
	time.sleep(2400)