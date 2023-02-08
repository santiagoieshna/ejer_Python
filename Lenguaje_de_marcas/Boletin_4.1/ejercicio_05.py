"""
Función EsVolca(caracter)
Definir una función que indique si una 
caracter pasado como parámetro es una vocal o no. 
Utiliza para ello listas.
Realiza un programa que pruebe la función
"""

def isVocal(caracter):

    if len(caracter)==1:
        listVocales = ["A","a","E","e","I","i","O","o",
                        "U","u"]
        return caracter in listVocales  #Devolvera  - True si es vocal
    return False                        #           - False si no es vocal