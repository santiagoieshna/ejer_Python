"""
Generar un diccionario de 2 listas
Definir una función que se le pase 2 listas como parámetros, y genere un diccionario resultante, donde la 1ª lista serán las claves y la 2 lista serán los varlores
Ejemplo:
keys = ['red', 'green', 'blue']
values = ['#FF0000','#008000', '#0000FF']
Resultado esperado: {'red': '#FF0000', 'green': '#008000', 'blue': '#0000FF'}

Realiza un programa que pruebe la función.
"""
def mergeListToDic(listaKey, listValue):
    dic={}
    try:
        for i in range(0,len(listaKey)):
           dic[listaKey[i]]=listValue[i] 
    except IndexError:
        print("Las longitudes de las listas son distintas")
    return dic