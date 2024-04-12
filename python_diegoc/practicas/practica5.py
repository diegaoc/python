import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "bd_traductor_python"
    )

cursor = mydb.cursor()
palabra = ""
while palabra != 0:
    palabra = input("Ingrese la palabra a traducir: ")
    sentencia = f"Select espanol, ingles from traductor where espanol like '{palabra}'"
    cursor.execute(sentencia)
    resultado = cursor.fetchall()

    if len(resultado) > 0:
        for x in resultado:
            print(f"(esp) {x[0]} : (eng) {x[1]}")
    elif palabra != 0:
        print("Palabra no existe. Desea agregarlo al diccionario?")
        resp = input("S/N:")
        if(resp in ["S","s"]):
            traduccion = input(f"Ingrese la traduccion de {palabra}:")
            sentencia = f"insert into traductor values (default,'{palabra}', '{traduccion}');"
            cursor.execute(sentencia)
            mydb.commit()
            print("Se ha agregado al diccionario")
        