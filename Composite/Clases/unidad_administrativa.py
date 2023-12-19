from Composite.Clases.base_sanitaria import Base_sanitaria
class Unidad_administrativa(Base_sanitaria):
    def __init__(self, nombre, direccion) -> None:
        self.__nombre = nombre
        self.__direccion = direccion
        self.__centros :Base_sanitaria = []
    
    def get_nombre(self):
        return self.__nombre
    def set_nombre(self,n):
        self.__nombre = n
    nombre = property(get_nombre,set_nombre)
    
    def get_direccion(self):
        return self.__direccion
    def set_direccion(self,d):
        self.__direccion = d
    direccion = property(get_direccion,set_direccion)
    
    def get_centros(self):
        return self.__centros
    def set_centros(self,c):
        self.__centros = c
    centros = property(get_centros,set_centros)
    
    def add_centro(self, c :Base_sanitaria):
        self.centros.append(c)
    
    def delete_centro(self,c :Base_sanitaria):
        self.centros.remove(c)
    
    def get_cantidad_ambulancias(self):
        cantidad = 0
        for centro in self.centros:
            cantidad += centro.get_cantidad_ambulancias()
        return cantidad
    
    def get_tiempo_promedio(self):
        tiempo = 0
        i = 0
        for centro in self.centros:
            tiempo += centro.get_tiempo_promedio()
            i+=1
        return round(tiempo/i)
    def mostrar_informacion_base(self):
        print(f"BASE {self.nombre} - DIRECCION {self.direccion}")
        print("Compuesta por:")
        for centro in self.centros:
            centro.mostrar_informacion_base()