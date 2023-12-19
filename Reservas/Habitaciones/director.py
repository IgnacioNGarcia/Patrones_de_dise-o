from Reservas.Habitaciones.builder import Builder_habitacion
from Reservas.Categoria.builder import Builder_categoria
from Reservas.Categoria.director import Director_categoria
class Director_habitacion():
    def __init__(self) -> None:
        self.__builder :Builder_habitacion = None 
    
    def get_builder(self):
        return self.__builder
    def set_builder(self,b):
        self.__builder = b
    builder = property(get_builder,set_builder)
    
    def crear_habitacion(self,ocupantes,id):
        self.get_builder().reset()
        self.builder.set_max_ocupantes(ocupantes)
        self.builder.set_id(id)
        self.builder.set_libre(True)
    
    def crear_habitacion_simple(self, ocupantes, id):
        builder = Builder_categoria()
        dir = Director_categoria()
        dir.set_builder(builder)
        dir.crear_categoria_simple()
        cat = builder.get_categoria()
        self.crear_habitacion(ocupantes,id)
        self.builder.set_categoria(cat)
    
    def crear_habitacion_doble(self, ocupantes, id):
        builder = Builder_categoria()
        dir = Director_categoria()
        dir.set_builder(builder)
        dir.crear_categoria_doble()
        cat = builder.get_categoria()
        self.crear_habitacion(ocupantes,id)
        self.builder.set_categoria(cat)
    
    def crear_habitacion_suite(self, ocupantes, id):
        builder = Builder_categoria()
        dir = Director_categoria()
        dir.set_builder(builder)
        dir.crear_categoria_suite()
        cat = builder.get_categoria()
        self.crear_habitacion(ocupantes,id)
        self.builder.set_categoria(cat)
