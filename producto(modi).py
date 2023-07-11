from datetime import datetime
import csv
class Producto:
    def __init__(self, nombre, descripcion, precio, status, cantidadStock):
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.status = status
        self.cantidadStock = cantidadStock
        self.fechaCreacion = datetime.now()
        self.fechaActualizacion = datetime.now()

    def imprimir(self):
        print(f' - Nombre: {self.nombre}\n Descripcion: {self.descripcion}\n Precio: {self.precio}\n Estatus: {self.status}\n Cantidad en Stock: {self.cantidadStock} \n Fecha de creacion: {self.fechaCreacion}\n Fecha de actualizacion: {self.fechaActualizacion}\n')

    def actualizar_stock(self, cantidadVendida):

        self.cantidadStock -= cantidadVendida
        self.fechaActualizacion = datetime.now()

class ProductoConOpciones(Producto):
    def __init__(self, nombre, descripcion, precio, status, cantidadStock, opciones):
        super().__init__(nombre, descripcion, precio, status, cantidadStock)
        self.opciones = opciones
        self.fechaCreacion = datetime.now()
        self.fechaActualizacion = datetime.now()

    def imprimirOpciones(self):
        for clave, valor in self.opciones.items():
            print(f"{clave}: {', '.join(valor)}")



class Nodo:
    def __init__(self,valor):
        self.valor = valor
        self.siguiente = None

class Carrito:
    def __init__(self):
        self.tope = None
        self.tamaño = 0

    def esta_vacia(self):
        return self.tope is None

    def agregar(self, valor):
        miNodo = Nodo(valor)
        if self.tamaño == 0:
            self.tope = miNodo
        else:
            actual = self.tope
            while actual.siguiente != None:
                actual = actual.siguiente

            actual.siguiente = miNodo
        
        self.tamaño += 1
        print(f"{valor} ha sido agregado")

    def mostrar2(self):
        if self.esta_vacia():
            print('La lista está vacía')
        else:
            temporal = self.tope
            while temporal:
                obj = temporal.valor
                este = obj
                produc = este.valor
                produc.valor.imprimir() 
                temporal = temporal.siguiente
    def mostrar(self):
        if self.esta_vacia():
            print('La lista está vacía')
        else:
            temporal = self.tope
            while temporal:
                obj = temporal.valor
                este = obj
                este.valor.imprimir() 
                temporal = temporal.siguiente

    def eliminar(self, nombre):
        if self.esta_vacia():
            return None
        anterior = None
        temporal = self.tope
        while temporal:
            if temporal.valor.nombre == nombre:
                if anterior:
                    anterior.siguiente = temporal.siguiente
                else:
                    self.tope = temporal.siguiente
                break
            anterior = temporal
            temporal = temporal.siguiente
        self.mostrar()

    
    def eliminar1(self, nombre): #error con este
        if self.tamaño == 0:
            print("El carrito está vacío")
            return False
        else:
            actual = self.tope
            
            while actual.siguiente.valor.nombre != nombre:
                if actual.siguiente == None:
                    print("El producto que desea eliminar no se encuentra")
                else:
                    actual = actual.siguiente
            NodoEliminado = actual.siguiente
            actual.siguiente = NodoEliminado.siguiente

        self.tamaño -= 1
        print(f"{nombre} ha sido eliminado")

    def calcularTotal(self):
        total = 0
        if self.esta_vacia():
            print('La lista está vacía')
        
        else:
            actual = self.tope
            while actual:
                obj = actual.valor
                este = obj
                total += este.valor.precio
                actual = actual.siguiente
           
        return total
    def calcularTotal2(self):
        total = 0
        if self.esta_vacia():
            print('La lista está vacía')
        
        else:
            actual = self.tope
            while actual:
                obj = actual.valor
                este = obj
                total += este.valor.valor.precio
                actual = actual.siguiente
            
        return total
    
class Orden():
    def __init__(self):
        self.frente = None
        self.fin = None
    
    def esta_vacia(self):
        return self.frente is None
    
    def imprimir(self):
        print(f' - Nombre: {self.nombre} Descripcion: {self.descripcion} Precio: {self.precio} Estatus: {self.status} Cantidad en Stock: {self.cantidadStock} \n Fecha de creacion: {self.fechaCreacion} Fecha de actualizacion: {self.fechaActualizacion}\n')
    
    def agregar(self, valor):
        nodo_nuevo = Nodo(valor)
        if self.esta_vacia():
            self.frente = nodo_nuevo
        else:
            self.fin.siguiente = nodo_nuevo
        self.fin = nodo_nuevo
        

    def mostrar(self):
        if self.esta_vacia():
            print('La lista está vacía')
        temporal = self.frente
        while temporal:
            temporal.valor.imprimir()
            temporal = temporal.siguiente

    def facturar(self):
        total = 0
        actual = self.frente
        while actual != None:
            total += actual.valor.precio
            actual = actual.siguiente
        print('                     ____________________ Factura ____________________            ')
        self.mostrar()
        print("El total de la compra es: " + str(total))

# . Listar catalogos de productos disponibles cuyo status sea activo y
# stock sea mayor que cero(mostrar las opciones de cada producto
def listar_productos(nodo):
    cont = 0
    i = 1
    lista_momentanea = Orden()
    while nodo:
        producto = nodo.valor
        if producto.status == "activo" and producto.cantidadStock > 0:
            print(f"-----Producto {i}-----")
            i += 1
            cont += 1
            print(f"Nombre: {producto.nombre}")
            print(f"Descripción: {producto.descripcion}")
            print(f"Precio: {producto.precio}")
            if isinstance(producto, ProductoConOpciones):
                print("Opciones")
                cont = producto.imprimirOpciones()
        lista_momentanea.agregar(nodo)
        nodo = nodo.siguiente
    return lista_momentanea, cont
