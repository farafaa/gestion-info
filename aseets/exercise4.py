"""
exercise4.py
Refactor de calculadora:
- Operaciones con nombres claros (suma, resta, multi, divi)
- Excepciones en lugar de retornar strings de error
- Tipos consistentes (siempre float o excepción)
- Separación de I/O y lógica
"""


class OperacionInvalidaError(Exception):
    """Se lanza cuando la operación solicitada no existe."""
    pass


def calc(a: float, b: float, op: str) -> float:
    """
    Calcula el resultado de la operación entre a y b.

    Args:
        a: primer número
        b: segundo número
        op: operación ('suma', 'resta', 'multi', 'divi')

    Returns:
        Resultado como float.

    Raises:
        ZeroDivisionError: si op='divi' y b=0
        OperacionInvalidaError: si op no es válida
    """
    ops = {
        "suma":  lambda x, y: x + y,
        "resta": lambda x, y: x - y,
        "multi": lambda x, y: x * y,
        "divi":  lambda x, y: x / y,   # ZeroDivisionError automático si y=0
    }

    if op not in ops:
        raise OperacionInvalidaError(
            f"Operación '{op}' no válida. Usa: {', '.join(ops.keys())}"
        )

    return ops[op](a, b)


def main():
    print("=== Ejercicio 4: Calculadora refactorizada ===")
    try:
        op = input("Ingrese operación (suma, resta, multi, divi): ").strip().lower()
        a  = float(input("Ingrese primer número: "))
        b  = float(input("Ingrese segundo número: "))
        resultado = calc(a, b, op)
        print(f"El resultado de {op} es: {resultado}")
    except ZeroDivisionError:
        print("[ERROR] No se puede dividir entre cero.")
    except OperacionInvalidaError as e:
        print(f"[ERROR] {e}")
    except ValueError:
        print("[ERROR] Los valores ingresados no son números válidos.")


if __name__ == "__main__":
    main()