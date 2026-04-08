"""
menu.py — Interfaz de consola (UI)
Muestra el menú principal e invoca la lógica del sistema.
"""

from service import (
    new_register,
    list_records,
    search_record,
    update_record,
    delete_record,
)
from integration import generate_fake_users


def show_menu():
    """Bucle principal del menú interactivo."""
    options = {
        "1": ("Crear usuario",                    new_register),
        "2": ("Listar usuarios",                  list_records),
        "3": ("Buscar usuario",                   search_record),
        "4": ("Actualizar usuario",               update_record),
        "5": ("Eliminar usuario",                 delete_record),
        "6": ("Generar usuarios de prueba (Faker)", _generate_users),
        "0": ("Salir",                            None),
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