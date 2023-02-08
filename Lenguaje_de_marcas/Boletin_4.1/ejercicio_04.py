"""Función Longitud(cadena)
Definir una función longitud que se le pase una cadena como argumento y devuelva el número de elementos o longitud de la cadena. No usar la función intrínseca de python para el cálculo.
Realiza un programa que pruebe la función
"""

# no se a que te refieres con la funcion intrinseca
# Si te refieres a len() o no...

def longitud(cadena: str): # hay alguna manera de forzar que solo sea string?
    cond=True
    cont=0
    if type(cadena) is str:
        while(cond==True):
            try:
                cadena[cont]
                cont +=1
            except:
                cond=False
        return cont 
    else:
        return "No es una cadena"
