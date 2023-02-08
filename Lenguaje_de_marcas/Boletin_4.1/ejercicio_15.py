"""
Definir una función para concatenar 2 diccionarios pasados como parámetros.
Imagen ilustrativa:
https://www.w3resource.com/w3r_images/python-data-type-dictionary-image-exercise-3.png

Ejemplo diccionario: dic1={1:10, 2:20} dic2={3:30, 4:40}
Experado resultado: {1: 10, 2: 20, 3: 30, 4: 40}
Realiza un programa que pruebe la función.
"""
def concatDic(dic1,dic2):
    return dic1 | dic2