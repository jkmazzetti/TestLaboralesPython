"""Dada una lista deordenada lista=[12,-25,5,14,140,84,3], programar una función
que devuelta la Lista (Ordenada Descendente), el Máximo y el Mínimo de sus elementos."""

def ordenar_maximo_minimo(una_lista):
    max=None
    min=None
    for i in range(len(una_lista)):
        if i==0:
            max=una_lista[i]
            min=una_lista[i]
        else:
            if max<una_lista[i]:
                max=una_lista[i]
            if min>una_lista[i]:
                min=una_lista[i]
    una_lista.sort()
    una_lista.reverse()
    return una_lista, max, min

lista=[12,-25,5,14,140,84,3]
print(ordenar_maximo_minimo(lista))
