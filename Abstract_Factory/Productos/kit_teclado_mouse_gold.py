from Abstract_Factory.Productos.kit_teclado_mouse import Kit_teclado_mouse

class Kit_teclado_mouse_gold(Kit_teclado_mouse):
    def __init__(self, modelo, precio) -> None:
        self.__modelo = modelo
        self.__precio = precio
        
    def get_modelo(self):
        return self.__modelo
    def set_modelo(self,m):
        self.__modelo = m
    modelo = property(get_modelo,set_modelo)
    
    def get_precio(self):
        return self.__precio
    def set_precio(self, p):
        self.__precio = p
    precio = property(get_precio,set_precio)
    
    def mostrar_producto(self):
        print(f"Kit Gold: {self.modelo} - Precio: ${self.precio}")
    def conectar(self):
        return super().conectar()
    