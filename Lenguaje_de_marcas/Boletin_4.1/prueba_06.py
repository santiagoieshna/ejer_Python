
from ejercicio_06 import sumarListaNumeros as plus
from ejercicio_06 import multiplicarListaNumeros as per
from ejercicio_06 import factorial as fac


l = [ 1 , 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("La lista es:",l)
print()
print("El resultado de la suma es "+
    "{} y de la multiplicación es {}"
    .format( plus(l), per(l)))

print("{} = 10! ".format(fac(10)))
