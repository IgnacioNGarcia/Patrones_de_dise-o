from datetime import datetime, timedelta

from Observer.Clases.subscriber import Subscriber
class Destino(Subscriber):
    def __init__(self, nombre, dif_horas) -> None:
        self.__nombre = nombre
        self.__dif_horas = dif_horas
        self.__hora_final :datetime = None
    
    def get_nombre(self):
        return self.__nombre
    def set_nombre(self,n):
        self.__nombre = n
    nombre = property(get_nombre,set_nombre)
    
    def get_dif_horas(self):
        return self.__dif_horas
    def set_dif_horas(self,d):
        self.__dif_horas = d
    dif_horas = property(get_dif_horas,set_dif_horas)
    
    def get_hora_final(self):
        return self.__hora_final
    def set_hora_final(self,h):
        self.__hora_final = h
    hora_final = property(get_hora_final,set_hora_final)
    
    def update(self,fecha_hora):
        self.set_hora_final(fecha_hora + timedelta(hours=self.dif_horas))
        
    def mostrar_info(self):
        print(f"{self.nombre} ({self.dif_horas})")
        print(f"{self.hora_final}")