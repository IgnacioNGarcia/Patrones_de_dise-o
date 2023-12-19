from abc import ABC, abstractmethod
class Temporada(ABC):
    def __init__(self) -> None:
        super().__init__()
    
    @abstractmethod
    def get_precio(self, reserva):
        pass
    @abstractmethod
    def get_tipo(self):
        pass
    