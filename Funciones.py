from abc import ABC, abstractmethod

#Punto 1 | ¿Esto es Sano?
def ingrediente_sano(calorias: int, vegetariano: bool) -> bool:
     
    if calorias < 100 or vegetariano:
        return True
    else:
        return False
    
#Punto 2 | Las Calorías    
def calorias(calorias_numero: list) -> float:
    
    total_calorias = sum(calorias_numero)
    calorias_generadas = total_calorias * 0.95
    return round(calorias_generadas, 2)

#Punto 3 | Costos
def costo_producto(ing1: dict, ing2: dict, ing3: dict) -> float:
    
    costo_total = ing1["precio"] + ing2["precio"] + ing3["precio"]
    return costo_total

#Punto 4 | Rentabilidad
def rentabilidad_producto(precio: float, ingredientes1: dict, ingredientes2: dict, ingredientes3: dict)-> float:
    
    costo_total = ingredientes1["precio"] + ingredientes2["precio"] + ingredientes3["precio"]
    rentabilidad = precio - costo_total
    return rentabilidad

#Punto 5 | El mejor producto
def producto_rentable (producto1: dict,producto2: dict,producto3: dict,producto4: dict) -> str:

    productos = [producto1, producto2, producto3, producto4]
    producto_rentabilidad = max(productos, key=lambda p: p["rentabilidad"])
    return producto_rentabilidad["nombre"]

#Punto 7 | Ingrediente
class Ingrediente(ABC):
    def __init__(self, nombre: str, precio: float, calorias: int, inventario: int, es_vegetariano: bool):
        self._nombre = nombre
        self._precio = precio
        self._calorias = calorias
        self._inventario = inventario
        self._es_vegetariano = es_vegetariano
    
    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, nombre: str):
        self._nombre = nombre

    @property
    def precio(self) -> float:
        return self._precio

    @precio.setter
    def precio(self, precio: float):
        self._precio = precio

    @property
    def calorias(self) -> int:
        return self._calorias

    @calorias.setter
    def calorias(self, calorias: int):
        self._calorias = calorias

    @property
    def inventario(self) -> int:
        return self._inventario

    @inventario.setter
    def inventario(self, inventario: int):
        self._inventario = inventario

    @property
    def es_vegetariano(self) -> bool:
        return self._es_vegetariano

    @es_vegetariano.setter
    def es_vegetariano(self, es_vegetariano: bool):
        self._es_vegetariano = es_vegetariano

    def ingrediente_sano(calorias: int, vegetariano: bool) -> bool:
     
        if calorias < 100 or vegetariano:
            return True
        else:
            return False

    def abastecer(self, cantidad: int):
        self._inventario += cantidad

class Base(Ingrediente):
    def __init__(self, nombre: str, precio: float, calorias: int, inventario: int, es_vegetariano: bool, sabor: str):
        self._nombre = nombre
        self._precio = precio
        self._calorias = calorias
        self._inventario = inventario
        self._es_vegetariano = es_vegetariano
        self._sabor = sabor

    @property
    def sabor(self) -> str:
        return self._sabor

    @sabor.setter
    def sabor(self, sabor: str):
        self._sabor = sabor

    def abastecer(self, cantidad: int = 5):
        self._inventario += cantidad


class Complemento(Ingrediente):
    def __init__(self, nombre: str, precio: float, calorias: int, inventario: int, es_vegetariano: bool):
        self._nombre = nombre
        self._precio = precio
        self._calorias = calorias
        self._inventario = inventario
        self._es_vegetariano = es_vegetariano

    def abastecer(self, cantidad: int = 10):
        self._inventario += cantidad

    def renovar_inventario(self):
        self._inventario = 0

#Punto 9 | IProducto
class IProducto(ABC):

    @abstractmethod
    def costo_producto(ing1: dict, ing2: dict, ing3: dict) -> float:
    
        costo_total = ing1["precio"] + ing2["precio"] + ing3["precio"]
        return costo_total

    @abstractmethod
    def rentabilidad_producto(precio: float, ingredientes1: dict, ingredientes2: dict, ingredientes3: dict)-> float:
    
        costo_total = ingredientes1["precio"] + ingredientes2["precio"] + ingredientes3["precio"]
        rentabilidad = precio - costo_total
        return rentabilidad
    
    @abstractmethod
    def calorias(calorias_numero: list) -> float:
    
        total_calorias = sum(calorias_numero)
        calorias_generadas = total_calorias * 0.95
        return round(calorias_generadas, 2)
    

