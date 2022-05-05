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

