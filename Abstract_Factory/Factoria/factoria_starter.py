from Abstract_Factory.Factoria.factoria_abstracta import Factoria_abstracta
from Abstract_Factory.Productos.headset_starter import Headset_starter
from Abstract_Factory.Productos.kit_teclado_mouse_starter import Kit_teclado_mouse_starter
from Abstract_Factory.Productos.webcam_starter import Webcam_starter
from Abstract_Factory.Factoria.combo import Combo
class Factoria_starter(Factoria_abstracta):
    def __init__(self) -> None:
        super().__init__()
    
    def crear_combo(self):
        w = Webcam_starter("Razer", 300)
        h = Headset_starter("HDR", 100)
        k = Kit_teclado_mouse_starter("Pentium", 250)
        
        combo = Combo(h,w,k)
        return combo