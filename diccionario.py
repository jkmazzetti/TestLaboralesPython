"""Dada la lista=[1,1,1,2,5,4,8,8,7,5,0,-1] contabilizar cuantas veces se repite cada elemento."""

def contador_de_elementos(una_lista):
    mi_dict=dict()
    for elemento in una_lista:
        if elemento not in mi_dict:
            mi_dict.update({elemento:1})
        else:
            mi_dict.update({elemento:mi_dict.get(elemento)+1})
    return mi_dict
    
lista=[1,1,1,2,5,4,8,8,7,5,0,-1]
print(contador_de_elementos(lista))