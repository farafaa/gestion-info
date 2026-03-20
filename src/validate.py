"""
validate.py — Validaciones y helpers
Funciones para verificar integridad de datos y dar formato a la salida.
"""

import re

VALID_ROLES = {"admin", "editor", "usuario"}

# Lambda: verifica que un string no esté vacío
is_not_empty = lambda s: bool(s and str(s).strip())

# Lambda: valida formato básico de email
is_valid_email = lambda e: bool(re.match(r"[^@]+@[^@]+\.[^@]+", str(e)))


def validate_user(user: dict) -> list:
    """
    Valida un diccionario de usuario.
    Retorna lista de mensajes de error (vacía = válido).
    """
    errors = []

    if not is_not_empty(user.get("name")):
        errors.append("El nombre no puede estar vacío.")

    if not is_valid_email(user.get("email", "")):
        errors.append("El email no tiene un formato válido.")

    try:
        age = int(user.get("age", -1))
        if not (0 < age < 120):
            errors.append("La edad debe estar entre 1 y 119 años.")
    except (ValueError, TypeError):
        errors.append("La edad debe ser un número entero.")

    if user.get("role", "").lower() not in VALID_ROLES:
        errors.append(f"El rol debe ser uno de: {', '.join(VALID_ROLES)}.")

    return errors


def format_user_display(user: dict) -> str:
    """Formatea un usuario como fila de tabla para consola."""
    return (
        f"{user.get('id', ''):<10} "
        f"{user.get('name', ''):<25} "
        f"{user.get('email', ''):<30} "
        f"{user.get('age', ''):<6} "
        f"{user.get('role', '')}"
    )
