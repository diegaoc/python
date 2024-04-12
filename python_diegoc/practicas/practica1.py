notas = []

for x in range(3):
    nota = int(input(f"Ingrese la nota {x}:"))
    notas.append(nota)

suma = 0
for x in range(3):
    suma = suma + notas[x]

promedio = suma / 3

print(f"Notas: {notas}")
print(f"Promedio: {promedio}")

if promedio > 1.7:
    print("Aprobado")
else:
    print("Reprobado")
