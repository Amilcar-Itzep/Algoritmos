# Solicitar una frase al usuario
frase = input("Introduce una frase: ")

# Solicitar una vocal al usuario
vocal = input("Introduce una vocal: ")

# Verificar que el usuario haya introducido una sola letra y que sea una vocal
if len(vocal) == 1 and vocal.lower() in "aeiou":
    # Reemplazar todas las ocurrencias de la vocal con su versión en mayúscula
    frase_modificada = frase.replace(vocal, vocal.upper()).replace(vocal.lower(), vocal.upper())
    
    # Mostrar la frase modificada
    print(f"La frase modificada es: {frase_modificada}")
else:
    print("Por favor, introduce una vocal válida.")
