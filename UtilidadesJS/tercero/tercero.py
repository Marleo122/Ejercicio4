# Solicita dos números al usuario
numero1 = float(input("Introduce el primer número: "))
numero2 = float(input("Introduce el segundo número: "))

# Compara y ordena los números
if numero1 > numero2:
    mayor = numero1
    menor = numero2
else:
    mayor = numero2
    menor = numero1

# Muestra los números ordenados
print("Números ordenados de mayor a menor: ", mayor, menor)