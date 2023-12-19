from Builder.Builder.builder_abstracto import Builder
from Builder.Clases.robot import Robot
from Builder.Clases.tipo import Tipo
class Builder_robot_tanque(Builder):
    def __init__(self) -> None:
        self.__robot = None

    def get_robot(self):
        return self.__robot
    def set_Robot(self, r):
        self.__robot = r
        
    robot = property(get_robot,set_Robot)
        
    def reset(self):
        self.robot = Robot()
    def set_vida(self):
        self.robot.set_vida(1000)
    def set_arma(self):
        self.robot.set_arma("Escudo")
    def set_modelo(self):
        self.robot.set_modelo("2025")
    def set_velocidad(self):
        self.robot.set_velocidad(25)
    def set_tipo(self):
        self.robot.set_tipo(Tipo.Tanque)
    
    def get_result(self):
        return self.robot
    