e = open("C:/Users/Giovanni Piredda/Desktop/Personali/curso_python_2022-main/Sesion4_Material/Ejercicios/example1.txt","r")
text = e.read()
listA = []
#lst = text.split(" ")
countR = 1
countW = 1
countC = 0
for i in text:
    listA.append(i)
print(listA)

for i in listA:
    if i == " ":
        countW += 1
        countC += 1
    elif i == ("\n"):
        countR += 1
        countW += 1
        #countC += 1 #to uncomment if we consider "\n" as character
    else:
        countC += 1

print("The number of lines in the text is:", countR)
print("The number of words in the text is:", countW)
print("The number of characters in the text is:", countC)


#step 1: Aprire il file ed assegnarlo ad una variabile
#step2.0: Verificare i moduli di lettura dei testi (magari risparmio tutto il gioco di crear variabili etc)
#step 2: Leggere il file e creare una variabile count per le parole
#segue con caratteri e righe