lista = [1, 2, 3, 4]

def numeros(lista):
    grande = 0
    for numero in lista:
        if numero > grande:
            grande = numero
    return grande

print(numeros(lista))