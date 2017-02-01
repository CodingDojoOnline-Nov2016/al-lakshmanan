def oddeven():
    sum = 0
    for val in range(1,2001,1):
        if val % 2 == 0:
            print "Number is ", val, ".This is even Number."
        else:
            print "Number is ", val, ".This is odd Number."
        sum = sum + val
    return sum


result = oddeven()
print result
