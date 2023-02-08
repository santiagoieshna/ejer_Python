"""
Cadenas mayores a 2 con inicio y fin iguales
Definir una función que cuente el nº de cadenas que cumplan:
a) donde la longitud mínima de cadena debe ser 2
b) el primer y último carácter sean iguales

Ejemplo: ['abc', 'xyz', 'aba', '1221'], devuelve la función: 2
Realiza un programa que pruebe la función.
"""

def capicua(patrones):
    posicion= 0
    for patron in patrones:
        if patron[0]==patron[-1]:
            return posicion
        posicion +=1
    return None