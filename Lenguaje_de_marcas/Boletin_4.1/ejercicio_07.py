"""
Realiza una función inversa(cadena) que genere la inversa de una cadena.
Utilizando para ello las funcionalidades de las listas. 	
Realiza un programa que pruebe la función.
"""
# FORMA FACIL -> return cadena[::-1]
# Operador Slice [Inicio : Fin : Paso]
def invertirCadena( cadena):
    listCadena =[]
    for i in cadena:
        listCadena.append(i)
    return "".join(listCadena[::-1])


def readList(lista):
    for element in lista:
        print(element)