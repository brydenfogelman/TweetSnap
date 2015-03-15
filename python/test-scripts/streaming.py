from slistener import SListener
import time, tweepy, sys

## authentication
#CONSUMER_KEY = 'HeAUdQaZ1dnSoJJguRmUHu0Uz'
#CONSUMER_SECRET = '00EINfdvwz3l5N5a62gTw8dqsQcZ9KWXVWfsqxvCV9ESiAa4nu'
#ACCESS_KEY = '3082570099-x5HGUIwv9Y0LhwZeRZnkxlT5ZK2WzbbGG1Y6xWY'
#ACCESS_SECRET = 'ieP8a2mEvup72IjkiveW77LBLqRpaAVaB4hDkoZy5BJwY'
CONSUMER_KEY = 'W8dXvXURHM3Iy4k9KiFxkzAox'#keep the quotes, replace this with your consumer key
CONSUMER_SECRET = 'Ntq8N3NrtdxdMmPVYuR2xn4LyMnIv4Fk2pnJewSy9koVFiLvDT'#keep the quotes, replace this with your consumer secret key
ACCESS_KEY = '594338908-7dXACIbKiuColhLysQZd4ezyzhdWmmihy1evgzto'#keep the quotes, replace this with your access token
ACCESS_SECRET = 'vQjq7KXn9pfDbG2rV6QR1ixRkKGifw2NtIdtFxJBqS6B3'#keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

def main():
    track = ['TweetSnap','TweetSnapHack']
 
    listen = SListener(api, 'myprefix')
    stream = tweepy.Stream(auth, listen)

    print "Streaming started..."

    try: 
        stream.filter(track = track)
    except:
        print "error!"
        stream.disconnect()

if __name__ == '__main__':
    main()