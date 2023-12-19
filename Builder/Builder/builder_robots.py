from Builder.Builder.builder_abstracto import Builder
from Builder.Clases.robot import Robot
class Builder_robot(Builder):
    def __init__(self) -> None:
        self.__robot = None
    
    def get_robot(self):
        return self.__robot
    def set_robot(self, r):
        self.__robot = r
    robot = property(get_robot,set_robot)
    
    def set_arma(self, a):
        self.get_robot().set_arma(a)
    
    def set_modelo(self, m):
        self.get_robot().set_modelo(m)
    
    def set_tipo(self, t):
        self.get_robot().set_tipo(t)
    
    def set_velocidad(self, v):
        self.get_robot().set_velocidad(v)
        
    def set_vida(self, v):
        self.get_robot().set_vida(v)
    
    def reset(self):
        self.robot = Robot()