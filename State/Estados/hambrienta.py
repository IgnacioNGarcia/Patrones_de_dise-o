from State.Estados.estado import Estado
from State.Clases.mascota import Mascota
from State.Estados.contenta import Contenta
from State.Clases.exception_hambrienta import Hambrienta_Exception
class Hambrienta(Estado):
    def __init__(self) -> None:
        super().__init__()
    
    def puede_jugar(self, mascota):
        raise Hambrienta_Exception("Tenemos HAMBREEEE")
    
    def comer(self, mascota):
        nuevo_estado = Contenta()
        nuevo_estado.set_mascota(mascota)
        mascota.set_estado(nuevo_estado)
        
         
    def jugar(self, mascota):
        raise Hambrienta_Exception("Tenemos HAMBREEEE")
    