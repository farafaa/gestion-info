"""
menu.py — Interfaz de consola (UI)
Muestra el menú principal e invoca la lógica del sistema.
"""

from service import (
    create_user,
    list_users,
    update_user,
    delete_user,
)
from integration import generate_fake_users


def show_menu():
    """Bucle principal del menú interactivo."""
    options = {
        "1": ("Crear usuario", create_user),
        "2": ("Listar usuarios", list_users),
        "3": ("Actualizar usuario", update_user),
        "4": ("Eliminar usuario", delete_user),
        "5": ("Generar usuarios de prueba (Faker)", _generate_users),
        "0": ("Salir", None),
    }

    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        for key, (label, _) in options.items():
            print(f"  [{key}] {label}")

        choice = input("\nElige una opción: ").strip()

        if choice == "0":
            print("Hasta luego 👋")
            break
        elif choice in options:
            _, action = options[choice]
            try:
                action()
            except Exception as e:
                print(f"[ERROR] Ocurrió un problema: {e}")
        else:
            print("Opción no válida. Intenta de nuevo.")


def _generate_users():
    """Wrapper para solicitar cuántos usuarios generar."""
    try:
        n = int(input("¿Cuántos usuarios falsos deseas generar? "))
        generate_fake_users(n)
    except ValueError:
        print("Debes ingresar un número entero.")
