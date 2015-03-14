#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
import os
import tweepy, time, sys
 
#argfile = str(sys.argv[1])
 
#enter the corresponding information from your Twitter application:
CONSUMER_KEY = 'W8dXvXURHM3Iy4k9KiFxkzAox'#keep the quotes, replace this with your consumer key
CONSUMER_SECRET = 'Ntq8N3NrtdxdMmPVYuR2xn4LyMnIv4Fk2pnJewSy9koVFiLvDT'#keep the quotes, replace this with your consumer secret key
ACCESS_KEY = '594338908-7dXACIbKiuColhLysQZd4ezyzhdWmmihy1evgzto'#keep the quotes, replace this with your access token
ACCESS_SECRET = 'vQjq7KXn9pfDbG2rV6QR1ixRkKGifw2NtIdtFxJBqS6B3'#keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

listOfPic = list()
for file in os.listdir("/Users/brydenfogelman/Documents/test/images"):
    if file.endswith(".jpg"):
        listOfPic.append(file)
        
listOfPic.reverse()
#filename=open(argfile,'r')
#f=filename.readlines()
#filename.close()
#api.update_with_media(filename='reofest.jpg',status='testing for nwHacks, sry for the spam')

count = 1
for item in listOfPic:
    picture = str(item)
    os.chdir('/Users/brydenfogelman/Documents/test/images')
    api.update_with_media(filename=picture,status='test')
    #'picture # ' + str(count)
    time.sleep(60)
    count += 1
#Tweet every 15 minutes