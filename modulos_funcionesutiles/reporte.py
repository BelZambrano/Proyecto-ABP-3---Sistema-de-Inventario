# reporte.py
# Funciones de reporte (solo lectura y cálculos)

def mostrar_reporte(inventario):
    print("\n" + "=" * 40)
    print("        REPORTE DE INVENTARIO")
    print("=" * 40)

    if not inventario:
        print("No hay productos registrados.")
        return

    total_productos = len(inventario)
    stock_total = 0
    valor_total = 0

    # Recorremos cada producto para sumar totales
    for _id, datos in inventario.items():
        stock = datos["stock"]
        precio = datos["precio"]

        stock_total += stock
        valor_total += (stock * precio)

    print(f"Productos distintos: {total_productos}")
    print(f"Stock total: {stock_total}")
    print(f"Valor total inventario: ${valor_total}")

    print("\n--- DETALLE ---")
    for _id, datos in inventario.items():
        subtotal = datos["stock"] * datos["precio"]
        print(
            f"ID: {_id} | {datos['nombre']} | "
            f"Precio: ${datos['precio']} | Stock: {datos['stock']} | "
            f"Subtotal: ${subtotal}"
        )
