"""
Definir 2 funciones:
    - Función sumarListaNumeros(listaNumeros) => suma total
    - Función multiplicarListaNumeros(listaNumeros) => multiplicación total
	
Realiza un programa que pruebe la función, mostrando el resultado de
la suma y la multiplicación utilizando interpolación de la siguiente forma:
“El resultado de la suma es X y de la multiplicación es Y”.
"""

def sumarListaNumeros(listaNumeros): 
    sum=0
    for i in listaNumeros:
        sum +=i
    return sum

def multiplicarListaNumeros(listaNumeros):
    pro=1
    for i in listaNumeros:
        pro *=i
    return pro

#Funcion extra
#@param int numero
#@return el factorial de numero
def factorial(numero:int):
    fac=1
    for i in range(numero, 0, -1):
        fac *= i
    return fac