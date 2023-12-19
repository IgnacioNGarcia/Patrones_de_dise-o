from abc import ABC, abstractmethod
class Headset(ABC):
    def __init__(self) -> None:
        super().__init__()
    
    @abstractmethod
    def escuchar_musica(self):
        pass
    
    @abstractmethod
    def mostrar_producto(self):
        pass