# Solicitar el precio del producto
precio = input("Introduce el precio del producto en euros (con dos decimales): ")

# Separar la parte de los euros y los céntimos
euros, centimos = precio.split('.')

# Mostrar el resultado
print(f"El precio tiene {euros} euros y {centimos} céntimos.")
