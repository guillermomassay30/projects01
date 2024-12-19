class Atraccion:
    def __init__(self, nombre, capacidad_maxima, tiempo_espera):
        self.nombre = nombre
        self.capacidad_maxima = capacidad_maxima
        self.tiempo_espera = tiempo_espera
        self.visitantes_en_espera = []

class Visitante:
    def __init__(self, nombre, edad, altura):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura
        self.atracciones_visitadas = []

    def __str__(self):
        return f"Visitante: {self.nombre}, Edad: {self.edad}, Altura: {self.altura} cm, Atracciones Visitadas: {', '.join(atraccion.nombre for atraccion in self.atracciones_visitadas)}"

class Reserva:
    def __init__(self):
        self.atracciones = []
        self.visitantes = []
        self.reservas = []

    def agregar_atraccion(self, atraccion):
        self.atracciones.append(atraccion)

    def agregar_visitante(self, visitante):
        self.visitantes.append(visitante)

    def realizar_reserva(self, visitante, atraccion):
        if (visitante, atraccion) not in self.reservas:
            self.reservas.append((visitante, atraccion))
            visitante.atracciones_visitadas.append(atraccion)  # Agregar la atracción a las visitadas por el visitante
            print(f"Reserva realizada para {visitante.nombre} en {atraccion.nombre}.")
        else:
            print(f"{visitante.nombre} ya ha realizado una reserva para {atraccion.nombre}.")

    def actualizar_estado(self):
        for atraccion in self.atracciones:
            if atraccion.visitantes_en_espera:
                visitante = atraccion.visitantes_en_espera.pop(0)
                print(f"{visitante.nombre} disfrutó de {atraccion.nombre}.")
                visitante.atracciones_visitadas.append(atraccion)

    def modificar_atraccion(self, nombre_atraccion):
        for atraccion in self.atracciones:
            if atraccion.nombre == nombre_atraccion:
                nueva_capacidad = int(input(f"Ingrese la nueva capacidad máxima para {atraccion.nombre}: "))
                atraccion.capacidad_maxima = nueva_capacidad
                print(f"La capacidad de {atraccion.nombre} ha sido modificada a {nueva_capacidad}.")
                return
        print("Atracción no encontrada.")

    def modificar_visitante(self, nombre_visitante):
        for visitante in self.visitantes:
            if visitante.nombre == nombre_visitante:
                nueva_edad = int(input(f"Ingrese la nueva edad para {visitante.nombre}: "))
                nueva_altura = int(input(f"Ingrese la nueva altura para {visitante.nombre} en cm: "))
                visitante.edad = nueva_edad
                visitante.altura = nueva_altura
                print(f"La información de {visitante.nombre} ha sido modificada.")
                return
        print("Visitante no encontrado.")

    def consultar_atracciones(self):
        print("\nAtracciones:")
        for atraccion in self.atracciones:
            print(atraccion)

    def consultar_visitantes(self):
        print("\nVisitantes:")
        for visitante in self.visitantes:
            print(visitante)

    def consultar_reservas(self):
        print("\nReservas:")
        if not self.reservas:
            print("No hay reservas en la base de datos.")
        else:
            for reserva in self.reservas:
                visitante = reserva[0]
                atraccion = reserva[1]
                atracciones_visitadas = ', '.join(atraccion.nombre for atraccion in visitante.atracciones_visitadas)
                print(f"{visitante.nombre} - Atracciones Visitadas: {atracciones_visitadas}")

# Solicitamos al usuario ingresar datos y ejecutar con el programa mostrado
reserva = Reserva()

