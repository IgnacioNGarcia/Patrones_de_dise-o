from Factory_Method.Producto.prod import producto
class Mesa(producto):
    def __init__(self, precio, material, forma) -> None:
        self.__precio = precio
        self.__material = material
        self.__forma = forma
    def get_precio(self):
        return self.__precio
    def set_precio(self, p):
        self.__precio = p
    precio = property(get_precio,set_precio)
    
    def get_material(self):
        return self.__material
    def set_material(self, m):
        self.__material = m
    material = property(get_material,set_material)
    
    def get_forma(self):
        return self.__forma
    def set_forma(self, m):
        self.__forma = m
    forma = property(get_forma,set_forma)
    
    def mostrar_producto(self):
        print(f"Mesa: Precio: ${self.precio} - Material: {self.material} - Forma: {self.forma}")