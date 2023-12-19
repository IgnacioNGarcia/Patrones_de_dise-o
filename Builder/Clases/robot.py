from Builder.Clases.tipo import Tipo
class Robot():
    def __init__(self) -> None:
        self.__modelo = None
        self.__vida = None
        self.__arma = None
        self.__velocidad = None
        self.__tipo = None
        
    def get_modelo(self):
        return self.__modelo
    def set_modelo(self, m):
        self.__modelo = m
    modelo = property(get_modelo,set_modelo)
    
    def get_vida(self):
        return self.__vida
    def set_vida(self, v):
        self.__vida = v
    vida = property(get_vida,set_vida)
    
    def get_arma(self):
        return self.__arma
    def set_arma(self,a):
        self.__arma = a
    arma = property(get_arma,set_arma)
    
    def get_velocidad(self):
        return self.__velocidad
    def set_velocidad(self, v):
        self.__velocidad = v
    velocidad = property(get_velocidad,set_velocidad)
    
    def get_tipo(self):
        return self.__tipo
    def set_tipo(self, t):
        self.__tipo = t
    tipo = property(get_tipo,set_tipo)
    
    def mostrar_info_robot(self):
        print(f"Robot {self.tipo} - Modelo: {self.modelo} \n Vida: {self.vida} - Arma {self.arma} \n - Velocidad: {self.velocidad}")