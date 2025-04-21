



def procesar_lista(lista):
    pares = []
    for numero in lista:
        if numero % 2 == 0:
            pares.append(numero)
    return pares

print (procesar_lista(range(100)))
