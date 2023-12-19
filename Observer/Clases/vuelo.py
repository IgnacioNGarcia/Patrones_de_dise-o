from Observer.Clases.subscriber import Subscriber
from datetime import datetime, timedelta

class Vuelo():
    def __init__(self, nombre, fecha_hora :datetime) -> None:
        self.__nombre = nombre
        self.__fecha_hora = fecha_hora
        self.subs :Subscriber = [] 
    
    def agregar_destino(self,d):
        self.subs.append(d)
        d.update(self.fecha_hora)
        
    def eliminar_destino(self,d):
        self.subs.remove(d)
    
    def notificar(self):
        for sub in self.subs:
            sub.update(self.__fecha_hora)
    
    def get_nombre(self):
        return self.__nombre
    def set_nombre(self,n):
        self.__nombre = n
    nombre = property(get_nombre,set_nombre)
    
    def get_fecha_hora(self):
        return self.__fecha_hora
    def set_fecha_hora(self,f):
        self.__fecha_hora = f
        self.notificar()
    fecha_hora = property(get_fecha_hora,set_fecha_hora)
    
    def get_subs(self):
        return self.subs
