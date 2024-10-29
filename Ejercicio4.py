# Solicitar el número de teléfono en el formato especificado
telefono = input("Introduce un número de teléfono en el formato +34-número-extensión: ")

# Dividir el número en partes usando el guion como separador
partes = telefono.split('-')

# Mostrar el número sin el prefijo y sin la extensión
numero = partes[1]
print(f"El número sin prefijo ni extensión es: {numero}")
