""" 
Generar grupos de 5 elementos
Definir una función que genere grupos de 5 consecutivos números dentro de una lista y retorne una lista que contenga en cada posición las subslistas de 5 elementos
Ej: [1,2,3,4,5,6,7,8,9,10]  => [ [1,2,3,4,5], [6,7,8,9,10] ]

"""
#Si entramos una lista de longitud < 5 creo que saltaria error
#Se arreglaria con try except o meteiendo un if else que englobe
#El While, pero bueno.. cumple su funcion del ejercicio y ya :)
def deCincoEnCinco(listaNumeros):
    indice=0 
    sublistas= 0 #Contara cuantas sublistas lleva
    numSublistas= int(len(listaNumeros)/5) #Max de sublistas
    cincoEnCinco = list()
    #Al final meti el if por si entra como argumento una lista len(list)<5 -.-
    if len(listaNumeros)> 5:
        while indice < len(listaNumeros) and sublistas<=numSublistas:
            if sublistas == numSublistas:
                cincoEnCinco.append(listaNumeros[indice:len(listaNumeros)])
            else:
                cincoEnCinco.append(listaNumeros[indice:indice+5])
            sublistas +=1
            indice +=5
    else:
        cincoEnCinco.append(listaNumeros[:])
    return cincoEnCinco        
# Pongo una salida (un return) y no varias (uno en if y otro en else)
# de manera que solo haya Una y asi Jose el de entorno no me quita el 
# pescuezo :')      
        