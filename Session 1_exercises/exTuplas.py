listA = [(1,2), 40, 50,90, 110, "monday",(1,3), (3,3,5), (45,87), "friday"]

count = 0
for i in listA:
    if type(i) == tuple:
        count = count + 1

print ("Our list is:", listA)
print("The number of tuples contained into out list is:", count)
