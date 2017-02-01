
def multiply(list,multiplier):
    resultlist = []
    for element in list:
        newelement = element * multiplier
        print newelement
        resultlist.append(newelement)
    return resultlist

mylist = [2,4,10,16]
mlist = multiply(mylist,5)
print mlist
