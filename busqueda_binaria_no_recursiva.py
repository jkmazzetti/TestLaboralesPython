"""Dada la siguiente lista ordenada, lista=[1,2,3,4,5,6,7,8,9,10], realizar las busqueda binarias de:

elemento=0 devuelve -1
elemento=1 devuelve 0
elemento=7 devuelve 6
elemento=10 devuelve 9

inicio=0
fin=len(lista)
medio=(fin+inicio)/2.__round()

Busqueda binaria no recursiva.
"""

def busqueda_binaria(lista,elemento):
    inicio=0
    fin=len(lista)-1
    posicion=((inicio+fin)/2).__round__()
    while (inicio!=fin and lista[posicion]!=elemento):  
        posicion=((inicio+fin)/2)
        if(posicion==0.5):
            posicion=((inicio+fin)/2).__floor__()
        else:
            posicion=((inicio+fin)/2).__ceil__()
        if elemento>lista[posicion]:
            inicio=posicion
        if elemento<lista[posicion]:
            fin=posicion
        if inicio==fin and lista[posicion]!=elemento:
            posicion=-1        
    return posicion

lista=[1,2,3,4,5,6,7,8,9,10]
print(0,":",busqueda_binaria(lista,0))
print(1,":",busqueda_binaria(lista,1))
print(7,":",busqueda_binaria(lista,7))
print(10,":",busqueda_binaria(lista,10))


