from __future__ import print_function
import os
for file in os.listdir("/Users/brydenfogelman/Documents/test/images"):
    if file.endswith(".jpg"):
        print(file)
        #add to list instead
        
listOfPic = list()
for file in os.listdir("/Users/brydenfogelman/Documents/test/images"):
    if file.endswith(".jpg"):
        print(file)
        listOfPic.append(file)
        
listOfPic.reverse()

print (listOfPic)