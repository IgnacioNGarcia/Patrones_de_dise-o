from abc import ABC, abstractmethod
from State.Clases.mascota import Mascota
class Estado(ABC):
    def __init__(self) -> None:
        self.__mascota = None
    
    def get_mascota(self):
        return self.__mascota
    def set_mascota(self,m):
        self.__mascota = m
    mascota = property(get_mascota,set_mascota)
    
    @abstractmethod
    def puede_jugar(self):
        pass
    @abstractmethod
    def jugar(self):
        pass
    @abstractmethod
    def comer(self):
        pass