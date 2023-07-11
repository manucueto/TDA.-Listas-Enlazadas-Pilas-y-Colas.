# TDA.-Listas-Enlazadas-Pilas-y-Colas.

Supongamos que uno de tus clientes tiene una aplicación de venta de
productos en línea. Cada producto tiene un nombre, una descripción, un precio y
una cantidad en stock. Además, cada producto puede tener diferentes opciones,
como tamaño, color, etc.
Este es un programa en Python que tiene las siguientes características:
1. Una clase "Producto" que tenga atributos para nombre, descripción, precio,
status,cantidad en stock, fecha de creación y de actualización. También tiene un método para actualizar la cantidad en stock cuando se realiza una
venta.
2. Una clase "ProductoConOpciones" que hereda de la clase "Producto" y tiene
un atributo adicional "opciones" que sea un diccionario con las diferentes
opciones disponibles para el producto (por ejemplo, {"tamaño": ["pequeño",
"mediano", "grande"], "color": ["rojo", "verde", "azul"]}). También tiene un
método para imprimir las opciones disponibles.
3. Una clase "Carrito" que tiene una lista enlazada(pila) de productos y
métodos para agregar productos, eliminar productos y calcular el total de la
compra.
4. Una clase "Orden" que tiene una lista de productos(cola) y un método para
generar una factura con el total de la compra y la información de cada
producto (nombre, precio, cantidad y opciones seleccionadas).(4 ptos)
5. Un controlador que permite hacer lo siguiente: 
a. Listar catalogos de productos disponibles cuyo status sea activo y
stock sea mayor que cero(mostrar las opciones de cada producto)
b. Seleccionar productos y añadirlo al carrito de compras.
c. Hacer una compra con los productos agregados al carrito.
d. Listar ordenes creadas junto con susrspctivos datos y productos.
e. Listar productos del carrito actual
f. Al correr el programa, cargar datos desde un archivo csv(productos,
órdenes, carrito de compra
