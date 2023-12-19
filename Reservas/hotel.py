from Reservas.Habitaciones.habitacion import Habitacion
from Reservas.reserva import Reserva
from Reservas.Temporada.temporada import Temporada
from Reservas.fecha_ocupada_exception import Fecha_tomada_exception
from datetime import datetime

class Hotel():
    def __init__(self) -> None:
        self.__habitaciones :Habitacion= []
        self.__reservas :Reserva = []
        self.__temporada :Temporada = None
    
    def get_habitaciones(self):
        return self.__habitaciones
    def set_habitaciones(self,h):
        self.__habitaciones = h
    habitaciones = property(get_habitaciones,set_habitaciones)
    
    def get_reservas(self):
        return self.__reservas
    def set_reservas(self,r):
        self.__reservas = r
    reservas = property(get_reservas,set_reservas)
    
    def get_temporada(self):
        return self.__temporada
    def set_temporada(self,t):
        self.__temporada = t
    temporada = property(get_temporada,set_temporada)
    
    def agregar_habitacion(self, h):
        self.habitaciones.append(h)
    
    def listar_habitaciones(self):
        for habitacion in self.habitacion:
            habitacion.mostrar_datos()
    
    def listar_habitaciones_disponibles(self):
        for habitacion in self.habitacion:
            if habitacion.get_disponible():
                habitacion.mostrar_datos()
    
    def establecer_temporada(self,t):
        self.set_temporada(t)
    
    def verificar_superposicion(self,nueva_reserva):
        nueva_fecha_ing = nueva_reserva.get_fecha_ing()
        nueva_fecha_egr = nueva_reserva.get_fecha_egr()

        for reserva in self.get_reservas():
            if (
                (nueva_fecha_ing >= reserva.fecha_ing and nueva_fecha_ing < reserva.fecha_egr) or
                (nueva_fecha_egr > reserva.fecha_ing and nueva_fecha_egr <= reserva.fecha_egr)
            ):
                # Hay superposición
                raise Fecha_tomada_exception


        # No hay superposición
        return False
    
    def agregar_reserva(self, reserva):
        if not self.verificar_superposicion(reserva):
            self.reservas.append(reserva)

