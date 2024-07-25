def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Leer la cantidad de grados Celsius del usuario
celsius = float(input("Ingrese la cantidad de grados Celsius: "))
fahrenheit = celsius_a_fahrenheit(celsius)

print(f"{celsius} grados Celsius son {fahrenheit} grados Fahrenheit.")
