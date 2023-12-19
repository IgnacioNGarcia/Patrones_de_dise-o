from Reservas.Temporada.temporada import Temporada
from Reservas.reserva import Reserva
class Baja(Temporada):
    def __init__(self) -> None:
        super().__init__()
    
    def get_precio(self, reserva:Reserva):
        precio = 0
        for habitacion,regimen in reserva.get_habitaciones().items():
            precio_habitacion = habitacion.get_categoria().get_precio() 
            precio += (precio_habitacion + precio_habitacion * regimen.get_porcentaje() / 100) * reserva.get_dias() * 1.10
        return precio
    
    def get_tipo(self):
        return "Baja"
    