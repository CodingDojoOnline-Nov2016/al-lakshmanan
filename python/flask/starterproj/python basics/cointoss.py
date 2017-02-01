import random

def tosscoin():
    tossspin = random.random()
    toss = round(tossspin)
    return toss


head=0
tail=0

for i in range(0,5000,1):
    result = tosscoin()
    if result == 0:
        tail = tail + 1
        print "Attempt #1: Throwing a coin... It's a tail! ... Got", tail ," tail(s) so far and",  head ,"head(s) so far"
    else:
        head = head + 1
        print "Attempt #1: Throwing a coin... It's a head! ... Got", head ," head(s) so far and",  tail ,"tail(s) so far"
