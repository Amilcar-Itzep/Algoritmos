# Solicitar el nombre del usuario
nombre = input("Introduce tu nombre: ")

# Calcular la cantidad de letras en el nombre (sin contar los espacios)
num_letras = len(nombre.replace(" ", ""))

# Imprimir el resultado
print(f"{nombre.upper()} tiene {num_letras} letras.")
