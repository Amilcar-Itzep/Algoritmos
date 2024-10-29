def mostrar_productos():
    # Pedir al usuario que introduzca los productos
    productos_input = input("Introduce los productos de la cesta de la compra, separados por comas: ")
    
    # Separar los productos por comas
    productos = productos_input.split(',')
    
    # Mostrar cada producto en una línea distinta
    print("Los productos en la cesta son:")
    for producto in productos:
        # Eliminar espacios en blanco al inicio y al final de cada producto
        print(producto.strip())

# Llamar a la función
mostrar_productos()
