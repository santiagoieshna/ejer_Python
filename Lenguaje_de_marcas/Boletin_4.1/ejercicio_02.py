""" Función Max() con 3 valores
Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos.
Realiza un programa que pruebe la función.
"""
def max(a , b, c):
    if a > b and a>c:
        numMax = a 
    elif b>a and b>c:
        numMax = b
    else:
        numMax = c
    return numMax