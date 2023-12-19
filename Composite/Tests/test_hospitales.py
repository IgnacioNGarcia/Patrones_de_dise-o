from unittest import TestCase
from unittest.mock import Mock, patch, MagicMock
from Composite.Clases.hospital import Hospital
from Composite.Clases.uap import Uap
from Composite.Clases.unidad_administrativa import Unidad_administrativa

class test_centros(TestCase):

    def test_hospital(self):
        hospital1 = Hospital("Dr. Bernardo Houssay","maipu",10,60)
        assert hospital1.get_cantidad_ambulancias() == 10
        hospital2 = Hospital("Hospital J.Ubaldo Carrea", "Laprida", 15,80)
        assert hospital2.get_ambulancias() == 15
        uap = Uap("Mitre Salita", "Mitre", 15)
        
        ua = Unidad_administrativa("Vicente Lopez Centro", "Avenida mitre")
        ua.add_centro(hospital1)
        ua.add_centro(hospital2)
        ua.add_centro(uap)
        assert ua.get_cantidad_ambulancias() == 25
        ua.mostrar_informacion_base() 
        assert ua.get_tiempo_promedio() == 52
        '''Hago que de mal para ver los prints y están okey. Es 52 el tiempo promedio'''
    
    def test_hospital2(self):
        hospital1 = Hospital("Dr. Bernardo Houssay","maipu",10,60)
        assert hospital1.get_cantidad_ambulancias() == 10
        hospital2 = Hospital("Hospital J.Ubaldo Carrea", "Laprida", 15,80)
        assert hospital2.get_ambulancias() == 15
        uap = Uap("Mitre Salita", "Mitre", 15)
        
        ua = Unidad_administrativa("Vicente Lopez Centro", "Avenida mitre")
        ua.add_centro(hospital1)
        ua.add_centro(hospital2)
        ua.add_centro(uap)
        
        uaGde = Unidad_administrativa("Zona Norte", "El rio e Yrigoyen")
        hospital3 = Hospital("Hospital Olivos","El rio y Roca", 35, 30)
        uaGde.add_centro(hospital3)
        uaGde.add_centro(ua)
        assert uaGde.get_cantidad_ambulancias() == 60
        uaGde.mostrar_informacion_base()
        assert uaGde.get_tiempo_promedio() == 41
        

        
       