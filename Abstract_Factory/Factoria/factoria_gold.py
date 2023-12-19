from Abstract_Factory.Factoria.factoria_abstracta import Factoria_abstracta
from Abstract_Factory.Productos.headset_gold import Headset_gold
from Abstract_Factory.Productos.kit_teclado_mouse_gold import Kit_teclado_mouse_gold
from Abstract_Factory.Productos.webcam_gold import Webcam_gold
from Abstract_Factory.Factoria.combo import Combo
class Factoria_gold(Factoria_abstracta):
    def __init__(self) -> None:
        super().__init__()
    
    def crear_combo(self):
        w = Webcam_gold("Razon", 800)
        k = Kit_teclado_mouse_gold("Pei", 550)
        h = Headset_gold("asda", 350)
        combo = Combo(h,w,k)
        return combo