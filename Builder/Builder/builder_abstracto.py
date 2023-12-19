from abc import ABC, abstractmethod
class Builder(ABC):
    def __init__(self) -> None:
        super().__init__()
    
    @abstractmethod
    def reset(self):
        pass
    @abstractmethod
    def set_vida(self):
        pass
    @abstractmethod
    def set_arma(self):
        pass
    @abstractmethod
    def set_modelo(self):
        pass
    @abstractmethod
    def set_velocidad(self):
        pass
    @abstractmethod
    def set_tipo(self):
        pass
    
    