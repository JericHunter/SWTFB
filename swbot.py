import tweepy
import time

app_key = 'rCguhoSNkQGrj2WfowC0iI4rj'
app_secret = 'nMU6MarVejiIpTPCx7aYrHwuiawbRywh13lXhXOuymbz77BieZ'
access_token = '992987135723687936-bJDIDdI8frBErPbyx6V9rYuneWtm3CX'
access_token_secret= 'tkYmrFRQJFWYpS33AzAighKPIjTin4UJCOEcWRWeLvH2G'


auth = tweepy.OAuthHandler(app_key, app_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

hashtag = ["#Sith", "StarWars", "Lightsabers"]
tweetCount = 20

tweets = tweepy.Cursor(api.search, hashtag).items(tweetCount)

def searchBot():
    for tweet in tweets:
        try:
            tweet.retweet()
            api.create_favorite(tweet.id)
            time.sleep(2)
        except tweepy.TweepError as e:
            print(e.reason)
            time.sleep(2)
searchBot()
