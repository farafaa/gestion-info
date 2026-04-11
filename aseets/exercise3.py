"""
exercise3.py
Menú interactivo con:
  (1) Dividir números
  (2) Abrir archivo y mostrar primera línea
  (3) Salir
Captura: ValueError, ZeroDivisionError, FileNotFoundError y Exception.
"""


def dividir():
    """Solicita dos números y divide el primero entre el segundo."""
    try:
        a = int(input("  Ingresa el dividendo: "))
        b = int(input("  Ingresa el divisor: "))
        resultado = a / b
        print(f"  Resultado: {resultado:.2f}")
    except ValueError:
        print("  [ERROR] Debes ingresar números enteros.")
    except ZeroDivisionError:
        print("  [ERROR] No se puede dividir entre cero.")


def mostrar_primera_linea():
    """Abre un archivo y muestra su primera línea."""
    try:
        ruta = input("  Ingresa la ruta del archivo: ").strip()
        with open(ruta, "r", encoding="utf-8") as f:
            primera = f.readline()
            print(f"  Primera línea: {primera.strip()}")
    except FileNotFoundError:
        print(f"  [ERROR] El archivo no existe.")
    except Exception as e:
        print(f"  [ERROR inesperado] {e}")


def main():
    print("=== Ejercicio 3: Menú con manejo de errores ===")

    opciones = {
        "1": ("Dividir números",              dividir),
        "2": ("Abrir archivo (primera línea)", mostrar_primera_linea),
        "3": ("Salir",                         None),
    }

    while True:
        print("\n--- MENÚ ---")
        for key, (label, _) in opciones.items():
            print(f"  [{key}] {label}")

        opcion = input("\nElige una opción: ").strip()

        if opcion == "3":
            print("Hasta luego.")
            break
        elif opcion in opciones:
            try:
                _, accion = opciones[opcion]
                accion()
            except Exception as e:
                print(f"  [ERROR no previsto] {e}")
        else:
            print("  Opción no válida.")


if __name__ == "__main__":
    main()