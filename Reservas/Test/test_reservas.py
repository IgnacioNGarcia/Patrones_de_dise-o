from datetime import datetime
from unittest import TestCase
from unittest.mock import Mock, patch, MagicMock

from Reservas.Categoria.builder import Builder_categoria
from Reservas.Categoria.director import Director_categoria
from Reservas.Categoria.categoria import Categoria

from Reservas.Regimen.builder import Builder_regimen
from Reservas.Regimen.director import Director_regimen
from Reservas.Regimen.regimen import Regimen

from Reservas.Habitaciones.builder import Builder_habitacion
from Reservas.Habitaciones.director import Director_habitacion
from Reservas.Habitaciones.habitacion import Habitacion

from Reservas.reserva import Reserva
from Reservas.cliente import Cliente
from Reservas.Temporada.alta import Alta
from Reservas.Temporada.baja import Baja

from Reservas.hotel import Hotel
from Reservas.fecha_ocupada_exception import Fecha_tomada_exception

class test_reservas(TestCase):
    def test_categoria_1(self):
        builder = Builder_categoria()
        dir = Director_categoria()
        dir.set_builder(builder)
        dir.crear_categoria_simple()
        cat = builder.get_categoria()
        
        assert cat.get_precio() == 100
        assert cat.get_nombre() == "Simple"
    
    def test_categoria_2(self):
        builder = Builder_categoria()
        dir = Director_categoria()
        dir.set_builder(builder)
        dir.crear_categoria_doble()
        cat = builder.get_categoria()
        
        assert cat.get_precio() == 250
        assert cat.get_nombre() == "Doble"
    
    def test_categoria_3(self):
        builder = Builder_categoria()
        dir = Director_categoria()
        dir.set_builder(builder)
        dir.crear_categoria_suite()
        cat = builder.get_categoria()
        
        assert cat.get_precio() == 500
        assert cat.get_nombre() == "Suite"

    
    def test_regimen_1(self):
        builder = Builder_regimen()
        dir = Director_regimen()
        dir.set_builder(builder)
        dir.crear_SA()
        reg = builder.get_regimen()
        
        assert reg.get_porcentaje() == 0
        assert reg.get_nombre() == "SA"
    
    def test_regimen_2(self):
        builder = Builder_regimen()
        dir = Director_regimen()
        dir.set_builder(builder)
        dir.crear_MP()
        reg = builder.get_regimen()
        
        assert reg.get_porcentaje() == 25
        assert reg.get_nombre() == "MP"
    
    def test_regimen_3(self):
        builder = Builder_regimen()
        dir = Director_regimen()
        dir.set_builder(builder)
        dir.crear_PC()
        reg = builder.get_regimen()
        
        assert reg.get_porcentaje() == 75
        assert reg.get_nombre() == "PC"
    
    def test_habitacion1(self):
        builder = Builder_habitacion()
        dir = Director_habitacion()
        dir.set_builder(builder)
        dir.crear_habitacion_simple(10,180)
        habitacion = builder.get_habitacion()
        
        assert habitacion.get_id() == 180
        assert habitacion.get_cant_maxima_ocupantes() == 10
        assert habitacion.get_categoria().get_nombre() == "Simple"
        assert habitacion.get_categoria().get_precio() == 100
    
    def test_habitacion2(self):
        builder = Builder_habitacion()
        dir = Director_habitacion()
        dir.set_builder(builder)
        dir.crear_habitacion_doble(10,180)
        habitacion = builder.get_habitacion()
        
        assert habitacion.get_id() == 180
        assert habitacion.get_cant_maxima_ocupantes() == 10
        assert habitacion.get_categoria().get_nombre() == "Doble"
        assert habitacion.get_categoria().get_precio() == 250

    def test_habitacion3(self):
        builder = Builder_habitacion()
        dir = Director_habitacion()
        dir.set_builder(builder)
        dir.crear_habitacion_suite(10,180)
        habitacion = builder.get_habitacion()
        
        assert habitacion.get_id() == 180
        assert habitacion.get_cant_maxima_ocupantes() == 10
        assert habitacion.get_categoria().get_nombre() == "Suite"
        assert habitacion.get_categoria().get_precio() == 500
    
    def test_habitacion_regimen1(self):
        builder_regimen = Builder_regimen()
        dir_regimen = Director_regimen()
        dir_regimen.set_builder(builder_regimen)
        dir_regimen.crear_SA()
        reg = builder_regimen.get_regimen()
        
        builder_hab = Builder_habitacion()
        dir_h = Director_habitacion()
        dir_h.set_builder(builder_hab)
        dir_h.crear_habitacion_suite(10,180)
        habitacion = builder_hab.get_habitacion()
        
        habitacion.agregar_regimen_disponible(reg)
        
        
        assert reg in habitacion.get_regimen()
        
        dir_regimen.crear_PC()
        reg2 = builder_regimen.get_regimen()
        habitacion.agregar_regimen_disponible(reg2)
        assert reg2 in habitacion.get_regimen()


        
    def test_reserva_1(self):
        builder_regimen = Builder_regimen()
        dir_regimen = Director_regimen()
        dir_regimen.set_builder(builder_regimen)
        dir_regimen.crear_SA()
        reg = builder_regimen.get_regimen()
        
        builder_hab = Builder_habitacion()
        dir_h = Director_habitacion()
        dir_h.set_builder(builder_hab)
        dir_h.crear_habitacion_suite(10,180)
        habitacion = builder_hab.get_habitacion()
        
        dir_regimen.crear_PC()
        reg2 = builder_regimen.get_regimen()
        
        habitacion.agregar_regimen_disponible(reg)
        dir_h.crear_habitacion_doble(2,150)
        habitacion_2 = builder_hab.get_habitacion()
        temporada = Alta()
        
        cliente = Cliente("Nacho", 41047964,"ignacio1garcia@gmail.com")
        reserva = Reserva("18/12/2023","20/12/2023",cliente,2,temporada)
        reserva.agregar_habitacion(habitacion,reg)
        reserva.agregar_habitacion(habitacion_2,reg2)
        
        assert len(reserva.get_habitaciones()) == 2
            
    def test_reserva_2(self):
        builder_regimen = Builder_regimen()
        dir_regimen = Director_regimen()
        dir_regimen.set_builder(builder_regimen)
        dir_regimen.crear_SA()
        reg = builder_regimen.get_regimen()
        
        builder_hab = Builder_habitacion()
        dir_h = Director_habitacion()
        dir_h.set_builder(builder_hab)
        dir_h.crear_habitacion_suite(10,180)
        habitacion = builder_hab.get_habitacion()
        habitacion.agregar_regimen_disponible(reg)
        
        temporada = Baja()
        cliente = Cliente("Nacho", 41047964,"ignacio1garcia@gmail.com")
        reserva = Reserva("18/12/2023","20/12/2023",cliente,2,temporada)
        reserva.agregar_habitacion(habitacion,reg)
        
        assert len(reserva.get_habitaciones()) == 1
        
        assert reserva.get_precio() == 550 
        'Tenemos una Suite de 500 X un día en temporada baja que suma 0.1'
        
        dir_h.crear_habitacion_doble(2,199)
        hab2 = builder_hab.get_habitacion()
        dir_regimen.crear_PC()
        reg2 = builder_regimen.get_regimen()
        
        hab2.agregar_regimen_disponible(hab2)
        
        reserva.agregar_habitacion(hab2,reg2)
        
        assert reserva.get_precio() == 1031.25
    
    def test_reserva_2(self):
        builder_regimen = Builder_regimen()
        dir_regimen = Director_regimen()
        dir_regimen.set_builder(builder_regimen)
        dir_regimen.crear_SA()
        reg = builder_regimen.get_regimen()
        
        builder_hab = Builder_habitacion()
        dir_h = Director_habitacion()
        dir_h.set_builder(builder_hab)
        dir_h.crear_habitacion_suite(10,180)
        habitacion = builder_hab.get_habitacion()
        habitacion.agregar_regimen_disponible(reg)
        
        temporada = Baja()
        cliente = Cliente("Nacho", 41047964,"ignacio1garcia@gmail.com")
        reserva = Reserva(datetime(2023, 1, 1), datetime(2023, 1, 10),cliente,2,temporada)
        reserva.agregar_habitacion(habitacion,reg)
        
        hotel = Hotel()
        with self.assertRaises(Fecha_tomada_exception):
            hotel.agregar_reserva(reserva)
            assert len(hotel.reservas) == 1
            hotel.agregar_reserva(reserva)
            


