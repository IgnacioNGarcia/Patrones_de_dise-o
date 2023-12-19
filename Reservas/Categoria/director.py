from Reservas.Categoria.builder import Builder_categoria
class Director_categoria():
    def __init__(self) -> None:
        self.__builder = None
    
    def get_builder(self):
        return self.__builder
    def set_builder(self,b):
        self.__builder = b
    builder = property(get_builder,set_builder)
    
    def crear_categoria_simple(self):
        self.builder.reset()
        self.builder.set_nombre("Simple")
        self.builder.set_precio(100)
    
    def crear_categoria_doble(self):
        self.builder.reset()
        self.builder.set_nombre("Doble")
        self.builder.set_precio(250)
        
    def crear_categoria_suite(self):
        self.builder.reset()
        self.builder.set_nombre("Suite")
        self.builder.set_precio(500)
        
        