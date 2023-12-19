class Regimen():
    def __init__(self) -> None:
        self.__nombre = None
        self.__porcentaje = None
    def get_nombre(self):
        return self.__nombre
    def set_nombre(self,n):
        self.__nombre = n
    nombre = property(get_nombre,set_nombre)
    
    def get_porcentaje(self):
        return self.__porcentaje
    def set_porcentaje(self,p):
        self.__porcentaje = p
    porcentaje = property(get_porcentaje,set_porcentaje)
    
    def calcular_valor(self):
        pass