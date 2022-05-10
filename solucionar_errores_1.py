"""Dado el siguiente programa determinar cuales son los problemas que tiene, repararlo de
modo que puede ser ejecutado y explicar que es lo que hace:

lista_a=[1,1,1,2,5,4,8,8,7,5,0,-1]
lista_b=[7,5,0,-1]
lista_c=list()

for i in range(lista_a):
    t=lista_a[i]+lista_b[i]
    lista_c.append(t)

print (lista_c)

En este ejercicio hay dos errores:
El primero es que el parametro que recibe range debe ser un int
ser repara así: range(len(lista_a))
El segundo error es que el largo de las dos listas que son iteradas, son de distanto tamaño
por lo que va a arrojar error fuera de indicie.py
Explicacion del programa:
Toma dos listas, suma sus elementos y los agrega a una tercera lista.

"""

lista_a=[1,1,1,2]
lista_b=[7,5,0,-1]
lista_c=list()
for i in range(len(lista_a)):
    t=lista_a[i]+lista_b[i]
    lista_c.append(t)
print (lista_c)