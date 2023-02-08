"""
Filtrar diccionarios sobre valor
Definir una función que filter un diccionario sobre el valor de sus elementos.
Debe devolver el mismo diccionario, eliminado las claves de los valores que 
no cumplen el criterio.
Ejemplo: Mayor que 174 cm.
Ejemplo:  {'Alonso': 175, 'Juan': 180, 'Andres': 165, 'Ramon': 190}
Restulado Esperado: {'Alonso': 175, 'Juan': 180, Ramon': 190}

Realiza un programa que pruebe la función.
"""
def ej19(dic, criterio):
    return dict(filter(lambda d: d[1]>criterio,dic.items()))