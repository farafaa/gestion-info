"""
exercise5.py
Refactor del validador de contraseñas.
Reglas:
  1. Longitud mínima 8
  2. Al menos 1 dígito
  3. Al menos 1 mayúscula
  4. No puede contener espacios
"""


def is_valid_password(password: str) -> bool:
    """
    Valida una contraseña según las reglas definidas.

    Args:
        password: cadena a validar

    Returns:
        True si cumple todas las reglas, False si falla alguna.
    """
    if len(password) < 8:
        return False

    if not any(caracter.isdigit() for caracter in password):
        return False

    if not any(caracter.isupper() for caracter in password):
        return False

    if " " in password:
        return False

    return True


# ── Pruebas manuales ──────────────────────────────────────────────────────────

def test_contrasena_valida():
    assert is_valid_password("Abcdefg1") is True

def test_sin_mayuscula():
    assert is_valid_password("abcdefg1") is False

def test_sin_numero():
    assert is_valid_password("ABCDEFGH") is False

def test_muy_corta():
    assert is_valid_password("Ab1") is False

def test_con_espacio():
    assert is_valid_password("Abcdef 1") is False

def test_valida_con_simbolos():
    assert is_valid_password("Abc@1234") is True


def ejecutar_pruebas():
    pruebas = [
        test_contrasena_valida,
        test_sin_mayuscula,
        test_sin_numero,
        test_muy_corta,
        test_con_espacio,
        test_valida_con_simbolos,
    ]
    print("=== Pruebas exercise5 ===")
    for prueba in pruebas:
        try:
            prueba()
            print(f"  ✓ {prueba.__name__}")
        except AssertionError:
            print(f"  ✗ {prueba.__name__} FALLÓ")


def main():
    print("=== Ejercicio 5: Validador de contraseñas ===")
    password = input("Ingresa una contraseña: ")
    if is_valid_password(password):
        print("✓ Contraseña válida.")
    else:
        print("✗ Contraseña inválida. Debe tener mínimo 8 caracteres, "
              "1 dígito, 1 mayúscula y sin espacios.")
    print()
    ejecutar_pruebas()


if __name__ == "__main__":
    main()