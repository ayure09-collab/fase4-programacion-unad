import os


# ===================================
# LIMPIAR PANTALLA
# ===================================

def limpiar_pantalla():

    os.system("cls" if os.name == "nt" else "clear")


# ===================================
# PAUSAR SISTEMA
# ===================================

def pausar():

    input("\nPresione ENTER para continuar...")


# ===================================
# MOSTRAR MENÚ PRINCIPAL
# ===================================

def menu_principal():

    print("\n" + "=" * 50)
    print("          SOFTWARE FJ")
    print("=" * 50)

    print("1. Registrar cliente")
    print("2. Crear servicio")
    print("3. Crear reserva")
    print("4. Ver reservas")
    print("5. Confirmar reserva")
    print("6. Cancelar reserva")
    print("7. Procesar reserva")
    print("8. Ver logs")
    print("9. Salir")

    print("=" * 50)


# ===================================
# MOSTRAR LOGS
# ===================================

def mostrar_logs():

    print("\n" + "=" * 50)
    print("               LOGS")
    print("=" * 50)

    try:

        with open(
            "logs.txt",
            "r",
            encoding="utf-8"
        ) as archivo:

            contenido = archivo.read()

            if contenido.strip() == "":
                print("No existen logs registrados")

            else:
                print(contenido)

    except FileNotFoundError:

        print("No existe el archivo logs.txt")

    print("=" * 50)
