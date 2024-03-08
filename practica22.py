"""Realizar un programa donde se ingrese repetidamente números, determinar si los números son pares. El ingreso finaliza cuando el número es impar. Use la sentencia break para salir del ciclo. Al final mostrar el promedio de los números pares ingresados.
"""

def main():
    suma = 0
    cantidad = 0
    while True:
        numero = int(input("Ingrese números pares y calculamos el promedio (para salir ingrese un número impar)): "))
        if numero % 2 == 0:
            suma += numero
            cantidad += 1
        else:
            break
    if cantidad > 0:
        promedio = suma / cantidad
        print(f"El promedio de los números pares ingresados es {promedio}")
    else:
        print("No se ingresaron números pares")
        
main()
