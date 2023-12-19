from unittest import TestCase
from unittest.mock import Mock, patch, MagicMock
from Factory_Method.Producto.prod import producto
from Factory_Method.Producto.silla import Silla
from Factory_Method.Producto.mesa import Mesa

from Factory_Method.Factoria.Creador_sillas import Fabrica_sillas
from Factory_Method.Factoria.Creador_mesas import Fabrica_mesas


class test_muebleria(TestCase):
    def test_silla(self):
        c = Fabrica_sillas()
        silla = c.crear_producto()
        assert isinstance(silla,Silla) == True
    
    def test_silla_precio(self):
        c = Fabrica_sillas()
        silla = c.crear_producto()
        assert silla.get_precio() == 500
    
    def test_mesa(self):
        c = Fabrica_mesas()
        mesa = c.crear_producto()
        assert isinstance(mesa, Mesa) == True
    
    def test_mesa_precio(self):
        c = Fabrica_mesas()
        mesa = c.crear_producto()
        assert mesa.get_precio() == 1000
    
    def test_producto_abstracto(self):
        c = Fabrica_mesas()
        mesa = c.crear_producto()
        assert isinstance(mesa, producto)
        
    def test_producto_abstracto2(self):
        c = Fabrica_sillas()
        silla = c.crear_producto()
        assert isinstance(silla, producto)
    