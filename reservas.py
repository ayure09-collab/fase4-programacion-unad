import logging
from datetime import datetime

from excepciones import ReservaError


# CONFIGURACIÓN LOGS
logging.basicConfig(
    filename="logs.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


class Reserva:

    def __init__(
        self,
        cliente,
        servicio,
        duracion
    ):

        try:

            # VALIDACIONES
            if cliente is None:
                raise ReservaError(
                    "Cliente inexistente"
                )

            if servicio is None:
                raise ReservaError(
                    "Servicio inexistente"
                )

            if duracion <= 0:
                raise ReservaError(
                    "La duración debe ser mayor a cero"
                )

            # ATRIBUTOS
            self.cliente = cliente
            self.servicio = servicio
            self.duracion = duracion

            self.estado = "Pendiente"

            self.fecha = datetime.now()

            logging.info(
                "Reserva creada correctamente"
            )

        except ReservaError as error:

            logging.error(error)

            print(error)

    # ===================================
    # CONFIRMAR RESERVA
    # ===================================

    def confirmar(self):

        try:

            if self.estado == "Confirmada":
                raise ReservaError(
                    "La reserva ya fue confirmada"
                )

            self.estado = "Confirmada"

            logging.info(
                "Reserva confirmada"
            )

        except ReservaError as error:

            logging.error(error)

            print(error)

        else:

            print("\nReserva confirmada exitosamente")

    # ===================================
    # CANCELAR RESERVA
    # ===================================

    def cancelar(self):

        try:

            if self.estado == "Cancelada":
                raise ReservaError(
                    "La reserva ya está cancelada"
                )

            self.estado = "Cancelada"

            logging.info(
                "Reserva cancelada"
            )

        except ReservaError as error:

            logging.error(error)

            print(error)

        else:

            print("\nReserva cancelada correctamente")

    # ===================================
    # PROCESAR RESERVA
    # ===================================

    def procesar(self):

        try:

            if self.estado == "Cancelada":
                raise ReservaError(
                    "No se puede procesar "
                    "una reserva cancelada"
                )

            total = (
                self.servicio.calcular_costo()
            )

            # FACTURA
            print("\n" + "=" * 50)
            print("           FACTURA SOFTWARE FJ")
            print("=" * 50)

            print(
                f"Cliente: "
                f"{self.cliente.get_nombre()}"
            )

            print(
                f"Servicio: "
                f"{self.servicio.descripcion()}"
            )

            print(
                f"Estado: {self.estado}"
            )

            print(
                f"Fecha: {self.fecha}"
            )

            print(
                f"Total a pagar: "
                f"${round(total, 2)}"
            )

            print("=" * 50)

            logging.info(
                "Reserva procesada"
            )

        except Exception as error:

            logging.error(error)

            print(error)

        finally:

            print(
                "\nProceso finalizado\n"
            )

    # ===================================
    # MOSTRAR RESERVA
    # ===================================

    def mostrar_reserva(self):

        print("\n" + "=" * 50)
        print("             RESERVA")
        print("=" * 50)

        print(
            f"Cliente: "
            f"{self.cliente.get_nombre()}"
        )

        print(
            f"Servicio: "
            f"{self.servicio.descripcion()}"
        )

        print(
            f"Duración: "
            f"{self.duracion}"
        )

        print(
            f"Estado: "
            f"{self.estado}"
        )

        print(
            f"Fecha: "
            f"{self.fecha}"
        )

        print("=" * 50)
