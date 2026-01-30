# 📦 Sistema de Inventario – Almacén (ABP 3)

Proyecto desarrollado en Python como parte del ABP 3.  
El sistema permite gestionar el inventario de un almacén mediante consola,
utilizando un enfoque modular.

---

## 🎯 Objetivo del proyecto
Desarrollar un sistema que permita:
- Agregar y reponer productos
- Listar productos disponibles
- Buscar productos por ID
- Vender productos y actualizar stock
- Visualizar un reporte del inventario

---

## 🗂️ Estructura del proyecto

El proyecto está organizado de forma modular:

- **main.py**  
  Archivo principal. Contiene el menú y controla el flujo del programa.

- **modulos_funcionesutiles/**
  - **data.py**: contiene el inventario inicial.
  - **productos.py**: funciones para agregar, listar, buscar y vender productos.
  - **reporte.py**: genera el reporte del inventario.
  - **__init__.py**: permite que la carpeta funcione como módulo.

---

## ⚙️ Descripción de módulos

- **main.py**  
  Punto de entrada del sistema. Contiene el menú y controla el flujo principal.

- **data.py**  
  Contiene el inventario inicial, almacenado en un diccionario.

- **productos.py**  
  Funciones para agregar/reponer productos, listar, buscar y vender.

- **reporte.py**  
  Genera un reporte general del inventario.

---

## 📋 Menú del sistema

1. Agregar producto / Reponer stock  
2. Listar productos  
3. Buscar producto por ID  
4. Vender producto  
5. Reporte de inventario  
6. Salir  

---## 🧠 Desafíos y soluciones implementadas

### 1. Ordenar el código para poder entenderlo mejor
**Desafío:**  
Al principio tenía gran parte del código junto y se me hacía difícil leerlo y saber qué hacía cada cosa, 
sobre todo cuando el programa empezó a crecer.

**Solución:**  
Decidí separar el sistema en distintos archivos según su función.  
Por ejemplo, dejé los datos del inventario en un archivo, 
las funciones de productos en otro y el menú principal en `main.py`.  
Esto me ayudó a entender mejor el flujo del programa y a trabajar de forma más ordenada. 
--- Esto es modularizar !! 

---

### 2. Evitar que el programa se cayera por errores del usuario
**Desafío:**  
Me di cuenta de que el programa podía fallar
si el usuario ingresaba letras en vez de números o valores que no tenían sentido, como cantidades negativas.

**Solución:**  
Agregué validaciones y manejo de errores para controlar estos casos, 
mostrando mensajes claros y evitando que el sistema se cierre inesperadamente.  
De esta forma el programa es más estable y fácil de usar. --- Esto es Validar datos !! 


## 🖥️ Evidencia de funcionamiento

Las siguientes imágenes muestran el sistema funcionando correctamente:

### Menú principal
![Menú principal](screenshots/main_inicial.png)

### Agregar producto nuevo
![Agregar producto](screenshots/agregar_producto_nuevo.png)

### Listar productos
![Listar productos](screenshots/listar_producto.png)

### Buscar producto
![Buscar producto](screenshots/buscar_producto.png)

### Reporte de inventario
![Reporte de inventario](screenshots/reporte_de_inventario.png)



