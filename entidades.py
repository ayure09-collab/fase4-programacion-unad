from abc import ABC, abstractmethod
import logging

from excepciones import ClienteError


# CONFIGURACIÓN DE LOGS
logging.basicConfig(
    filename="logs.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


# CLASE ABSTRACTA
class Entidad(ABC):

    @abstractmethod
    def mostrar_info(self):
        pass


# CLASE CLIENTE
class Cliente(Entidad):

    def __init__(self, nombre, correo, telefono):

        try:

            # VALIDACIÓN NOMBRE
            if not nombre.strip():
                raise ValueError(
                    "El nombre no puede estar vacío"
                )

            # VALIDACIÓN CORREO
            if "@" not in correo:
                raise ValueError(
                    "Correo inválido"
                )

            # VALIDACIÓN TELÉFONO
            if not telefono.isdigit():
                raise ValueError(
                    "El teléfono debe contener solo números"
                )

            if len(telefono) != 10:
                raise ValueError(
                    "El teléfono debe tener 10 dígitos"
                )

            # ENCAPSULACIÓN
            self.__nombre = nombre
            self.__correo = correo
            self.__telefono = telefono

            logging.info(
                f"Cliente registrado: {nombre}"
            )

        except ValueError as error:

            logging.error(error)

            raise ClienteError(
                "No se pudo registrar el cliente"
            ) from error

    # GETTERS
    def get_nombre(self):
        return self.__nombre

    def get_correo(self):
        return self.__correo

    def get_telefono(self):
        return self.__telefono

    # SETTERS
    def set_nombre(self, nuevo_nombre):

        try:

            if not nuevo_nombre.strip():
                raise ClienteError(
                    "Nombre inválido"
                )

            self.__nombre = nuevo_nombre

            logging.info(
                "Nombre actualizado"
            )

        except ClienteError as error:

            logging.error(error)

            print(error)

    def set_correo(self, nuevo_correo):

        try:

            if "@" not in nuevo_correo:
                raise ClienteError(
                    "Correo inválido"
                )

            self.__correo = nuevo_correo

            logging.info(
                "Correo actualizado"
            )

        except ClienteError as error:

            logging.error(error)

            print(error)

    def set_telefono(self, nuevo_telefono):

        try:

            if not nuevo_telefono.isdigit():
                raise ClienteError(
                    "El teléfono debe tener números"
                )

            if len(nuevo_telefono) != 10:
                raise ClienteError(
                    "El teléfono debe tener 10 dígitos"
                )

            self.__telefono = nuevo_telefono

            logging.info(
                "Teléfono actualizado"
            )

        except ClienteError as error:

            logging.error(error)

            print(error)

    # MOSTRAR INFORMACIÓN
    def mostrar_info(self):

        print("\n" + "=" * 40)
        print("        CLIENTE REGISTRADO")
        print("=" * 40)

        print(f"Nombre: {self.__nombre}")
        print(f"Correo: {self.__correo}")
        print(f"Teléfono: {self.__telefono}")

        print("=" * 40)
