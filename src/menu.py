"""
menu.py — Interfaz de consola (UI)
Módulo 4: Menú interactivo con colorama y validación de entradas.
"""

from colorama import init, Fore, Style
from service import (
    new_register,
    list_records,
    search_record,
    update_record,
    delete_record,
)
from integration import generate_fake_users

init(autoreset=True)


def _header():
    print(Fore.CYAN + "=" * 45)
    print(Fore.CYAN + "   Sistema de Gestion de Usuarios")
    print(Fore.CYAN + "=" * 45)


def _print_menu():
    print(Fore.CYAN + "\n--- MENU PRINCIPAL ---")
    opciones = [
        ("1", "Crear usuario"),
        ("2", "Listar usuarios"),
        ("3", "Buscar usuario"),
        ("4", "Actualizar usuario"),
        ("5", "Eliminar usuario"),
        ("6", "Generar usuarios de prueba (Faker)"),
        ("0", "Salir"),
    ]
    for key, label in opciones:
        print(f"  {Fore.YELLOW}[{key}]{Style.RESET_ALL} {label}")


def _get_option(valid: set) -> str:
    """
    Solicita una opción y valida que sea correcta.
    Usa try-except para no romperse con letras u otros caracteres.
    """
    while True:
        try:
            choice = input(Fore.GREEN + "\nElige una opcion: " + Style.RESET_ALL).strip()
            if choice not in valid:
                raise ValueError
            return choice
        except ValueError:
            print(Fore.RED + f"  Opcion invalida. Elige entre: {sorted(valid)}")


def _generate_users():
    """Wrapper para solicitar cuántos usuarios generar con validación."""
    while True:
        try:
            n = int(input(Fore.GREEN + "Cuantos usuarios falsos deseas generar? " + Style.RESET_ALL))
            if n <= 0:
                raise ValueError
            generate_fake_users(n)
            break
        except ValueError:
            print(Fore.RED + "  Debes ingresar un numero entero mayor a 0.")


ACTIONS = {
    "1": new_register,
    "2": list_records,
    "3": search_record,
    "4": update_record,
    "5": delete_record,
    "6": _generate_users,
}


def show_menu():
    """Bucle principal del menú interactivo."""
    _header()
    valid_options = set(ACTIONS.keys()) | {"0"}

    while True:
        _print_menu()
        choice = _get_option(valid_options)

        if choice == "0":
            print(Fore.CYAN + "\nHasta luego!")
            break

        try:
            ACTIONS[choice]()
        except KeyboardInterrupt:
            print(Fore.YELLOW + "\n  Operacion cancelada.")
        except Exception as e:
            print(Fore.RED + f"\n  [ERROR] {e}")