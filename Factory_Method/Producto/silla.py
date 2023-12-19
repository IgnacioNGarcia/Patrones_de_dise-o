from Factory_Method.Producto.prod import producto
class Silla(producto):
    def __init__(self, precio,material,color) -> None:
        self.__precio = precio
        self.__material = material
        self.__color = color
    def get_precio(self):
        return self.__precio
    def set_precio(self, p):
        self.__precio = p
    precio = property(get_precio,set_precio)
    
    def get_material(self):
        return self.__material
    def set_material(self,m):
        self.__material = m
    material = property(get_material,set_material)
    
    def get_color(self):
        return self.__color
    def set_color(self, c):
        self.__color = c
    color = property(get_color,set_color)
    
    def mostrar_producto(self):
        print(f"Silla: ${self.precio} - Color: {self.color} - Material {self.material}")