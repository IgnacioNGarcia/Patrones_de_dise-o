from abc import ABC, abstractmethod
class Subscriber(ABC):
    def __init__(self) -> None:
        super().__init__()
    
    @abstractmethod
    def update(self,fecha_hora):
        pass
    
    @abstractmethod
    def mostrar_info(self):
        pass