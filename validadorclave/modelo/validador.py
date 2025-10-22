from abc import ABC, abstractmethod

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
