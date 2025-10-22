from abc import ABC, abstractmethod
from validadorclave.modelo.errores import (
    NoCumpleLongitudMinimaError,
    NoTieneLetraMayusculaError,
    NoTieneLetraMinusculaError,
    NoTieneNumeroError,
    NoTieneCaracterEspecialError,
    NoTienePalabraSecretaError
)

class ReglaValidacion(ABC):
    def __init__(self, longitud_esperada: int):
        self._longitud_esperada = longitud_esperada

    def _validar_longitud(self, clave: str) -> bool:
        return len(clave) > self._longitud_esperada

    def _contiene_mayuscula(self, clave: str) -> bool:
        for caracter in clave:
            if caracter.isupper():
                return True
        return False

    def _contiene_minuscula(self, clave: str) -> bool:
        for caracter in clave:
            if caracter.islower():
                return True
        return False

    def _contiene_numero(self, clave: str) -> bool:
        for caracter in clave:
            if caracter.isdigit():
                return True
        return False

    @abstractmethod
    def es_valida(self, clave: str) -> bool:
        pass


class ReglaValidacionGanimedes(ReglaValidacion):
    def __init__(self):
        super().__init__(longitud_esperada=8)

    def contiene_caracter_especial(self, clave: str) -> bool:
        caracteres_especiales = ['@', '_', '#', '$', '%']
        for caracter in clave:
            if caracter in caracteres_especiales:
                return True
        return False

    def es_valida(self, clave: str) -> bool:
        if not self._validar_longitud(clave):
            raise NoCumpleLongitudMinimaError("La clave debe tener una longitud de más de 8 caracteres")

        if not self._contiene_mayuscula(clave):
            raise NoTieneLetraMayusculaError("La clave debe contener al menos una letra mayúscula")

        if not self._contiene_minuscula(clave):
            raise NoTieneLetraMinusculaError("La clave debe contener al menos una letra minúscula")

        if not self._contiene_numero(clave):
            raise NoTieneNumeroError("La clave debe contener al menos un número")

        if not self.contiene_caracter_especial(clave):
            raise NoTieneCaracterEspecialError("La clave debe contener al menos un caracter especial (@, _, #, $, %)")

        return True


class ReglaValidacionCalisto(ReglaValidacion):
    def __init__(self):
        super().__init__(longitud_esperada=6)

    def contiene_calisto(self, clave: str) -> bool:
        palabra = "calisto"
        clave_lower = clave.lower()

        i = 0
        while i <= len(clave_lower) - len(palabra):
            if clave_lower[i:i + len(palabra)] == palabra:
                subcadena = clave[i:i + len(palabra)]

                mayusculas_count = sum(1 for c in subcadena if c.isupper())

                if mayusculas_count >= 2 and mayusculas_count < len(palabra):
                    return True
            i += 1

        return False

    def es_valida(self, clave: str) -> bool:
        if not self._validar_longitud(clave):
            raise NoCumpleLongitudMinimaError("La clave debe tener una longitud de más de 6 caracteres")

        if not self._contiene_numero(clave):
            raise NoTieneNumeroError("La clave debe contener al menos un número")

        if not self.contiene_calisto(clave):
            raise NoTienePalabraSecretaError(
                "La palabra calisto debe estar escrita con al menos dos letras en mayúscula")

        return True

class Validador:
    def __init__(self, regla: ReglaValidacion):
        self.regla = regla

    def es_valida(self, clave: str) -> bool:
        return self.regla.es_valida(clave)