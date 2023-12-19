class Habitacion():
    def __init__(self) -> None:
        self.__id = None
        self.__cant_maxima_ocupantes = None
        self.__categoria = None
        self.__regimen = set()
        self.__libre = None
    
      
    def get_id(self):
        return self.__id
    def set_id(self,i):
        self.__id = i
    id = property(get_id,set_id)
    
    def get_precio(self):
        return self.__precio
    def set_precio(self,p):
        self.__precio = p
    precio = property(get_precio,set_precio)
    
    def get_cant_maxima_ocupantes(self):
        return self.__cant_maxima_ocupantes
    def set_cant_maxima_ocupantes(self,c):
        self.__cant_maxima_ocupantes = c
    cant_maxima_ocupantes = property(get_cant_maxima_ocupantes,set_cant_maxima_ocupantes)
    
    def get_categoria(self):
        return self.__categoria
    def set_categoria(self,c):
        self.__categoria = c
    categoria = property(get_categoria,set_categoria)
    
    def get_regimen(self):
        return self.__regimen
    def set_regimen(self,r):
        self.__regimen = r
    regimen = property(get_regimen,set_regimen)
    
    def get_libre(self):
        return self.__libre
    def set_libre(self,l):
        self.__libre = l
    libre = property(get_libre,set_libre)
    
    def esta_disponible(self):
        return self.libre
    
    def agregar_regimen_disponible(self,r):
        self.regimen.add(r)
    
    def mostrar_datos(self):
        print(f"Habitacion {self.id} - Max Ocupantes: {self.cant_maxima_ocupantes} - Categoria: {self.get_categoria().get_nombre()} - Libre: {self.libre}")
     