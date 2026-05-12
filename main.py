from entidades import Cliente
from servicios import (
    ReservaSala,
    AlquilerEquipo,
    AsesoriaEspecializada
)
from reservas import Reserva


print("===== SOFTWARE FJ =====\n")

# ==============================
# OPERACIÓN 1
# Cliente válido
# ==============================

try:

    cliente1 = Cliente(
        "Gabriel Ayure",
        "gabriel@gmail.com",
        "3001234567"
    )

    cliente1.mostrar_info()

except Exception as e:
    print(e)


# ==============================
# OPERACIÓN 2
# Cliente inválido
# ==============================

try:

    cliente2 = Cliente(
        "Carlos",
        "correo_invalido",
        "1234567"
    )

except Exception as e:

    with open("logs.txt", "a", encoding="utf-8") as log:
        log.write(f"ERROR CLIENTE: {str(e)}\n")

    print(f"Error detectado: {e}\n")


# ==============================
# OPERACIÓN 3
# Servicio válido
# ==============================

try:

    servicio1 = ReservaSala(
        "Sala VIP",
        100
    )

    print(servicio1.descripcion())

except Exception as e:
    print(e)


# ==============================
# OPERACIÓN 4
# Servicio inválido
# ==============================

try:

    servicio2 = AlquilerEquipo(
        "Laptop",
        -50
    )

except Exception as e:

    with open("logs.txt", "a", encoding="utf-8") as log:
        log.write(f"ERROR SERVICIO: {str(e)}\n")

    print(f"Error detectado: {e}\n")


# ==============================
# OPERACIÓN 5
# Reserva exitosa
# ==============================

reserva1 = Reserva(
    cliente1,
    servicio1,
    3
)

reserva1.confirmar()


# ==============================
# OPERACIÓN 6
# Reserva fallida
# ==============================

reserva2 = Reserva(
    cliente1,
    servicio1,
    -5
)

reserva2.confirmar()


# ==============================
# OPERACIÓN 7
# Asesoría especializada
# ==============================

try:

    servicio3 = AsesoriaEspecializada(
        "Asesoría Python",
        200
    )

    costo = servicio3.calcular_costo(
        5,
        0.10
    )

    print(
        f"Costo con descuento: ${costo}\n"
    )

except Exception as e:
    print(e)


# ==============================
# OPERACIÓN 8
# Cancelación válida
# ==============================

reserva1.cancelar()


# ==============================
# OPERACIÓN 9
# Cancelación repetida
# ==============================

reserva1.cancelar()


# ==============================
# OPERACIÓN 10
# Error de cálculo
# ==============================

try:

    servicio4 = ReservaSala(
        "Sala Ejecutiva",
        120
    )

    print(
        servicio4.calcular_costo(0)
    )

except Exception as e:

    with open("logs.txt", "a", encoding="utf-8") as log:
        log.write(f"ERROR CÁLCULO: {str(e)}\n")

    print(f"Error detectado: {e}\n")


print("===== FIN DEL SISTEMA =====")
