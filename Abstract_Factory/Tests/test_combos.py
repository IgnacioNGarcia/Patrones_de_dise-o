from unittest import TestCase
from unittest.mock import Mock, patch, MagicMock
from Abstract_Factory.Factoria.factoria_starter import Factoria_starter
from Abstract_Factory.Factoria.factoria_gold import Factoria_gold


class test_combos(TestCase):
    def test_precio_combo_starter(self):
        factoria = Factoria_starter()
        combo = factoria.crear_combo()
        
        assert combo.precio_combo() == 650
    def test_precio_combo_gold(self):
        factoria = Factoria_gold()
        combo = factoria.crear_combo()
        
        assert combo.precio_combo() == 1700
'''

    def test_precio_combo_platinum(self):
        factoria = Factoria_platinum()
        combo = factoria.create_combo()
        
        assert combo.precio_combo() == 3000
'''