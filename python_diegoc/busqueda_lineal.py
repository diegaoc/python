#practica con el módulo de random
#ejercicio de búsqueda lineal
import random

def busqueda_lineal(lista, valor_buscado):
    existe = False

    for elemento in lista: #0(n)
        if elemento == valor_buscado:
            existe = True
            break

    return existe

if __name__ == '__main__':
    tamano_de_lista = 20 #solicita por teclado el tamaño de la lista
    valor_buscado = int(input("¿Qué número quieres buscar en la lista?"))
    lista = []

    #creamos una lista y cargamos con valores aleatorios de 0 a 100
    
    for i in range(tamano_de_lista):
        lista.append(random.randint(0,100))

    existe_valor = busqueda_lineal(lista, valor_buscado)
    print(lista)

    print(f"El número {valor_buscado} {"existe" if existe_valor else "no está"} en la lista")