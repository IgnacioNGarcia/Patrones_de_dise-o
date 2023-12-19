from Factory_Method.Factoria.Creador import Creador_abstracto
from Factory_Method.Producto.mesa import Mesa
class Fabrica_mesas(Creador_abstracto):
    def __init__(self) -> None:
        super().__init__()
    
    def crear_producto(self):
        m = Mesa(1000,"Madera","Circular")
        return m
