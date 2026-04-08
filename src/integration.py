"""
integration.py — Integración con librería externa: Faker
Genera usuarios falsos realistas para poblar el sistema en pruebas.
"""

import random

try:
    from faker import Faker
except ImportError:
    Faker = None

from service import new_register

ROLES = ["admin", "editor", "usuario"]


def generate_fake_users(n: int = 5) -> list:
    """
    Genera `n` usuarios falsos usando Faker y los agrega al sistema.
    Usa **kwargs en new_register para llamada programática.
    """
    if Faker is None:
        print("[ERROR] La librería 'faker' no está instalada.")
        print("  Ejecuta: pip install faker")
        return []

    fake = Faker("es_MX")
    created = []
    skipped = 0

    print(f"\n  Generando {n} usuario(s) de prueba...")

    for _ in range(n):
        try:
            user = new_register(
                name=fake.name(),
                email=fake.unique.email(),
                age=random.randint(18, 65),
                role=random.choice(ROLES),
            )
            created.append(user)
        except ValueError:
            skipped += 1

    print(f"  ✓ {len(created)} creado(s), {skipped} omitido(s) por duplicados.")
    return created