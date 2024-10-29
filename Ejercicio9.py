def obtener_fecha_nacimiento():
    fecha = input("Introduce tu fecha de nacimiento (dd/mm/aaaa): ")
    
    # Separar la fecha por '/'
    partes = fecha.split('/')
    
    # Verificar que se hayan ingresado 3 partes
    if len(partes) != 3:
        print("La fecha introducida no es válida. Asegúrate de usar el formato dd/mm/aaaa.")
        return
    
    # Asegurarse de que el día y el mes tengan dos caracteres
    dia = partes[0].zfill(2)  # Rellenar con ceros a la izquierda si es necesario
    mes = partes[1].zfill(2)  # Rellenar con ceros a la izquierda si es necesario
    anio = partes[2]
    
    # Mostrar el resultado
    print(f"Día: {dia}, Mes: {mes}, Año: {anio}")

# Llamar a la función
obtener_fecha_nacimiento()
