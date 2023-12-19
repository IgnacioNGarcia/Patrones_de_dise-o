from Reservas.cliente import Cliente
from Reservas.Habitaciones.habitacion import Habitacion
from Reservas.Regimen.regimen import Regimen
from Reservas.Temporada.temporada import Temporada
class Reserva():
    def __init__(self, fecha_ing, fecha_egr,cliente :Cliente, cant, temporada : Temporada) -> None:
        self.__fecha_ing = fecha_ing
        self.__fecha_egr = fecha_egr
        self.__cliente = cliente
        self.__precio = None
        self.__habitaciones = {}
        self.dias = 1
        '''[Clave / Habitacion] = Regimen'''

        self.__cant_ocupantes = cant
        self.__temporada = temporada
    
    def get_dias(self):
        return self.dias
    def set_dias(self, d):
        self.dias = d
    def get_temporada(self):
        return self.__temporada
    def set_temporada(self,t):
        self.__temporada = t
    temporada = property(get_temporada,set_temporada)
    
    def get_fecha_ing(self):
        return self.__fecha_ing
    def set_fecha_ing(self,f):
        self.__fecha_ing = f
    fecha_ing = property(get_fecha_ing,set_fecha_ing)
    
    def get_fecha_egr(self):
        return self.__fecha_egr
    def set_fecha_egr(self,f):
        self.__fecha_egr = f
    fecha_egr = property(get_fecha_egr,set_fecha_egr)
    
    def get_cliente(self):
        return self.__cliente
    def set_cliente(self,c):
        self.__cliente = c
    cliente = property(get_cliente,set_cliente)
    
    def get_habitaciones(self):
        return self.__habitaciones
    def set_habitaciones(self,h):
        self.__habitaciones = h
    habitaciones = property(get_habitaciones,set_habitaciones)
    
    def agregar_habitacion(self, habitacion :Habitacion, regimen:Regimen):
        self.habitaciones[habitacion] = regimen
    
    def get_precio(self):
        return self.temporada.get_precio(self)