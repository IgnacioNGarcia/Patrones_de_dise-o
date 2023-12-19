from abc import ABC, abstractmethod
class Kit_teclado_mouse(ABC):
    def __init__(self) -> None:
        super().__init__()
    @abstractmethod
    def conectar(self):
        pass
    @abstractmethod
    def mostrar_producto(self):
        pass