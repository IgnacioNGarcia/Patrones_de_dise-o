from abc import ABC, abstractmethod

class Creador_abstracto(ABC):
    def __init__(self) -> None:
        super().__init__()
    @abstractmethod
    def crear_producto(self):
        pass