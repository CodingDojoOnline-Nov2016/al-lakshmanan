import random
typeofdice = 6
numberofdice = 2

diceresult=0
result=0
flag = 0

for i in range(numberofdice):

    while flag is 0:
        dicetoss = random.random()
        diceresult = int(dicetoss * 10)
        if diceresult > 0 and diceresult <= typeofdice:
            flag = 1
            print diceresult
    result = result + diceresult
    flag=0

print result
