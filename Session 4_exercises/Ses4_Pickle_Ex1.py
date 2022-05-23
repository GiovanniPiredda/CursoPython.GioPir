'''Guardar en un fichero en formato pickle el contenido del diccionario y
recuperarlo posteriormente.'''

import pickle

dictionary = {"Giovanni": 1, "Piredda": 2, "Sardinia": 3}

with open("file1","wb") as fp:
    pickle.dump(dictionary,fp)

with open("file1","rb") as fp:
    newDict = pickle.load(fp)

print(newDict, newDict == dictionary)