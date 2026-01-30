# Sistema de gestión de productos (Almacén) - ABP 3
# main.py = punto de entrada (menú + flujo principal)

from modulos_funcionesutiles.data import inventario
from modulos_funcionesutiles.productos import agregar_o_reponer, listar_productos, buscar_producto, vender_producto
from modulos_funcionesutiles.reporte import mostrar_reporte



def mostrar_menu():
    print("\n" + "=" * 40)
    print("     SISTEMA INVENTARIO - ALMACÉN")
    print("=" * 40)
    print("1) Agregar producto / Reponer stock")
    print("2) Listar productos")
    print("3) Buscar producto por ID")
    print("4) Vender producto")
    print("5) Reporte de inventario")
    print("6) Salir")


def leer_opcion():
    # Esto evita que se caiga si escriben letras
    try:
        return int(input("Elige una opción (1-6): ").strip())
    except ValueError:
        return -1


def main():
    while True:
        mostrar_menu()
        opcion = leer_opcion()

        if opcion == 1:
            agregar_o_reponer(inventario)

        elif opcion == 2:
            listar_productos(inventario)

        elif opcion == 3:
            buscar_producto(inventario)

        elif opcion == 4:
            vender_producto(inventario)

        elif opcion == 5:
            mostrar_reporte(inventario)

        elif opcion == 6:
            print("Gracias por usar el sistema de inventario, Hasta luego!")
            break

        else:
            print("Opción inválida. Intenta nuevamente.")


if __name__ == "__main__":
    main()
