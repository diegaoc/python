#practica de funciones

def ordenar(l,orden):
    #orden ascendente
    lista = l[:]
    limite = len(lista) - 1 
    if(orden == "ASC"):
        for x in range(0, limite):
            for y in range(0, limite):
                if lista[y] > lista[y+1]:
                    aux = lista[y]
                    lista [y] = lista[y+1]
                    lista[y+1] = aux

    elif(orden == "DESC"):
        for x in range(0, limite):
            for y in range(0, limite):
                if lista[y] < lista[y+1]:
                    aux = lista[y]
                    lista [y] = lista[y+1]
                    lista[y+1] = aux
    return lista

temperatura = [30, 125, -3, 100, 25, -12, 1, 0]
lista_ordenada = ordenar(temperatura, "ASC")
lista_ordenada1 = ordenar(temperatura, "DESC")
print(temperatura)
print("ASCENDENTE",lista_ordenada)
print("DESCENDENTE",lista_ordenada1)
