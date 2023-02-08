"""
Definir una función histograma que tome una lista de números enteros 
e imprima un histograma en la pantalla. 
Ejemplo: histograma([4, 9, 7]) debería imprimir lo siguiente:
++++
+++++++++
+++++++
Realiza un programa que pruebe la función.
"""
def histograma(lista):
    histo = list(map(lambda x: x*"+",lista))
    for i in histo:print(i)
        