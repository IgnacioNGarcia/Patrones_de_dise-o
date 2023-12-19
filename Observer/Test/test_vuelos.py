from unittest import TestCase
from unittest.mock import Mock, patch, MagicMock
from Observer.Clases.vuelo import Vuelo
from Observer.Clases.destino import Destino
from datetime import datetime, date, time
from Observer.Clases.pantalla import Pantalla

class test_vuelos(TestCase):
    def test1(self):
        v1 = Vuelo("Argentina", datetime(2023, 12, 31, 15, 30, 0))
        d1 = Destino("España", 5)
        d2 = Destino("Nueva York", -1)
        v1.agregar_destino(d1)
        v1.agregar_destino(d2)
        pantalla = Pantalla(v1)
        pantalla.mostrar_datos()
        assert d1.get_hora_final() == datetime(2023, 12, 31, 20, 30, 0)
        assert d2.get_hora_final() == datetime(2023, 12, 31, 14, 30, 0)
        
        v1.set_fecha_hora(datetime(2023, 12, 31, 20, 30, 0))
        pantalla.mostrar_datos()

        assert d1.get_hora_final() == datetime(2024, 1, 1, 1, 30, 0)
        assert d2.get_hora_final() == datetime(2023, 12, 31, 19, 30, 0)
        