
class Producto:
    def __init__(self):
        self.productos = {
        1: {"Nombre": "Manzana","cantidad": 20, "precio_por_kilo": 3500},
        2: {"Nombre": "Banana","cantidad": 30, "precio_por_kilo": 2800},
        3: {"Nombre": "Naranja","cantidad": 25, "precio_por_kilo": 3000},
        4: {"Nombre": "Pera","cantidad": 18, "precio_por_kilo": 4200},
        5: {"Nombre": "Uva","cantidad": 15, "precio_por_kilo": 6500},
        6: {"Nombre": "Sandía","cantidad": 10, "precio_por_kilo": 1800},
        7: {"Nombre": "Melón","cantidad": 12, "precio_por_kilo": 2500},
        8: {"Nombre": "Piña","cantidad": 8, "precio_por_kilo": 3800},
        9: {"Nombre": "Mango","cantidad": 20, "precio_por_kilo": 5000},
        10: {"Nombre": "Papaya","cantidad": 10, "precio_por_kilo": 2900},
        11: {"Nombre": "Tomate","cantidad": 25, "precio_por_kilo": 2200},
        12: {"Nombre": "Zanahoria","cantidad": 30, "precio_por_kilo": 1900},
        13: {"Nombre": "Papa","cantidad": 50, "precio_por_kilo": 1500},
        14: {"Nombre": "Cebolla","cantidad": 40, "precio_por_kilo": 2000},
        15: {"Nombre": "Lechuga","cantidad": 20, "precio_por_kilo": 1200}
    }

    histotico_ventas=[]

    def consultar_inventario(self):
        return [(clave, producto["Nombre"], producto["cantidad"], producto["precio_por_kilo"])
                for clave, producto in self.productos.items()]

    def consultar_productos(self):
        return [(clave, producto["Nombre"])
                for clave, producto in self.productos.items()]

    def __iter__(self):
        return iter(self.productos.items())
    
    def agregar_historico():
        pass

    def actualizar_stock():
        pass

    


