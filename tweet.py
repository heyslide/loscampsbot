import time, tweepy
from linereader import copen
from random import randint

"""tweepy doing its magic"""
CONSUMER_KEY = 'bM86WKsdFEJgrWlBrUY3KCSni'
CONSUMER_SECRET = '8T43isXZlIIwlOxrwPLg0AAajWjLlNvfTDydkzAVIFRHfvq7Fg'
ACCESS_KEY = '848238932328402945-Kvzj1xXS3eurZOPOVaXP9drkIB4jOw4'
ACCESS_SECRET = 'hdEPrSMGGKK2PXidlhFHWvaWNHiUeSjeUu56PMsj2pxNv'

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
	time.sleep(20*60)