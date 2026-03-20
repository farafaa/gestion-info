"""
integration.py — Integración con librería externa: Faker
Genera usuarios falsos realistas para poblar el sistema en pruebas.
"""

import random

try:
    from faker import Faker
except ImportError:
    Faker = None

from service import create_user

ROLES = ["admin", "editor", "usuario"]


def generate_fake_users(n: int = 5) -> list:
    """
    Genera `n` usuarios falsos usando Faker y los agrega al sistema.
    Usa *args internamente a través de **kwargs en create_user.
    """
    if Faker is None:
        print("[ERROR] La librería 'faker' no está instalada.")
        print("  Ejecuta: pip install faker")
        return []

    fake = Faker("es_MX")  # Nombres en español
    created = []
    skipped = 0

    print(f"\n  Generando {n} usuario(s) de prueba...")

    for _ in range(n):
        try:
            user = create_user(
                name=fake.name(),
                email=fake.unique.email(),
                age=random.randint(18, 65),
                role=random.choice(ROLES),
            )
            created.append(user)
        except ValueError as e:
            # Email duplicado u otro error de validación: se omite
            skipped += 1

    print(f"  ✓ {len(created)} creado(s), {skipped} omitido(s) por duplicados.")
    return created
