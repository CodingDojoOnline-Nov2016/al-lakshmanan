def grade(scores):
    if scores >= 60 and scores < 70:
        print "Score: ", scores , "; Your grade is D"
    elif scores >= 70 and scores < 80:
        print "Score: ", scores , "; Your grade is c"
    elif scores >= 80 and scores < 90:
        print "Score: ", scores , "; Your grade is B"
    elif scores >= 90 and scores < 100:
        print "Score: ", scores , "; Your grade is A"

def getinput():
    count = 0
    while count < 9:
        print "Please enter the score"
        try:
            score = int(raw_input())
        except:
            print "Nope"
            score=0
        if score > 59 and score < 101:
            print "entered score is", score
            grade(score)
            count = count + 1
        else:
            print "score is invalid"
            print "Please Re-enter the score between 60 and 100"
            score = raw_input()

print "Scores and Grades"
getinput()
print "End of the Program - Bye!"