while True:
    print("\nSeleccione una Opción (0-9): ")
    print("1. Agregar Atracción")
    print("2. Agregar Visitante")
    print("3. Realizar Reserva")
    print("4. Modificar Atracción")
    print("5. Modificar Visitante")
    print("6. Actualizar Estado")
    print("7. Consultar Atracciones")
    print("8. Consultar Visitantes")
    print("9. Consultar Reservas")
    print("0. Salir")

    resultados = []
    opcion = input()
    if opcion == "0":
        break
    elif opcion == "1":
        # Agregar Atracción
        while True:
            nombre_atraccion = input("Ingrese el nombre de la atracción: ")
            if nombre_atraccion.isalpha():
                break
            else:
                print("Por favor, ingrese solo texto.")

        while True:
            capacidad_maxima_str = input("Ingrese la capacidad máxima de la atracción (solo números): ")
            if capacidad_maxima_str.isdigit():
                capacidad_maxima = float(capacidad_maxima_str)
                break
            else:
                print("Por favor, ingrese solo números.")

        tiempo_espera_str = input("Ingrese el tiempo de espera de la atracción en minutos (solo números): ")

        while True:
            if tiempo_espera_str.isdigit():
                tiempo_espera = int(tiempo_espera_str)
                break
            else:
                print("Por favor, ingresa solo números.")
                tiempo_espera_str = input("Ingrese el tiempo de espera de la atracción en minutos (solo números): ")

        nueva_atraccion = Atraccion(nombre_atraccion, capacidad_maxima, tiempo_espera)
        reserva.agregar_atraccion(nueva_atraccion)
        resultados.append(f"Atracción '{nueva_atraccion.nombre}' agregada correctamente.")
    elif opcion == "2":
        # Agregarmos al  visitante
        nombre_visitante = input("Ingrese el nombre del visitante: ")
        while True:
            if nombre_visitante.isalpha():
                break
            else:
                print("Por favor, ingrese solo texto.")

            nombre_atraccion = input("Ingrese el nombre de la atracción: ")
            while True:
                if nombre_atraccion.isalpha():
                    break
                else:
                    print("Por favor, ingrese solo texto.")
        edad_visitante_str = input("Ingrese la edad del visitante (solo números): ")
        while True:
            if edad_visitante_str.isdigit():
                edad_visitante = int(edad_visitante_str)
                break
            else:
                print("Por favor, ingresa solo números.")
                edad_visitante_str = input("Ingrese la edad del visitante (solo números): ")

        altura_visitante_str = input("Ingrese la altura del visitante en cm (solo números): ")
        while True:
            if altura_visitante_str.isdigit():
                altura_visitante = int(altura_visitante_str)
                break
            else:
                print("Por favor, ingresa solo números.")
                altura_visitante_str = input("Ingrese la altura del visitante en cm (solo números): ")
        nuevo_visitante = Visitante(nombre_visitante, edad_visitante, altura_visitante)
        reserva.agregar_visitante(nuevo_visitante)
        resultados.append(f"Visitante '{nuevo_visitante.nombre}' agregado correctamente.")
    elif opcion == "3":
        # Se realiza la reservacion
        nombre_visitante_res = input("Ingrese el nombre del visitante: ")
        while True:
            if nombre_visitante_res.isalpha():
                break
            else:
                print("Por favor, ingrese solo texto.")

        nombre_atraccion = input("Ingrese el nombre de la atracción: ")
        while True:
            if nombre_atraccion.isalpha():
                break
            else:
                print("Por favor, ingrese solo texto.")
        visitante = next((v for v in reserva.visitantes if v.nombre == nombre_visitante_res), None)
        atraccion = next((a for a in reserva.atracciones if a.nombre == nombre_atraccion), None)

        if visitante is not None and atraccion is not None:
            reserva.realizar_reserva(visitante,atraccion)
            resultados.append(f"Reserva realizada para '{visitante.nombre}' en '{atraccion.nombre}'.")
        else:
            resultados.append("Visitante o atracción no encontrados.")
    elif opcion == "4":
        # Modificacion de la atracción
        nombre_atraccion = input("Ingrese el nombre de la atracción a modificar: ")
        reserva.modificar_atraccion(nombre_atraccion)
    elif opcion == "5":
        # Modificacion del visitante
        nombre_visitante = input("Ingrese el nombre del visitante a modificar: ")
        reserva.modificar_visitante(nombre_visitante)
    elif opcion == "6":
        # Actualizacion del Estado
        reserva.actualizar_estado()
        resultados.append("Estado actualizado.")
    elif opcion == "7":
        # Consultacion de las atracciones
        if not reserva.atracciones:
            resultados.append("No hay atracciones en la base de datos.")
        else:
            resultados.extend([str(atraccion) for atraccion in reserva.atracciones])
    elif opcion == "8":
        # Consultacion de los visitantes
        if not reserva.visitantes:
            resultados.append("No hay visitantes en la base de datos.")
        else:
            resultados.extend([str(visitante) for visitante in reserva.visitantes])
    elif opcion == "9":
        # Consultacion de las reservas
        if not reserva.visitantes:
            resultados.append("No hay reservas en la base de datos.")
        else:
            resultados.extend([f"{visitante.nombre} - Atracción Reservada: {[atraccion.nombre for atraccion in visitante.atracciones_visitadas]}"for visitante in reserva.visitantes])
    else:
        resultados.append("Opción no válida. Ingrese un numero (0-9) por favor.")
    # Imprimir los resultados de las opciones
    for resultado in resultados:
        print(resultado)