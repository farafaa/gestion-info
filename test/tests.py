"""
test/tests.py
Módulo 6: Pruebas unitarias con pytest (mínimo 4 funciones).
"""

import sys
import os

# Agrega src/ al path para importar los módulos
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from validate import validate_user, is_valid_email, is_not_empty


def test_usuario_valido():
    """Un usuario con todos los campos correctos no debe tener errores."""
    user = {
        "id": "abc12345",
        "name": "Ana Torres",
        "email": "ana@correo.com",
        "age": 25,
        "role": "admin",
    }
    errors = validate_user(user)
    assert errors == [], f"No deberia haber errores, pero se encontraron: {errors}"


def test_nombre_vacio():
    """Un usuario sin nombre debe retornar error."""
    user = {
        "id": "abc12345",
        "name": "",
        "email": "ana@correo.com",
        "age": 25,
        "role": "usuario",
    }
    errors = validate_user(user)
    assert any("nombre" in e.lower() for e in errors), "Debe detectar nombre vacio."


def test_email_invalido():
    """Un email sin @ debe retornar error."""
    user = {
        "id": "abc12345",
        "name": "Ana Torres",
        "email": "correo-invalido",
        "age": 25,
        "role": "usuario",
    }
    errors = validate_user(user)
    assert any("email" in e.lower() for e in errors), "Debe detectar email invalido."


def test_edad_fuera_de_rango():
    """Una edad de 0 o mayor a 119 debe retornar error."""
    user = {
        "id": "abc12345",
        "name": "Ana Torres",
        "email": "ana@correo.com",
        "age": 0,
        "role": "usuario",
    }
    errors = validate_user(user)
    assert any("edad" in e.lower() for e in errors), "Debe detectar edad invalida."


def test_rol_invalido():
    """Un rol que no sea admin/editor/usuario debe retornar error."""
    user = {
        "id": "abc12345",
        "name": "Ana Torres",
        "email": "ana@correo.com",
        "age": 25,
        "role": "superusuario",
    }
    errors = validate_user(user)
    assert any("rol" in e.lower() for e in errors), "Debe detectar rol invalido."


def test_lambda_email_valido():
    """La lambda is_valid_email debe aprobar un email correcto."""
    assert is_valid_email("test@correo.com") is True


def test_lambda_email_invalido():
    """La lambda is_valid_email debe rechazar un email sin @."""
    assert is_valid_email("sinArroba") is False


def test_lambda_is_not_empty():
    """La lambda is_not_empty debe rechazar strings vacios o con espacios."""
    assert is_not_empty("hola") is True
    assert is_not_empty("") is False
    assert is_not_empty("   ") is False