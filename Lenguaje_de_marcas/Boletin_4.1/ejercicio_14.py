"""
Iterar sobre elementos de un diccionario
Definir programa para iterar sobre los elementos del siguiente diccionario 
Equipo = {'Rafa':'Científico de datos', 'Pedro':'Arquitecto de datos',
 'Javier':'Ingeniero de datos', 'Antonio':'Director'}
Imprimiendo la siguiente salida:
Rafa - Científico de datos
Pedro - Arquitecto de datos
Javier - Ingeniero de datos
Antonio - Director
"""
def showDic(dic):
    for c,v in dic.items():
        print(c,"-",v)