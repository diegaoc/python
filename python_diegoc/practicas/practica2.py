usuarios_autenticados = {"admin":"12345","diego":"2006"}

usuario = input("Ingrese su usuario:")
password = input("Ingrese su contraseña:")

if(usuario in usuarios_autenticados):
    intentos = 1
    while (intentos <= 3):
        if(usuarios_autenticados[usuario] == password):
            print("Acceso Correcto")
            break
        else:
            if(intentos >= 3):
                print("Su cuenta ha sido bloqueada")
                intentos = intentos + 1
            else:
                intentos = intentos + 1
                print(f"Error de contraseña. Intentos {intentos} de 3!")
                password = input("Ingrese contraseña:")
else:
    print("El usuario no existe")

