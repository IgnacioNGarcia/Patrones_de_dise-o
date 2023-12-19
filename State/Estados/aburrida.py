from State.Estados.estado import Estado
from State.Clases.mascota import Mascota
from State.Estados.contenta import Contenta

class Aburrida(Estado):
    def __init__(self) -> None:
        super().__init__()
    
    def puede_jugar(self):
        return True
    
    def comer(self, mascota):
        if mascota.get_tiempo_aburrida() > 80:
            nuevo_estado = Contenta()
            nuevo_estado.set_mascota(mascota)

            mascota.set_estado(nuevo_estado)
        else:
            print("Sin cambios :/ ")
         
    def jugar(self, mascota):
            nuevo_estado = Contenta()
            nuevo_estado.set_mascota(mascota)
            mascota.set_estado(nuevo_estado)
