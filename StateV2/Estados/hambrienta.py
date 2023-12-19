from StateV2.Estados.estado import Estado
from StateV2.Clases.mascota import Mascota
from StateV2.Estados.contenta import Contenta
from StateV2.Clases.exception_hambrienta import Hambrienta_Exception
class Hambrienta(Estado):
    def __init__(self) -> None:
        super().__init__()
    
    def puede_jugar(self):
        raise Hambrienta_Exception("Tenemos HAMBREEEE")
    
    def comer(self):
        nuevo_estado = Contenta()
        nuevo_estado.set_mascota(self.mascota)
        self.mascota.set_estado(nuevo_estado)
        
         
    def jugar(self):
        raise Hambrienta_Exception("Tenemos HAMBREEEE")
    