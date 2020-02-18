
# """
# A python script to nuke tweets in your account

# @requirements: tweepy, python-dotenv
# @author: github.com/actualdragon
# """
from os import getenv
from os.path import join, dirname
from dotenv import load_dotenv

import tweepy
# import csv
# import jsonlines

# Load env file
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Access env variables
consumer_key = getenv('CONSUMER_KEY')
consumer_secret = getenv('CONSUMER_SECRET')
access_token = getenv('ACCESS_TOKEN')
access_token_secret = getenv('ACCESS_TOKEN_SECRET')
tweets_to_keep = getenv('TWEETS_TO_KEEP').split(',')
tweets_csv = getenv('PATH_TO_TWEETS')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

print('OAuth request sent')
api = tweepy.API(auth)

print('OAuth successful, now loading tweets archive')
# with open(tweets_csv, 'r') as f:
#     reader = csv.reader(f)

#     # Skip header
#     next(reader, None)

#     # Convert CSV to list
#     tweets_list = list(reader)

# print('Nuking...')
# for tweet in tweets_list:
#     # tweet[0] is the tweet_id column
#     tweet_id = tweet[0]

#     if (tweet_id in tweets_to_keep):
#         # Do not delete tweet
#         print('[ 0 ] tweet with id %s' % (tweet_id))
#     else:
#         # Delete the tweet
#         api.destroy_status(tweet_id)
#         print('[ - ] tweet with id %s' % (tweet_id))

# print('Mission complete!')
import twitter
import sys
# from twitter import Twitter

# twitter = Twitter(auth(consumer_key, consumer_secret, access_token, access_token_secret))

okay = twitter.Api(consumer_key, consumer_secret, access_token, access_token_secret)

filepath = sys.argv[0]
with open(tweets_csv, encoding="utf8") as tweets:
    tweetID = tweets.readline()
    while tweetID:
        print(tweetID)
        try:
            api.destroy_status(tweetID.rstrip(), trim_user=False)
        except:
            print('No such tweet')
        tweetID = tweets.readline()