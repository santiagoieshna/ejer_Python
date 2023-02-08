"""
Generar un diccionario
Definir una función que tenga como parámetro N, siendo N el máximo numero 
del rango. La función debe generar un diccionario de la siguiente forma:
Generar números entre 1 y N.
Generar diccionario con la siguiente estructura: {1:1*1,2: 2*2,... n: n*n}

Ejemplo: n = 5
Resultado esperado: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
"""

def genDicPow(scope):
    dic= {}
    for i in range(1,scope+1,1):
        dic[i]=i*i
    return dic