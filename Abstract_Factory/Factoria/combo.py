from Abstract_Factory.Productos.headset import Headset
from Abstract_Factory.Productos.webcam import Webcam
from Abstract_Factory.Productos.kit_teclado_mouse import Kit_teclado_mouse

class Combo():
    def __init__(self, h : Headset, w : Webcam, k : Kit_teclado_mouse) -> None:
        self.__headset = h
        self.__webcam = w
        self.__kit = k
    
    def get_headset(self):
        return self.__headset
    def set_headset(self, h):
        self.__headset = h
    headset = property(get_headset,set_headset)
    
    def get_webcam(self):
        return self.__webcam
    def set_webcam(self, w):
        self.__headset = w
    webcam = property(get_webcam,set_webcam)
    
    def get_kit(self):
        return self.__kit
    def set_kit(self, k):
        self.__headset = k
    kit = property(get_kit,set_kit)
    
    def mostrar_combo(self):
        print(f"Combo: \n {self.get_headset().mostrar_producto()}\n {self.get_webcam().mostrar_producto()}\n {self.get_kit().mostrar_producto()}")
    def precio_combo(self):
        return (self.get_headset().get_precio() + self.get_kit().get_precio() + self.get_webcam().get_precio())
    
    
    
    