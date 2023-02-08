"""Función Max() con N valores
Definir una función maximo_lista(), que tome una lista de valores como argumente y devuelva el mayor de ellos.
Realiza un programa que pruebe la función
"""

def max(*argv):
    x= argv[0]-1
    for arg in argv:
        if x<arg:
            x=arg    
    return x
