from abc import ABC, abstractmethod
class Webcam(ABC):
    def __init__(self) -> None:
        super().__init__()
    
    def mostrar_producto(self):
        pass
    def captar_imagen(self):
        pass