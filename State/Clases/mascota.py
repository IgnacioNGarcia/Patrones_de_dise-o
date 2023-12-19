class Mascota():
    def __init__(self, nombre, nivel_felicidad, nivel_mascota, estado, tiempo_aburrida) -> None:
        self.__nombre = nombre,
        self.__nivel_felicidad = nivel_felicidad
        self.__nivel = nivel_mascota
        self.__estado = estado
        self.__tiempo_aburrida = tiempo_aburrida
        
    def get_nombre(self):
        return self.__nombre
    def set_nombre(self,n):
        self.__nombre = n
    nombre = property(get_nombre,set_nombre)
    
    def get_nivel_felicidad(self):
        return self.__nivel_felicidad
    def set_felicidad(self,f):
        self.__nivel_felicidad = f
    nivel_felicidad = property(get_nivel_felicidad,set_felicidad)
    
    def get_nivel(self):
        return self.__nivel
    def set_nivel(self,n):
        self.__nivel = n
    nivel = property(get_nivel,set_nivel)
    
    def get_estado(self):
        return self.__estado
    def set_estado(self,e):
        self.__estado = e
    estado = property(get_estado,set_estado)
    
    def get_tiempo_aburrida(self):
        return self.__tiempo_aburrida
    def set_tiempo_aburrida(self,t):
        self.__tiempo_aburrida = t
    tiempo_aburrida = property(get_tiempo_aburrida,set_tiempo_aburrida)
    
    def comer(self):
        self.estado.comer(self)
        
    def jugar(self):
        self.estado.jugar(self)