from Reservas.Habitaciones.habitacion import Habitacion
class Builder_habitacion():
    def __init__(self) -> None:
        self.__habitacion = Habitacion()
    
    def get_habitacion(self):
        return self.__habitacion
    def set_habitacion(self,h):
        self.__habitacion = h
    habitacion = property(get_habitacion,set_habitacion)
    
    def reset(self):
        self.habitacion = Habitacion()
    
    def set_id(self,id):
        self.habitacion.set_id(id)
    def set_max_ocupantes(self,max):
        self.habitacion.set_cant_maxima_ocupantes(max)
    def set_libre(self,l):
        self.habitacion.set_libre(l)
    def set_categoria(self,c):
        self.habitacion.set_categoria(c)
    def set_regimen(self,r):
        self.habitacion.set_regimen(r)
    def set_precio(self,p):
        self.habitacion.set_precio(p)
        
    