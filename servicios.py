from abc import ABC, abstractmethod
import logging

from entidades import Entidad
from excepciones import ServicioError


# CONFIGURACIÓN LOGS
logging.basicConfig(
    filename="logs.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


# CLASE ABSTRACTA SERVICIO
class Servicio(Entidad):

    def __init__(self, nombre, precio_base):

        try:

            if not nombre.strip():
                raise ValueError(
                    "El nombre del servicio está vacío"
                )

            if precio_base <= 0:
                raise ValueError(
                    "El precio debe ser mayor a cero"
                )

            self._nombre = nombre
            self._precio_base = precio_base

            logging.info(
                f"Servicio creado: {nombre}"
            )

        except ValueError as error:

            logging.error(error)

            raise ServicioError(
                "No se pudo crear el servicio"
            ) from error

    # MÉTODOS ABSTRACTOS
    @abstractmethod
    def calcular_costo(self):
        pass

    @abstractmethod
    def descripcion(self):
        pass

    # MOSTRAR INFORMACIÓN
    def mostrar_info(self):

        print("\n" + "=" * 40)
        print("       INFORMACIÓN SERVICIO")
        print("=" * 40)

        print(f"Servicio: {self._nombre}")
        print(f"Precio Base: ${self._precio_base}")

        print("=" * 40)


# ===================================
# RESERVA DE SALA
# ===================================

class ReservaSala(Servicio):

    def __init__(self, nombre, precio_base, horas):

        super().__init__(
            nombre,
            precio_base
        )

        try:

            if horas <= 0:
                raise ValueError(
                    "Las horas deben ser mayores a cero"
                )

            self.horas = horas

            logging.info(
                "Reserva de sala creada"
            )

        except ValueError as error:

            logging.error(error)

            raise ServicioError(
                "Error en reserva de sala"
            ) from error

    # POLIMORFISMO
    def calcular_costo(
        self,
        impuesto=0.19,
        descuento=0
    ):

        subtotal = (
            self._precio_base * self.horas
        )

        valor_impuesto = subtotal * impuesto

        valor_descuento = subtotal * descuento

        total = (
            subtotal
            + valor_impuesto
            - valor_descuento
        )

        return total

    def descripcion(self):

        return (
            f"Reserva de sala por "
            f"{self.horas} horas"
        )

    def mostrar_info(self):

        print("\n" + "=" * 40)
        print("        RESERVA DE SALA")
        print("=" * 40)

        print(f"Sala: {self._nombre}")
        print(f"Horas: {self.horas}")
        print(f"Precio Base: ${self._precio_base}")

        print("=" * 40)


# ===================================
# ALQUILER DE EQUIPOS
# ===================================

class AlquilerEquipo(Servicio):

    def __init__(self, nombre, precio_base, dias):

        super().__init__(
            nombre,
            precio_base
        )

        try:

            if dias <= 0:
                raise ValueError(
                    "Los días deben ser mayores a cero"
                )

            self.dias = dias

            logging.info(
                "Alquiler de equipo creado"
            )

        except ValueError as error:

            logging.error(error)

            raise ServicioError(
                "Error en alquiler de equipo"
            ) from error

    def calcular_costo(
        self,
        impuesto=0.15,
        descuento=0.05
    ):

        subtotal = (
            self._precio_base * self.dias
        )

        valor_impuesto = subtotal * impuesto

        valor_descuento = subtotal * descuento

        total = (
            subtotal
            + valor_impuesto
            - valor_descuento
        )

        return total

    def descripcion(self):

        return (
            f"Alquiler de equipo por "
            f"{self.dias} días"
        )

    def mostrar_info(self):

        print("\n" + "=" * 40)
        print("       ALQUILER DE EQUIPO")
        print("=" * 40)

        print(f"Equipo: {self._nombre}")
        print(f"Días: {self.dias}")
        print(f"Precio Base: ${self._precio_base}")

        print("=" * 40)


# ===================================
# ASESORÍA ESPECIALIZADA
# ===================================

class AsesoriaEspecializada(Servicio):

    def __init__(self, nombre, precio_base, horas):

        super().__init__(
            nombre,
            precio_base
        )

        try:

            if horas <= 0:
                raise ValueError(
                    "Las horas deben ser mayores a cero"
                )

            self.horas = horas

            logging.info(
                "Asesoría creada"
            )

        except ValueError as error:

            logging.error(error)

            raise ServicioError(
                "Error en asesoría"
            ) from error

    def calcular_costo(
        self,
        impuesto=0.10,
        descuento=0.20
    ):

        subtotal = (
            self._precio_base * self.horas
        )

        valor_impuesto = subtotal * impuesto

        valor_descuento = subtotal * descuento

        total = (
            subtotal
            + valor_impuesto
            - valor_descuento
        )

        return total

    def descripcion(self):

        return (
            f"Asesoría especializada por "
            f"{self.horas} horas"
        )

    def mostrar_info(self):

        print("\n" + "=" * 40)
        print("     ASESORÍA ESPECIALIZADA")
        print("=" * 40)

        print(f"Asesoría: {self._nombre}")
        print(f"Horas: {self.horas}")
        print(f"Precio Base: ${self._precio_base}")

        print("=" * 40)
