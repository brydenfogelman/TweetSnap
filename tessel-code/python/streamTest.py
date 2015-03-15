from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json

ckey = 'HeAUdQaZ1dnSoJJguRmUHu0Uz'
csecret = '00EINfdvwz3l5N5a62gTw8dqsQcZ9KWXVWfsqxvCV9ESiAa4nu'
atoken = '3082570099-x5HGUIwv9Y0LhwZeRZnkxlT5ZK2WzbbGG1Y6xWY'
asecret = 'ieP8a2mEvup72IjkiveW77LBLqRpaAVaB4hDkoZy5BJwY'

class listener(StreamListener):

    def on_data(self, data):
        tweetObject = json.loads(data)
        ScreenName = tweetObject['user']['screen_name']
        api.update_with_media(filename=picture ,status='@'+ScreenName+ " Enjoy nwhacks!")
        return True

    def on_error(self, status):
        print status

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
twitterStream.filter(track=["TweetSnap","TweetSnapHack"])