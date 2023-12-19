from unittest import TestCase
from unittest.mock import Mock, patch, MagicMock
from Builder.Builder.builder_robots import Builder_robot
from Builder.Director.direc import Director_creacion
from Builder.Clases.robot import Robot
from Builder.Builder.builder_robot_ataque import Builder_robot_ataque
from Builder.Builder.builder_robot_tanque import Builder_robot_tanque
from Builder.Clases.not_a_tipe_exception import Not_A_robot_type_Exception
from Builder.Clases.tipo import Tipo
class test_robots(TestCase):

    def test_robot_ataque(self):
        builder = Builder_robot_ataque()
        dir = Director_creacion(builder)
        dir.crear_robot()
        robot = builder.get_robot()
        assert robot.get_vida() == 500
        assert robot.get_arma() == "Espada"
        assert robot.get_tipo() == Tipo.Ataque


    def test_robot_tanque(self):
        builder = Builder_robot_tanque()
        dir = Director_creacion(builder)
        dir.crear_robot()
        robot = builder.get_robot()
        assert robot.get_vida() == 1000
   
    def test_exception(self):
        tipo = "Luchador"
        with self.assertRaises(Not_A_robot_type_Exception):
            if tipo == Tipo.Ataque:
                builder = Builder_robot_ataque()
            elif tipo == Tipo.Tanque:
                    builder = Builder_robot_tanque()
            else:
                raise Not_A_robot_type_Exception("Robot invalido")
            
            dir = Director_creacion(builder)    
            dir.crear_robot()
           
       