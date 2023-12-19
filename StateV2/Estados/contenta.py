from StateV2.Clases.mascota import Mascota
from StateV2.Estados.estado import Estado

class Contenta(Estado):
    def __init__(self) -> None:
        super().__init__()
    
    def puede_jugar(self):
        return True
    
    def comer(self):
        self.mascota.set_nivel(self.mascota.get_nivel() + 1)    
    def jugar(self):
        self.mascota.set_nivel(self.mascota.get_nivel() + 2)