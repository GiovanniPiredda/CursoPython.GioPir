#######################Session 2 - Exercises##########################
############
######Functions
############

#Exercise 7
'''Desarrollar una función que comprueba si la cadena
 que se pasa por parámetro es palíndroma.'''

'''print(es_palindromo('abba')) #True
print(es_palindromo('python')) #False'''


def is_palindrome(word):
    if word == word[::-1]:
        res = True
    else:
        res = False
    return res

print(is_palindrome("abba"))
###################################################################
