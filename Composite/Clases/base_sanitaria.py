from abc import ABC, abstractmethod
class Base_sanitaria(ABC):
    def __init__(self) -> None:
        super().__init__()
    
    @abstractmethod
    def get_cantidad_ambulancias(self):
        pass
    @abstractmethod
    def get_tiempo_promedio(self):
        pass
    @abstractmethod
    def mostrar_informacion_base(self):
        pass