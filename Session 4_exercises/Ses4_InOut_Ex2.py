"Implementar un método llamado buscar que dada una palabra y el contenido"
"del fichero, busque la palabra dentro del contenido de un fichero."

def findWord():
    e = open("C:/Users/Giovanni Piredda/Desktop/Personali/curso_python_2022-main/Sesion4_Material/Ejercicios/example1.txt",
        "r")
    # path = str("Please input the path of the file where you want to search: ") #if we want to input
    # e = open(path)
    count = 0
    check = 0
    word = str(input("Please insert the word you want to find here: "))
    for line in e:
        if word in line:
            count += 1
    if count != 0:
        if count > 1:
            print('The word', str(word), "was found", str(count), "times in the file.")
        else:
            print("The word", str(word), "was found once in the file")
        check = True
    else:
        print('Word', str(word),'not found.')
        check = False
    return check

findWord()