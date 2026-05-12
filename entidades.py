from abc import ABC, abstractmethod
from excepciones import ClienteInvalido


class Entidad(ABC):
    """Clase abstracta principal"""

    @abstractmethod
    def mostrar_info(self):
        pass


class Cliente(Entidad):

    def __init__(self, nombre, correo, telefono):

        # Encapsulación
        self.__nombre = nombre
        self.__correo = correo
        self.__telefono = telefono

        # Validaciones
        if len(nombre.strip()) == 0:
            raise ClienteInvalido(
                "El nombre no puede estar vacío"
            )

        if "@" not in correo:
            raise ClienteInvalido(
                "Correo inválido"
            )

        if len(telefono) < 7:
            raise ClienteInvalido(
                "Teléfono inválido"
            )

    # Getters
    def get_nombre(self):
        return self.__nombre

    def get_correo(self):
        return self.__correo

    def get_telefono(self):
        return self.__telefono

    # Setters
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_correo(self, correo):
        if "@" not in correo:
            raise ClienteInvalido(
                "Correo inválido"
            )

        self.__correo = correo

    def mostrar_info(self):
        print("===== CLIENTE =====")
        print(f"Nombre: {self.__nombre}")
        print(f"Correo: {self.__correo}")
        print(f"Teléfono: {self.__telefono}")
