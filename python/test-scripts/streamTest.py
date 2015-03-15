from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import tweepy, time, sys

picture = str(sys.argv[1])

CONSUMER_KEY = 'KrYDiF0Aqu6RTgXzkEdtdpuGB'
CONSUMER_SECRET = 's7tYSprUgNEo8TOcSCmhBP9cx6SikGEzC2hp38C2JzeTdt46ZG'
ACCESS_KEY = '3082570099-x5HGUIwv9Y0LhwZeRZnkxlT5ZK2WzbbGG1Y6xWY'
ACCESS_SECRET = 'ieP8a2mEvup72IjkiveW77LBLqRpaAVaB4hDkoZy5BJwY'

class listener(StreamListener):
    
    def __init__(self, api, picture):
        self.api = api
        self.picture = picture
        
    def on_data(self, data):
        tweetObject = json.loads(data)
        ScreenName = tweetObject['user']['screen_name']
        if ScreenName != "TweetSnapHack":
            self.api.update_with_media(filename=self.picture ,status='@'+ScreenName+ " Enjoy nwhacks!")
            print "Tweeted at " + ScreenName + "!"
        return True

    def on_error(self, status):
        print "error" + status

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
twitterStream = Stream(auth, listener(api, picture))
twitterStream.filter(track=["TweetSnapHack"])
