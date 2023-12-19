from abc import ABC, abstractmethod
class producto(ABC):
    def __init__(self) -> None:
        super().__init__()
    
    @abstractmethod
    def mostrar_producto(self):
        pass
    @abstractmethod
    def get_precio(self):
        pass
    