#Seleccionar productos y añadirlo al carrito de compras.

def iterar(listaEnlazada, n):
    actual = listaEnlazada.frente
    cont = 1
    while cont<n and actual is not None:
        actual = actual.siguiente
        cont += 1
    return actual
        
def imprimir_opciones(nodo):
    cont = 1
    print("Eliga producto por su número: ")
    while nodo:
        producto = nodo.valor
        print(f"-----------Producto {cont}-------")
        print(f"Nombre: {producto.nombre}")
        print(f"Descripción: {producto.descripcion}")
        print(f"Precio: {producto.precio}")

        nodo = nodo.siguiente
        cont += 1
    return cont
    
    
def selecionar(nodo,milista):
    miCarrito = Carrito()
    miCarrito2 = Carrito()
    cent = 0
    while cent == 0:
        imprimir_opciones(nodo)
        print("""\n[] Presione 1 para elegir el Producto 1\n
        [] Presione 2 para elegir el Producto 2\n
        [] Presione 3 para elegir el Producto 3\n
        [] Presione 4 para elegir el Producto 4\n
        [] Presione 5 para elegir el Producto 5\n
        [] Presione 6 para elegir el Producto 6\n
        [] Presione 7 para ver Carrito\n
        [] Presione 8 para listar catalogos de productos disponibles cuyo status sea activo y stock sea mayor que cero\n
        [] Presione 9 para pagar \n
        [] Presione 10 para salir del carrito""")
        while True:
            try:
                opcionElegida = int(input())
                break
            except:
                print("No ha ingresado una opción. Por favor ingrese una opción valida: ")
        match opcionElegida:
            case 1:
                seleccionado = iterar(milista,1)
                miCarrito.agregar(seleccionado)
                selec = seleccionado.valor
                print(f"{selec.nombre} ha sido añadido al carrito")
            case 2:
                seleccionado = iterar(milista,2)
                miCarrito.agregar(seleccionado)
                selec = seleccionado.valor
                print(f"{selec.nombre} ha sido añadido al carrito")
            case 3:
                seleccionado = iterar(milista,3)
                miCarrito.agregar(seleccionado)
                selec = seleccionado.valor
                print(f"{selec.nombre} ha sido añadido al carrito")
            case 4:
                seleccionado = iterar(milista,4)
                miCarrito.agregar(seleccionado)
                selec = seleccionado.valor
                print(f"{selec.nombre} ha sido añadido al carrito")
            case 5:
                seleccionado = iterar(milista,5)
                miCarrito.agregar(seleccionado)
                selec = seleccionado.valor
                print(f"{selec.nombre} ha sido añadido al carrito")
            case 6:
                seleccionado = iterar(milista,6)
                miCarrito.agregar(seleccionado)
                selec = seleccionado.valor
                print(f"{selec.nombre} ha sido añadido al carrito")
            case 7:
                miCarrito.mostrar()
                miCarrito2.mostrar2()
            case 8:
                catalogoFiltrado, cont= listar_productos(nodo)
                while True:
                    print("Eliga el producto por su numero: ")
                    try:
                        opcionElegida2 = int(input())
                        if opcionElegida2 <= cont:
                            seleccionado = iterar(catalogoFiltrado,opcionElegida2)
                            miCarrito2.agregar(seleccionado)
                            selec = seleccionado.valor
                            print(f"{selec.valor.nombre} ha sido añadido al carrito")
                            break
                        else: 
                            print("Eliga un producto valido")
                    except:
                        print("Ingrese una opción valida")
            case 9:
                total1 = miCarrito.calcularTotal()
                total2 = miCarrito2.calcularTotal2()
                print(f"El total es: {total1+total2}")
                while True:
                    print("¿Deseas pagar(si/no)?")
                    pago = str(input())
                    if pago == "si":
                        miCarrito = Carrito()
                        miCarrito2 = Carrito()
                        print("Compra exitosa")
                        break
                    elif pago == "no":
                        break
                    else:
                        print("Por favor indique(si/no):")

            case 10:
                cent = 1
                return milista
            

def csv_():
    lista = Orden()
    notes = ''
    with open('productos.csv', newline='') as f:
        reader = csv.reader(f, delimiter=',')
        notes = list(reader)
        for i in range(len(notes)):
            nombre = notes[i][0]
            descripcion = notes[i][1]
            precio = float(notes[i][2])
            status = notes[i][3]
            cantidadStock = int(notes[i][4])
            producto = Producto(nombre, descripcion, precio, status, cantidadStock)
            lista.agregar(producto)
    return lista


                                                                                                                                                                    

    




lista = csv_()
selecionar(lista.frente, lista)


# secador = Producto("secador", "para pelo", 4, "activo", 6)
# harina = Producto("harina", "para arepa", 4, "activo", 6)
# par = ProductoConOpciones("par", "par de zapatos", 4, "no", 6, {"tamaño":["pequeños","medianos","grandes"], "color":["azul","amarillo","verde"]})
# pan = Producto("pan", "pa comer", 4, "activo", 6)
# milista = Orden()
# milista.agregar(secador)
# milista.agregar(harina)
# milista.agregar(par)
# milista.agregar(pan)


# secador = Producto("secador", "para pelo", 4, 1, 6)
# harina = Producto("harina", "para pelo", 4, 1, 6)
# compu = Producto("compu", "para pelo", 4, 1, 6)

# miLista = Carrito()

# miLista.agregar(secador)
# miLista.agregar(harina)
# miLista.agregar(compu)

# miLista.eliminar(harina)
# miLista.calcularTotal()

