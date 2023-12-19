from Builder.Builder.builder_abstracto import Builder
from Builder.Clases.tipo import Tipo
class Director_creacion():
    def __init__(self, builder :Builder) -> None:
        self.__builder = builder
    
    def get_builder(self):
        return self.__builder
    def set_builder(self,b):
        self.__builder = b
    builder = property(get_builder,set_builder)
    '''
    def crear_robot_ataque(self):
        self.get_builder().reset()
        self.get_builder().set_tipo(Tipo.Ataque)
        self.get_builder().set_arma("Navaja")
        self.get_builder().set_modelo(2023)
        self.get_builder().set_velocidad(100)
        self.get_builder().set_vida(500)
    def crear_robot_tanque(self):
        self.get_builder().reset()
        self.get_builder().set_tipo(Tipo.Tanque)
        self.get_builder().set_arma("Escudo")
        self.get_builder().set_modelo(2024)
        self.get_builder().set_velocidad(5)
        self.get_builder().set_vida(1000)
    
    '''

    def crear_robot(self):
        self.get_builder().reset()
        self.get_builder().set_tipo()
        self.get_builder().set_arma()
        self.get_builder().set_modelo()
        self.get_builder().set_velocidad()
        self.get_builder().set_vida()
        
        