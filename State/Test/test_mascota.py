from unittest import TestCase
from unittest.mock import Mock, patch, MagicMock
from State.Clases.mascota import Mascota
from State.Estados.aburrida import Aburrida
from State.Estados.contenta import Contenta
from State.Estados.hambrienta import Hambrienta
from State.Clases.exception_hambrienta import Hambrienta_Exception

class test_mascota(TestCase):
    def test_mascota_feliz(self):
        contenta = Contenta()
        mascota = Mascota("Gero", 10, 15,contenta,10)
        mascota.comer()
        assert mascota.get_nivel() == 16
        mascota.jugar()
        assert mascota.get_nivel() == 18
    
    def test_mascota_hambrienta(self):
        hambrienta = Hambrienta()
        mascota = Mascota("Gero", 10, 15,hambrienta,10)
        mascota.comer()
        assert isinstance(mascota.estado, Contenta)
    
    def test_mascota_hambrienta2(self):
        with self.assertRaises(Hambrienta_Exception):
            hambrienta = Hambrienta()
            mascota = Mascota("Gero", 10, 15,hambrienta,90)
            mascota.jugar()
            assert  not isinstance(mascota.estado, Contenta)
    
    def test_mascota_aburrida(self):
        aburrida = Aburrida()
        mascota = Mascota("Gero", 10, 15,aburrida,90)
        mascota.comer()
        assert isinstance(mascota.estado, Contenta)
        
    def test_mascota_aburrida2(self):
        aburrida = Aburrida()
        mascota = Mascota("Gero", 10, 15,aburrida,70)
        mascota.comer()
        assert not isinstance(mascota.estado, Contenta)
    
    def test_mascota_aburrida3(self):
        
        aburrida = Aburrida()
        mascota = Mascota("Gero", 10, 15,aburrida,70)
        mascota.jugar()
        assert isinstance(mascota.estado, Contenta)
