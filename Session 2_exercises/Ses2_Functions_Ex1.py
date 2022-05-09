#######################Session 2 - Exercises##########################
############
######Functions
############

#Exercise 1
'''Escribir una función llamada encontrar_elemento(secuencia,item)
que dada una secuencia y un ítem pasado por parámetros,
devuelve el valor true si encuentra el ítem dentro de la secuencia y false en caso contrario.'''

'''print(encontrar_elemento([100,200,300,400],200)) #True
print(encontrar_elemento([100,200,300,400],400)) #True
print(encontrar_elemento([100,200,300,400],500)) #False '''

#if both parameter should be inputted by the user:
def encontrar_elemento(serie,item):
    #print("This is the function to find an item into a serie.")
    if item in serie:
        #print("encontrar_elemento", item, "in: ", serie, "->", True)
        print(str(item), "is present on our list" )
    else:
        #print("encontrar_elemento", item, "in: ", serie, "->", False)
        print( str(item), "not found")
dayWeek =["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
#encontrar_elemento(["monday","tuesday","wednesday","thursday","friday","saturday","sunday"],"friday")
encontrar_elemento(dayWeek,"armand")

###################################################################
