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

