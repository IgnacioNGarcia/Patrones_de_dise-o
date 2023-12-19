class Director_regimen():
    def __init__(self) -> None:
        self.__builder = None
    
    def get_builder(self):
        return self.__builder
    def set_builder(self,b):
        self.__builder = b
    builder = property(get_builder,set_builder)
    
    def crear_SA(self):
        self.builder.reset()
        self.builder.set_nombre("SA")
        self.builder.set_porcentaje(0)
    
    def crear_MP(self):
        self.builder.reset()
        self.builder.set_nombre("MP")
        self.builder.set_porcentaje(25)
    
    def crear_PC(self):
        self.builder.reset()
        self.builder.set_nombre("PC")
        self.builder.set_porcentaje(75)