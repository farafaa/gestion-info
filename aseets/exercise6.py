"""
exercise6.py
Refactor del procesador de ventas.
Separación de lógica, I/O y pruebas.
"""


# ── Lógica pura (sin prints) ──────────────────────────────────────────────────

def calcular_descuento(qty: int, customer: str) -> float:
    """
    Calcula el descuento según cantidad y tipo de cliente.

    Args:
        qty: cantidad de unidades
        customer: tipo de cliente ('vip' u otro)

    Returns:
        Descuento como decimal (ej: 0.15 = 15%)
    """
    descuento = 0.0
    if qty >= 10:
        descuento += 0.10
    if customer == "vip":
        descuento += 0.05
    return descuento


def calculate_sale_total(sale: dict) -> float:
    """
    Calcula el subtotal de una venta válida aplicando descuentos.

    Args:
        sale: diccionario con keys 'status', 'price', 'qty', 'customer'

    Returns:
        Subtotal con descuento aplicado.

    Raises:
        ValueError: si la venta no tiene status 'ok'
    """
    if sale.get("status") != "ok":
        raise ValueError(f"Venta inválida: {sale}")

    price    = sale["price"]
    qty      = sale["qty"]
    customer = sale.get("customer", "")

    descuento = calcular_descuento(qty, customer)
    subtotal  = price * qty
    return subtotal * (1 - descuento)


def calculate_total(sales: list) -> float:
    """
    Suma los totales de todas las ventas válidas.
    Las ventas inválidas se ignoran silenciosamente.

    Args:
        sales: lista de diccionarios de ventas

    Returns:
        Total acumulado de ventas válidas.
    """
    total = 0.0
    for sale in sales:
        try:
            total += calculate_sale_total(sale)
        except (ValueError, KeyError):
            pass  # Ventas inválidas se ignoran
    return total


def report_invalid_sales(sales: list) -> None:
    """Imprime las ventas que no tienen status 'ok'."""
    invalidas = [s for s in sales if s.get("status") != "ok"]
    if invalidas:
        print("Ventas inválidas:")
        for venta in invalidas:
            print(f"  - {venta}")


# ── Pruebas manuales ──────────────────────────────────────────────────────────

def test_suma_ventas_ok():
    ventas = [
        {"status": "ok", "price": 100, "qty": 2, "customer": "normal"},
        {"status": "ok", "price": 50,  "qty": 3, "customer": "normal"},
    ]
    assert calculate_total(ventas) == 350.0

def test_descuento_por_cantidad():
    venta = {"status": "ok", "price": 100, "qty": 10, "customer": "normal"}
    # 100 * 10 = 1000, descuento 10% → 900
    assert calculate_sale_total(venta) == 900.0

def test_descuento_vip():
    venta = {"status": "ok", "price": 100, "qty": 10, "customer": "vip"}
    # 1000, descuento 15% → 850
    assert calculate_sale_total(venta) == 850.0

def test_venta_invalida_lanza_error():
    venta = {"status": "bad", "price": 100, "qty": 2, "customer": "normal"}
    try:
        calculate_sale_total(venta)
        assert False, "Debía lanzar ValueError"
    except ValueError:
        pass

def test_ventas_invalidas_se_ignoran():
    ventas = [
        {"status": "ok",  "price": 100, "qty": 1, "customer": "normal"},
        {"status": "bad", "price": 100, "qty": 5, "customer": "normal"},
    ]
    assert calculate_total(ventas) == 100.0


def ejecutar_pruebas():
    pruebas = [
        test_suma_ventas_ok,
        test_descuento_por_cantidad,
        test_descuento_vip,
        test_venta_invalida_lanza_error,
        test_ventas_invalidas_se_ignoran,
    ]
    print("=== Pruebas exercise6 ===")
    for prueba in pruebas:
        try:
            prueba()
            print(f"  ✓ {prueba.__name__}")
        except AssertionError as e:
            print(f"  ✗ {prueba.__name__} FALLÓ: {e}")


def main():
    print("=== Ejercicio 6: Procesamiento de ventas ===")
    ventas = [
        {"status": "ok",  "price": 200, "qty": 10, "customer": "vip"},
        {"status": "ok",  "price": 100, "qty": 5,  "customer": "normal"},
        {"status": "bad", "price": 50,  "qty": 2,  "customer": "normal"},
        {"status": "ok",  "price": 300, "qty": 1,  "customer": "vip"},
    ]
    report_invalid_sales(ventas)
    total = calculate_total(ventas)
    print(f"\nTOTAL ventas válidas: ${total:.2f}")
    print()
    ejecutar_pruebas()


if __name__ == "__main__":
    main()