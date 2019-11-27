from tweepy import API
from tweepy import Cursor

from tweepy.streaming import StreamListener
from tweepy import Stream
from tweepy import OAuthHandler

print("Please insert the username of the account you would like to analyze")
user = input()
print("What is the first term you would like to analyze")
term1 = input()
print("would you like to analyze a second term? Y/N")

if(input == 'Y'):
    term2 = input()
    print("would you like to analyze a third term? Y/N")
    term3 = input()
    term4 = input()

ACCESS_TOKEN = ""
ACCESS_TOKEN_SECRET = ""
CONSUMER_KEY = ""
CONSUMER_SECRET = ""

class TwitterClient():
    def __init__(self):
        self.auth = TwitterAuthenticator().authenticate_twitter_app
        self.twitter_client = API(self.auth)

        def get_tweets(self, num_tweets):
            tweets = []
            for tweet in Cursor(self.twitter_client.user_timeline).items(num_tweets):
                tweets.append(tweet)
            return tweets


class TwitterAuthenticator():
    def authenticate_twitter_app(self):
        auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        return auth

class TwitterStreamer():

    def __init__(self):
        self.twitter_authenticator = TwitterAuthenticator()

    def stream_tweets(self, fetched_tweets_filename, hash_tag_list):
    
        listener = TwitterListener()
        auth = self.twitter_authenticator.authenticate_twitter_app()
        stream = Stream(auth, listener)

        stream.filter(track= [term1, term2, term3, term4])
    

class TwitterListener(StreamListener):

    def __init__(self, fetched_tweets_filename):
        self.fetched_tweets_filename = fetched_tweets_filename

    def on_data(self, data):
        try:
            print(data)
            with open(self.fetched_tweets_filename, 'a') as tf: 
                tf.write(data)
            return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))

    def on_error(self, status):
        if(status == 420):
            return False
        print(status)
    
if name__=="__main__":
    
    hash_tag_list = [term1, term2, term3, term4]
    fetched_tweets_filename = "tweets.json"

    twitter_streamer = TwitterStreamer()
    twitter_streamer.stream_tweets(fetched_tweets_filename, hash_tag_list)
