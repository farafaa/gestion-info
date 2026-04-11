"""
exercise1.py
Leer enteros separados por comas, calcular el promedio
y manejar errores de conversión.
"""


def calcular_promedio(entrada: str) -> float:
    """
    Convierte una cadena de números separados por comas a lista de enteros
    y calcula el promedio. Lanza ValueError si algún valor no es número.
    """
    valores = []
    for item in entrada.split(","):
        try:
            valores.append(int(item.strip()))
        except ValueError:
            raise ValueError(f"'{item.strip()}' no es un número entero válido.")

    if not valores:
        raise ValueError("No se ingresaron valores.")

    # Promedio correcto: suma / cantidad
    return sum(valores) / len(valores)


def main():
    print("=== Ejercicio 1: Promedio de enteros ===")
    entrada = input("Ingresa números separados por comas: ")

    try:
        promedio = calcular_promedio(entrada)
        print(f"Promedio: {promedio:.2f}")
    except ValueError as e:
        print(f"[ERROR] {e}")


if __name__ == "__main__":
    main()