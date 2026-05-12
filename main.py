from entidades import Cliente
from servicios import (
    ReservaSala,
    AlquilerEquipo,
    AsesoriaEspecializada
)
from reservas import Reserva

from utilidades import (
    limpiar_pantalla,
    pausar,
    menu_principal,
    mostrar_logs
)


# ===================================
# LISTAS DEL SISTEMA
# ===================================

clientes = []
servicios = []
reservas = []

operaciones = 0


# ===================================
# INICIO DEL SISTEMA
# ===================================

while True:

    limpiar_pantalla()

    menu_principal()

    opcion = input(
        "\nSeleccione una opción: "
    )

    # ===================================
    # REGISTRAR CLIENTE
    # ===================================

    if opcion == "1":

        try:

            print("\n===== REGISTRO CLIENTE =====")

            nombre = input(
                "Ingrese nombre: "
            )

            correo = input(
                "Ingrese correo: "
            )

            telefono = input(
                "Ingrese teléfono: "
            )

            cliente = Cliente(
                nombre,
                correo,
                telefono
            )

            clientes.append(cliente)

            operaciones += 1

            print(
                "\nCliente registrado correctamente"
            )

            cliente.mostrar_info()

        except Exception as error:

            operaciones += 1

            print(f"\nError: {error}")

        pausar()

    # ===================================
    # CREAR SERVICIO
    # ===================================

    elif opcion == "2":

        try:

            print("\n===== CREAR SERVICIO =====")

            print("1. Reserva Sala")
            print("2. Alquiler Equipo")
            print("3. Asesoría")

            tipo = input(
                "\nSeleccione servicio: "
            )

            nombre = input(
                "Nombre del servicio: "
            )

            precio = float(
                input("Precio base: ")
            )

            # RESERVA SALA
            if tipo == "1":

                horas = int(
                    input("Horas: ")
                )

                servicio = ReservaSala(
                    nombre,
                    precio,
                    horas
                )

            # ALQUILER EQUIPO
            elif tipo == "2":

                dias = int(
                    input("Días: ")
                )

                servicio = AlquilerEquipo(
                    nombre,
                    precio,
                    dias
                )

            # ASESORÍA
            elif tipo == "3":

                horas = int(
                    input("Horas: ")
                )

                servicio = (
                    AsesoriaEspecializada(
                        nombre,
                        precio,
                        horas
                    )
                )

            else:

                raise ValueError(
                    "Opción inválida"
                )

            servicios.append(servicio)

            operaciones += 1

            print(
                "\nServicio creado correctamente"
            )

            servicio.mostrar_info()

        except Exception as error:

            operaciones += 1

            print(f"\nError: {error}")

        pausar()

    # ===================================
    # CREAR RESERVA
    # ===================================

    elif opcion == "3":

        try:

            if len(clientes) == 0:
                raise Exception(
                    "No hay clientes registrados"
                )

            if len(servicios) == 0:
                raise Exception(
                    "No hay servicios registrados"
                )

            print("\n===== CREAR RESERVA =====")

            # MOSTRAR CLIENTES
            print("\nCLIENTES:")

            for i, cliente in enumerate(clientes):

                print(
                    f"{i + 1}. "
                    f"{cliente.get_nombre()}"
                )

            cliente_index = int(
                input(
                    "\nSeleccione cliente: "
                )
            ) - 1

            # MOSTRAR SERVICIOS
            print("\nSERVICIOS:")

            for i, servicio in enumerate(servicios):

                print(
                    f"{i + 1}. "
                    f"{servicio.descripcion()}"
                )

            servicio_index = int(
                input(
                    "\nSeleccione servicio: "
                )
            ) - 1

            duracion = int(
                input(
                    "Duración real: "
                )
            )

            reserva = Reserva(
                clientes[cliente_index],
                servicios[servicio_index],
                duracion
            )

            reservas.append(reserva)

            operaciones += 1

            print(
                "\nReserva creada correctamente"
            )

            reserva.mostrar_reserva()

        except Exception as error:

            operaciones += 1

            print(f"\nError: {error}")

        pausar()

    # ===================================
    # VER RESERVAS
    # ===================================

    elif opcion == "4":

        print("\n===== RESERVAS =====")

        if len(reservas) == 0:

            print(
                "\nNo existen reservas"
            )

        else:

            for i, reserva in enumerate(reservas):

                print(
                    f"\nRESERVA #{i + 1}"
                )

                reserva.mostrar_reserva()

        pausar()

    # ===================================
    # CONFIRMAR RESERVA
    # ===================================

    elif opcion == "5":

        try:

            if len(reservas) == 0:
                raise Exception(
                    "No existen reservas"
                )

            print("\n===== CONFIRMAR =====")

            for i, reserva in enumerate(reservas):

                print(
                    f"{i + 1}. "
                    f"{reserva.cliente.get_nombre()}"
                )

            indice = int(
                input(
                    "\nSeleccione reserva: "
                )
            ) - 1

            reservas[indice].confirmar()

            operaciones += 1

        except Exception as error:

            operaciones += 1

            print(f"\nError: {error}")

        pausar()

    # ===================================
    # CANCELAR RESERVA
    # ===================================

    elif opcion == "6":

        try:

            if len(reservas) == 0:
                raise Exception(
                    "No existen reservas"
                )

            print("\n===== CANCELAR =====")

            for i, reserva in enumerate(reservas):

                print(
                    f"{i + 1}. "
                    f"{reserva.cliente.get_nombre()}"
                )

            indice = int(
                input(
                    "\nSeleccione reserva: "
                )
            ) - 1

            reservas[indice].cancelar()

            operaciones += 1

        except Exception as error:

            operaciones += 1

            print(f"\nError: {error}")

        pausar()

    # ===================================
    # PROCESAR RESERVA
    # ===================================

    elif opcion == "7":

        try:

            if len(reservas) == 0:
                raise Exception(
                    "No existen reservas"
                )

            print("\n===== PROCESAR =====")

            for i, reserva in enumerate(reservas):

                print(
                    f"{i + 1}. "
                    f"{reserva.cliente.get_nombre()}"
                )

            indice = int(
                input(
                    "\nSeleccione reserva: "
                )
            ) - 1

            reservas[indice].procesar()

            operaciones += 1

        except Exception as error:

            operaciones += 1

            print(f"\nError: {error}")

        pausar()

    # ===================================
    # VER LOGS
    # ===================================

    elif opcion == "8":

        mostrar_logs()

        pausar()

    # ===================================
    # SALIR
    # ===================================

    elif opcion == "9":

        print("\n===== FIN DEL SISTEMA =====")

        print(
            f"\nOperaciones realizadas: "
            f"{operaciones}"
        )

        break

    else:

        print("\nOpción inválida")

        pausar()
