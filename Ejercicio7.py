# Solicitar el correo electrónico al usuario
correo = input("Introduce tu correo electrónico: ")

# Separar la parte del nombre del correo antes de la arroba
nombre = correo.split('@')[0]

# Crear el nuevo correo con el dominio ceu.es
nuevo_correo = nombre + "@ceu.es"

# Mostrar el nuevo correo
print(f"Tu nuevo correo es: {nuevo_correo}")