class Copa(IProducto):
    def __init__(self, nombre: str, precio_publico: float, ingredientes, tipo_vaso: str):
        self.nombre = nombre
        self.precio_publico = precio_publico
        self.ingredientes = ingredientes  
        self.tipo_vaso = tipo_vaso

    @property
    def tipo_vaso(self) -> str:
        return self._tipo_vaso

    @tipo_vaso.setter
    def tipo_vaso(self, tipo_vaso: str):
        self._tipo_vaso = tipo_vaso

    def costo_producto(self):
        return sum(ingrediente.precio for ingrediente in self.ingredientes)

    def rentabilidad_producto(self):
        costo = self.calcular_costo()
        return self.precio_publico - costo

    def calorias(self):
        total_calorias = sum(ingrediente.calorias for ingrediente in self.ingredientes)
        return round(total_calorias * 0.95, 2)
    

class Malteada(IProducto):
    def __init__(self, nombre: str, precio_publico: float, ingredientes, volumen: float):
        self.nombre = nombre
        self.precio_publico = precio_publico
        self.ingredientes = ingredientes  
        self.volumen = volumen  

    @property
    def volumen(self) -> float:
        return self._volumen

    @volumen.setter
    def volumen(self, volumen: float):
        self._volumen = volumen

    def costo_producto(self):
        return sum(ingrediente.precio for ingrediente in self.ingredientes) + 500  

    def rentabilidad_producto(self):
        costo = self.calcular_costo()
        return self.precio_publico - costo

    def calorias(self):
        total_calorias = sum(ingrediente.calorias for ingrediente in self.ingredientes)
        return total_calorias + 200  
    
#Punto 11 | Heladería

class Heladeria:
    def __init__(self):
        self.productos = []  
        self.ingredientes = []  
        self.ventas_diarias = 0  

    def agregar_producto(self, producto):
        if len(self.productos) < 4:
            self.productos.append(producto)
        else:
            print("No se pueden agregar más de 4 productos a la heladería.")

    def agregar_ingrediente(self, ingrediente):
        self.ingredientes.append(ingrediente)

    def vender_producto(self, producto_nombre):
        for producto in self.productos:
            if producto.nombre == producto_nombre:
                for ingrediente in producto.ingredientes:
                    if ingrediente.inventario <= 0:
                        print(f"No hay suficiente inventario para el ingrediente: {ingrediente.nombre}")
                    ingrediente.c -= 1  # Resta 1 del inventario por cada ingrediente utilizado
                self.ventas_diarias += 1
                return producto
        print(f"Producto {producto_nombre} no encontrado.")

    def producto_mas_rentable(self):
        if not self.productos:
            return None
        return max(self.productos, key=lambda p: p.calcular_rentabilidad()).nombre

    def reporte_ventas(self):
        return f"Ventas del día: {self.ventas_diarias} productos vendidos."

#Punto 12 | Vender

class Heladeria:
    def __init__(self):
        self.productos = []  
        self.ingredientes = []  
        self.ventas_diarias = 0

    def agregar_producto(self, producto):
        if len(self.productos) < 4:
            self.productos.append(producto)
        else:
            print("No se pueden agregar más de 4 productos a la heladería.")

    def agregar_ingrediente(self, ingrediente):
        self.ingredientes.append(ingrediente) 

    def vender(self, nombre_producto):
        producto = None

        # Verificar que el producto esté disponible
        for prod in self.productos:
            if prod.nombre == nombre_producto:
                producto = prod
                break

        if not producto:
            print(f"Producto {nombre_producto} no encontrado.")

        # Verificar existencias de ingredientes
        for ingrediente in producto.ingredientes:
            if isinstance(ingrediente, Base):
                if ingrediente.inventario < 0.2:  
                    print(f"No hay suficiente inventario para la base: {ingrediente.nombre}")
            else:
                if ingrediente.inventario < 1:  
                    print(f"No hay suficiente inventario para el complemento: {ingrediente.nombre}")

        # Restar los ingredientes
        for ingrediente in producto.ingredientes:
            if isinstance(ingrediente, Base):
                ingrediente.inventario -= 0.2  
            else:
                ingrediente.inventario -= 1  

        # Sumar el precio del producto a las ventas del día
        self.ventas_diarias += producto.precio_publico
        return True

