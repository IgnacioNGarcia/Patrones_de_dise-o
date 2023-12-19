from State.Clases.mascota import Mascota
from State.Estados.estado import Estado

class Contenta(Estado):
    def __init__(self) -> None:
        super().__init__()
    
    def puede_jugar(self):
        return True
    
    def comer(self, mascota):
        mascota.set_nivel(mascota.get_nivel() + 1)    
    def jugar(self, mascota):
        mascota.set_nivel(mascota.get_nivel() + 2)