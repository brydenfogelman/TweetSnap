import time
import re


filename = time.strftime("%x") + "_1"
currentdate = time.strftime("%x")
print currentdate
print filename

newString = str(currentdate)+"_"
print newString
line = re.sub('[!@#$]', '', newString)
#changed = filename.replace(, "")

print filename