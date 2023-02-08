"""
Generar diccionario desde String
Definir una función que se le pase una cadena, y que genere un diccionario:
Claves (keys) son las letras de la cadena
Valores: nº veces que se repite cada letra en la cadena.

Ejemplo: 'w3resource'
Restulado Esperado: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}
Realiza un programa que pruebe la función
"""

def strToDic(c):
    dic={}
    for i in range(0,len(c)):
        dic[c[i]]=i+1
    return dic