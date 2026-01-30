# productos.py
# Funciones relacionadas con la gestión de productos


def agregar_o_reponer(inventario):
    print("\n--- AGREGAR / REPONER PRODUCTO ---")

    try:
        id_producto = int(input("ID del producto: "))
    except ValueError:
        print("ID inválido.")
        return

    # Si el producto ya existe → reponer stock
    if id_producto in inventario:
        try:
            cantidad = int(input("Cantidad a reponer: "))
        except ValueError:
            print("Cantidad inválida.")
            return

        if cantidad <= 0:
            print("La cantidad debe ser mayor a 0.")
            return

        inventario[id_producto]["stock"] += cantidad
        print("Stock actualizado correctamente.")

    # Si NO existe → crear producto nuevo
    else:
        nombre = input("Nombre del producto: ").strip()

        try:
            precio = int(input("Precio del producto: "))
            stock = int(input("Stock inicial: "))
        except ValueError:
            print("Precio o stock inválido.")
            return

        if precio <= 0 or stock < 0:
            print("Precio o stock no válidos.")
            return

        inventario[id_producto] = {
            "nombre": nombre,
            "precio": precio,
            "stock": stock
        }

        print("Producto agregado correctamente.")


def listar_productos(inventario):
    print("\n--- LISTA DE PRODUCTOS ---")

    if not inventario:
        print("No hay productos registrados.")
        return

    for id_prod, datos in inventario.items():
        print(
            f"ID: {id_prod} | "
            f"{datos['nombre']} | "
            f"Precio: ${datos['precio']} | "
            f"Stock: {datos['stock']}"
        )


def buscar_producto(inventario):
    print("\n--- BUSCAR PRODUCTO ---")

    try:
        id_producto = int(input("ID del producto: "))
    except ValueError:
        print("ID inválido.")
        return

    if id_producto in inventario:
        datos = inventario[id_producto]
        print(
            f"ID: {id_producto}\n"
            f"Nombre: {datos['nombre']}\n"
            f"Precio: ${datos['precio']}\n"
            f"Stock: {datos['stock']}"
        )
    else:
        print("Producto no encontrado.")


def vender_producto(inventario):
    print("\n--- VENDER PRODUCTO ---")

    try:
        id_producto = int(input("ID del producto: "))
    except ValueError:
        print("ID inválido.")
        return

    if id_producto not in inventario:
        print("Producto no existe.")
        return

    try:
        cantidad = int(input("Cantidad a vender: "))
    except ValueError:
        print("Cantidad inválida.")
        return

    if cantidad <= 0:
        print("La cantidad debe ser mayor a 0.")
        return

    if inventario[id_producto]["stock"] < cantidad:
        print("Stock insuficiente.")
        return

    inventario[id_producto]["stock"] -= cantidad
    print("Venta registrada correctamente.")
