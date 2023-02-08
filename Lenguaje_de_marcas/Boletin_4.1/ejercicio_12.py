"""
Escribir una función que genera e imprime una lista de los primeros y últimos
5 elementos donde los valores son elevados al cuadrado. Generar los números 
entre 1 y 30 ambos incluidos. Imagen ejemplo

Realiza un programa que pruebe la función que genere los números entre 1 y 30
 ambos inclusive, e imprima por pantalla la lista resultante.
"""
#No se si se queria usando el metodo .append() con un bucle
def genIntervalo(inicio, fin):
    return list(range(inicio, fin+1, 1))

def noseQueNombrePonerXD(intervalo):
    for e in range(1, 6, 1):
        print(intervalo[e]**2)
    for i in range(-1, -6, -1):
        print(intervalo[i]**2)


