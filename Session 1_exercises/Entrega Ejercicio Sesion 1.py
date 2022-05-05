#####String Exercises
####

import re

#exercise 1

nameUser = input("Please Insert your full name: ")
print(nameUser.upper(), " is ", len(nameUser), " characters long. (counting spaces)")

#exercise 2

stringName = input("Please Insert an alphanumeric string: ")
print("Thanks")
charOne = input("Please Insert an alphabetic character: ") #should insert a check for charType
print("Thanks. Your string is ", stringName, " your character is ", charOne, ".")

def processString3(stringName):
    stringName = re.sub('[0-9]', charOne, stringName)
    print("after replacing is ",stringName, ".")

processString3(stringName)

#exercise 3

stringLarge = input("Please Insert a large string: ")
subString = input("Thank you. Now please insert a string which is contained in the first one you already inputted: ")

while not (subString in stringLarge):   #verify the input
    print ("Your input is incorrect.")
    stringLarge = input("Please Insert AGAIN a large string: ")
    subString = input(
        "Thank you. Now please insert a string WHICH IS CONTAINED in the first one you already inputted: ")

print ("Thank you, your input is correct")


print("Does the first string starts with the second one?: ",stringLarge.startswith(subString))
print("Does the first string ends with the second one?: ",stringLarge.endswith(subString))
print("How many times is the second string showed into the first one?:", stringLarge.count(subString))

print("Second string is in position:", stringLarge.find(subString))


#exercise 4

stringOrig = input("Please insert a new string here: ")
print("Your original string is: ", stringOrig)
print("Your string reversed is :", stringOrig[::-1])

####Dictionary Exercises

#exercise 1

currencies = {"Euro":"€", "Dollar":"$", "BitCoin":"B"}
userCurrency = input("Please insert a currency here: ")
if userCurrency in currencies.keys():
    print(currencies[userCurrency])
else: print("The currency you inputted is not in our dictionary or it doesn't exist")

#exercise 2
#amore amaro amato a amore amagno amore amato
newDict={}
userString = input("Please insert a string here: ")
usStrSplit = userString.split(" ")
#print(usStrSplit)

for word in usStrSplit:
    newDict[word] = usStrSplit.count(word)

print("Your dictionary is:", newDict)


####List Exercises
####
#exercise 1

listFix = ["due", "uomo", "2", "half", "torrijas", "tacchino", "2", "due", "uomo", "donna", "donna", "donna"]
stringA = input("Please insert a string here: ")

#for i in listFix:
if stringA in listFix:
    print("Your string is into our list")
    print("Number of times when",stringA, "is present in our list is:", listFix.count(stringA),)
else: print("Your string is not present in our list")

#exercise 2

password = input("Please insert a string here: ")
if str(password) == str(password)[::-1]:
    print("Your string",password, "is palindrome")
else: print ("Your string",password, "is not palindrome")

####Tuples Exercises
listA = [(1,2), 40, 50,90, 110, "monday",(1,3), (3,3,5), (45,87), "friday"]

count = 0
for i in listA:
    if type(i) == tuple:
        count = count + 1

print ("Our list is:", listA)
print("The number of tuples contained into out list is:", count)
