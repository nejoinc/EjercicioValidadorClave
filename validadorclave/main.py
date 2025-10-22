from validadorclave.modelo.validador import (
    Validador,
    ReglaValidacionGanimedes,
    ReglaValidacionCalisto
)
from validadorclave.modelo.errores import ValidadorError


def validar_clave(clave: str, reglas: list):
    for regla in reglas:
        validador = Validador(regla)
        nombre_regla = regla.__class__.__name__
        
        try:
            if validador.es_valida(clave):
                print(f"La clave es válida para {nombre_regla}")
        except ValidadorError as e:
            print(f"Error: {nombre_regla}: {str(e)}")


if __name__ == "__main__":
    print("=== Ejemplo de Validación de Claves ===\n")

    reglas = [ReglaValidacionGanimedes(), ReglaValidacionCalisto()]

    print("Probando clave: 'abc123'")
    validar_clave("abc123", reglas)
    print()

    print("Probando clave: 'ASdDS234_-@'")
    validar_clave("ASdDS234_-@", reglas)
    print()

    print("Probando clave: 'CaLisTo95'")
    validar_clave("CaLisTo95", reglas)
    print()
