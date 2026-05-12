from abc import ABC, abstractmethod
from excepciones import ServicioNoDisponible


class Servicio(ABC):
    """Clase abstracta para servicios"""

    def __init__(self, nombre, precio_base):

        self.nombre = nombre
        self.precio_base = precio_base

        if precio_base <= 0:
            raise ServicioNoDisponible(
                "El precio debe ser mayor a cero"
            )

    @abstractmethod
    def calcular_costo(self, tiempo):
        pass

    @abstractmethod
    def descripcion(self):
        pass


class ReservaSala(Servicio):

    def calcular_costo(self, horas=1):

        if horas <= 0:
            raise ValueError(
                "Las horas deben ser mayores a cero"
            )

        return self.precio_base * horas

    def descripcion(self):
        return "Reserva de salas empresariales"


class AlquilerEquipo(Servicio):

    def calcular_costo(self, dias=1):

        if dias <= 0:
            raise ValueError(
                "Los días deben ser mayores a cero"
            )

        return self.precio_base * dias

    def descripcion(self):
        return "Alquiler de equipos tecnológicos"


class AsesoriaEspecializada(Servicio):

    def calcular_costo(self, horas=1, descuento=0):

        if horas <= 0:
            raise ValueError(
                "Las horas deben ser mayores a cero"
            )

        total = self.precio_base * horas

        # Método con descuento opcional
        if descuento > 0:
            total -= total * descuento

        return total

    def descripcion(self):
        return "Asesorías especializadas"
