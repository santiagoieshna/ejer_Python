"""
Eliminar duplicados en lista
Definir una función que elimine los elementos duplicados de una lista,
devolviendo otra lista sin los elementos duplicados. 
Pista (funcionalidad elemento contenido en lista)
Realiza un programa que pruebe la función.
"""
#Forma FACIL
# return list(set(duplicados))
def delDuples(duplicados):
    for duplicado in duplicados:
        while duplicados.count(duplicado) >1:
            duplicados.remove(duplicado)
    return duplicados