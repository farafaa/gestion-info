"""
service.py — Lógica de negocio (CRUD)
Operaciones sobre la colección de usuarios en memoria + persistencia.
"""

import uuid
from file import load_records, save_records
from validate import validate_user, format_user_display


# ── Helpers internos ──────────────────────────────────────────────────────────

def _get_all() -> list:
    return load_records()


def _save_all(users: list) -> None:
    save_records(users)


def _find_by_id(users: list, user_id: str) -> dict | None:
    """Retorna el usuario que coincide con el ID, o None."""
    matches = [u for u in users if u["id"] == user_id]
    return matches[0] if matches else None


# ── CRUD ─────────────────────────────────────────────────────────────────────

def create_user(*args, **kwargs) -> dict:
    """
    Crea un nuevo usuario.
    Acepta **kwargs para poder llamarlo desde Faker o desde el menú.
    """
    if kwargs:
        # Llamada programática (ej. desde integration.py)
        name  = kwargs.get("name", "")
        email = kwargs.get("email", "")
        age   = kwargs.get("age", 0)
        role  = kwargs.get("role", "usuario")
    else:
        # Llamada interactiva desde el menú
        name  = input("Nombre completo: ").strip()
        email = input("Email: ").strip()
        age   = input("Edad: ").strip()
        role  = input("Rol (admin/editor/usuario): ").strip() or "usuario"

    user = {
        "id":    str(uuid.uuid4())[:8],
        "name":  name,
        "email": email,
        "age":   int(age),
        "role":  role,
    }

    errors = validate_user(user)
    if errors:
        for e in errors:
            print(f"  ✗ {e}")
        raise ValueError("Usuario inválido, no fue guardado.")

    users = _get_all()
    # Verificar email duplicado con set comprehension
    existing_emails = {u["email"].lower() for u in users}
    if user["email"].lower() in existing_emails:
        raise ValueError(f"El email '{user['email']}' ya existe.")

    users.append(user)
    _save_all(users)
    print(f"  ✓ Usuario '{user['name']}' creado con ID {user['id']}.")
    return user


def list_users() -> list:
    """Lista todos los usuarios registrados."""
    users = _get_all()
    if not users:
        print("  No hay usuarios registrados.")
        return []

    # List comprehension para formatear la salida
    rows = [format_user_display(u) for u in users]
    print(f"\n{'ID':<10} {'Nombre':<25} {'Email':<30} {'Edad':<6} {'Rol'}")
    print("-" * 80)
    for row in rows:
        print(row)
    print(f"\nTotal: {len(users)} usuario(s).")
    return users


def update_user() -> None:
    """Actualiza nombre, edad o rol de un usuario existente."""
    users = _get_all()
    if not users:
        print("  No hay usuarios para actualizar.")
        return

    user_id = input("ID del usuario a actualizar: ").strip()
    user = _find_by_id(users, user_id)
    if not user:
        print(f"  No se encontró usuario con ID '{user_id}'.")
        return

    print(f"  Editando: {user['name']} | {user['email']}")
    print("  (Deja en blanco para no cambiar el campo)")

    new_name  = input(f"  Nuevo nombre [{user['name']}]: ").strip()
    new_age   = input(f"  Nueva edad  [{user['age']}]: ").strip()
    new_role  = input(f"  Nuevo rol   [{user['role']}]: ").strip()

    if new_name:
        user["name"] = new_name
    if new_age:
        user["age"] = int(new_age)
    if new_role:
        user["role"] = new_role

    errors = validate_user(user)
    if errors:
        for e in errors:
            print(f"  ✗ {e}")
        raise ValueError("Datos inválidos, no se guardaron los cambios.")

    _save_all(users)
    print(f"  ✓ Usuario '{user['name']}' actualizado correctamente.")


def delete_user() -> None:
    """Elimina un usuario por ID."""
    users = _get_all()
    if not users:
        print("  No hay usuarios para eliminar.")
        return

    user_id = input("ID del usuario a eliminar: ").strip()
    user = _find_by_id(users, user_id)
    if not user:
        print(f"  No se encontró usuario con ID '{user_id}'.")
        return

    confirm = input(f"  ¿Eliminar a '{user['name']}'? (s/n): ").strip().lower()
    if confirm != "s":
        print("  Operación cancelada.")
        return

    # Lambda para filtrar sin el usuario eliminado
    updated = list(filter(lambda u: u["id"] != user_id, users))
    _save_all(updated)
    print(f"  ✓ Usuario '{user['name']}' eliminado.")
