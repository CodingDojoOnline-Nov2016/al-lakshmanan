for count in range(0,5):
    print "looping - ", count

mylist = [4,'dog',99,['list','inside','another'],'helloworld']
for element in mylist:
    print element

count=0
while count < 5:
    print count
    count+=1

for val in "string":
    if val == 'i':
        continue
    print val
