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