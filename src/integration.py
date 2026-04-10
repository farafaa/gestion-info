"""
integration.py — Integración con librería externa: Faker
Módulo 5: Genera usuarios falsos realistas usando *args/**kwargs.
"""

import random

try:
    from faker import Faker
except ImportError:
    Faker = None

from service import new_register

ROLES = ["admin", "editor", "usuario"]


def generate_fake_users(n: int = 5, *args, **kwargs) -> list:
    """
    Genera `n` usuarios falsos usando Faker y los guarda en el sistema.

    Parámetros opcionales via **kwargs:
        - locale (str): idioma para Faker. Por defecto 'es_MX'.
        - role (str): forzar un rol específico para todos los usuarios.

    Uso de *args/**kwargs:
        generate_fake_users(10)
        generate_fake_users(5, locale='en_US')
        generate_fake_users(3, role='admin')
    """
    if Faker is None:
        print("[ERROR] La libreria 'faker' no esta instalada.")
        print("  Ejecuta: pip install faker")
        return []

    locale = kwargs.get("locale", "es_MX")
    forced_role = kwargs.get("role", None)

    fake = Faker(locale)
    created = []
    skipped = 0

    print(f"\n  Generando {n} usuario(s) de prueba...")

    for _ in range(n):
        try:
            user = new_register(
                name=fake.name(),
                email=fake.unique.email(),
                age=random.randint(18, 65),
                role=forced_role if forced_role else random.choice(ROLES),
            )
            created.append(user)
        except ValueError:
            skipped += 1

    print(f"  {len(created)} creado(s), {skipped} omitido(s) por duplicados.")
    return created