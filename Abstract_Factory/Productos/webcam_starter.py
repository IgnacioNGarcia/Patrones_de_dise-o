from Abstract_Factory.Productos.webcam import Webcam

class Webcam_starter(Webcam):
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
    
    def captar_imagen(self):
        return super().captar_imagen()
    def mostrar_producto(self):
        print(f"Webcam Starter: {self.modelo} - Precio: ${self.precio}")
    