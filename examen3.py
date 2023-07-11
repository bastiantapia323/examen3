import datetime

# Definir los precios de los departamentos
precios_departamentos = {
    'A': 3800,
    'B': 3000,
    'C': 2800,
    'D': 3500
}

# Crear listas para almacenar los datos
departamentos_disponibles = []
departamentos_vendidos = []
compradores = []

# Generar lista de departamentos disponibles
for piso in range(1, 21):
    for tipo in ['A', 'B', 'C', 'D']:
        departamento = tipo + str(piso)
        departamentos_disponibles.append(departamento)

# Función para comprar departamento
def comprar_departamento():
    print("Departamentos disponibles:")
    for departamento in departamentos_disponibles:
        print(departamento, end=' ')

    print("\nIngrese el piso y el tipo de departamento que desea comprar:")
    piso = int(input("Piso: "))
    tipo = input("Tipo (A, B, C o D): ").upper()

    departamento = tipo + str(piso)
    if departamento in departamentos_disponibles:
        departamentos_disponibles.remove(departamento)
        departamentos_vendidos.append(departamento)

        run = input("Ingrese el RUN del comprador (sin guiones ni puntos): ")
        compradores.append(run)

        print("Departamento", departamento, "comprado correctamente.")
    else:
        print("El departamento no está disponible.")

# Función para mostrar departamentos disponibles
def mostrar_departamentos_disponibles():
    print("Departamentos disponibles:")
    for departamento in departamentos_disponibles:
        print(departamento, end=' ')
    print()

# Función para mostrar listado de compradores
def mostrar_listado_compradores():
    print("Listado de compradores:")
    compradores_ordenados = sorted(compradores)
    for comprador in compradores_ordenados:
        print(comprador)

# Función para mostrar ventas totales
def mostrar_ventas_totales():
    total_ventas = sum([precios_departamentos.get(departamento[0]) for departamento in departamentos_vendidos])
    print("Ventas totales:", total_ventas, "UF")

# Función para salir del programa
def salir():
    print("Saliendo del sistema.")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    fecha_actual = datetime.date.today().strftime("%d/%m/%Y")
    print("¡Hasta luego,", nombre, apellido + "!")
    print("Fecha actual:", fecha_actual)

# Función para mostrar el menú y procesar la opción seleccionada
def mostrar_menu():
    while True:
        print("\n----- MENU -----")
        print("1. Comprar departamento")
        print("2. Mostrar departamentos disponibles")
        print("3. Ver listado de compradores")
        print("4. Mostrar ganancias totales")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            comprar_departamento()
        elif opcion == '2':
            mostrar_departamentos_disponibles()
        elif opcion == '3':
            mostrar_listado_compradores()
        elif opcion == '4':
            mostrar_ventas_totales()
        elif opcion == '5':
            salir()
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")


# Ejecutar el programa
mostrar_menu()
