from excepciones import ReservaError


class Reserva:

    def __init__(self, cliente, servicio, duracion):

        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"

    def confirmar(self):

        try:

            if self.duracion <= 0:
                raise ReservaError(
                    "La duración debe ser mayor a cero"
                )

            costo = self.servicio.calcular_costo(
                self.duracion
            )

        except Exception as e:

            self.estado = "Error"

            with open("logs.txt", "a", encoding="utf-8") as log:
                log.write(
                    f"ERROR EN CONFIRMACIÓN: {str(e)}\n"
                )

            print(f"Error: {e}")

        else:

            self.estado = "Confirmada"

            print("Reserva confirmada correctamente")
            print(f"Costo total: ${costo}")

        finally:
            print("Proceso de confirmación finalizado\n")

    def cancelar(self):

        try:

            if self.estado == "Cancelada":
                raise ReservaError(
                    "La reserva ya fue cancelada"
                )

            self.estado = "Cancelada"

            with open("logs.txt", "a", encoding="utf-8") as log:
                log.write(
                    "Reserva cancelada correctamente\n"
                )

            print("Reserva cancelada")

        except Exception as e:

            with open("logs.txt", "a", encoding="utf-8") as log:
                log.write(
                    f"ERROR EN CANCELACIÓN: {str(e)}\n"
                )

            print(f"Error: {e}")

        finally:
            print("Proceso de cancelación finalizado\n")
