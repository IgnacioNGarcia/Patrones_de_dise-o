from StateV2.Estados.estado import Estado
from StateV2.Clases.mascota import Mascota
from StateV2.Estados.contenta import Contenta

class Aburrida(Estado):
    def __init__(self) -> None:
        super().__init__()
    
    def puede_jugar(self):
        return True
    
    def comer(self):
        if self.mascota.get_tiempo_aburrida() > 80:
            nuevo_estado = Contenta()
            nuevo_estado.set_mascota(self.mascota)

            self.mascota.set_estado(nuevo_estado)
        else:
            print("Sin cambios :/ ")
         
    def jugar(self):
            nuevo_estado = Contenta()
            nuevo_estado.set_mascota(self.mascota)
            self.mascota.set_estado(nuevo_estado)
