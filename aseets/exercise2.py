"""
exercise2.py
Abrir un archivo, capturar errores de apertura,
contar líneas en else, cerrar en finally y mostrar mensaje final.
"""


def contar_lineas(ruta: str) -> None:
    """
    Abre un archivo y cuenta sus líneas.
    - except: captura error si no existe o no se puede abrir
    - else: cuenta líneas si no hubo error
    - finally: siempre muestra mensaje final
    """
    archivo = None
    try:
        archivo = open(ruta, "r", encoding="utf-8")
    except FileNotFoundError:
        print(f"[ERROR] El archivo '{ruta}' no existe.")
    except OSError as e:
        print(f"[ERROR] No se pudo abrir el archivo: {e}")
    else:
        lineas = archivo.readlines()
        print(f"El archivo tiene {len(lineas)} línea(s).")
    finally:
        if archivo:
            archivo.close()
        print("Operación finalizada.")


def main():
    print("=== Ejercicio 2: Contar líneas de un archivo ===")
    ruta = input("Ingresa la ruta del archivo: ").strip()
    contar_lineas(ruta)


if __name__ == "__main__":
    main()