#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
import os
import tweepy, time, sys
 
picture = str(sys.argv[1])
 
#enter the corresponding information from your Twitter application:
CONSUMER_KEY = 'HeAUdQaZ1dnSoJJguRmUHu0Uz'#keep the quotes, replace this with your consumer key
CONSUMER_SECRET = '00EINfdvwz3l5N5a62gTw8dqsQcZ9KWXVWfsqxvCV9ESiAa4nu'#keep the quotes, replace this with your consumer secret key
ACCESS_KEY = '3082570099-x5HGUIwv9Y0LhwZeRZnkxlT5ZK2WzbbGG1Y6xWY'#keep the quotes, replace this with your access token
ACCESS_SECRET = 'ieP8a2mEvup72IjkiveW77LBLqRpaAVaB4hDkoZy5BJwY'#keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

lastMentions = api.mentions_timeline(count=1)
mentionItem = lastMentions.pop()
print (mentionItem)
print (lastMentions)
user = mentionItem.user.screen_name
#os.chdir("/Users/brydenfogelman/Documents/nwHacks/TweetSnap/tessel-code/camera")
api.update_with_media(filename=picture ,status='@'+user+ " Enjoy nwhacks!")
        
#while True:
 #   mentions = api.mentions_timeline(count=1) # is a list
  #  mentionItem = mentions.pop()
   # 
    #if lastMentions != mentionItem:
     #   #do shit here
      #  lastMentions = (mentionItem)
       # print (lastMentions)
        ##This will create the tweet
        #user = mentionItem.user.screen_name
        #os.chdir("/Users/brydenfogelman/Documents/nwHacks/TweetSnap/tessel-code/camera")
        #api.update_with_media(filename=picture ,status='@'+user+ " Enjoy nwhacks!")