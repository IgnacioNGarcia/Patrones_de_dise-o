from Composite.Clases.centro_atencion import Centro_atencion_medica
class Uap(Centro_atencion_medica):
    def __init__(self, nombre, direccion,tiempo_promedio) -> None:
        self.__nombre = nombre
        self.__direccion = direccion
        self.__tiempo_promedio = tiempo_promedio
    
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
    
    
    def get_tiempo_promedio(self):
        return self.__tiempo_promedio
    def set_Tiempo_promedio(self,t):
        self.__tiempo_promedio = t
    tiempo_promedio = property(get_tiempo_promedio,set_Tiempo_promedio)
    
    def get_cantidad_ambulancias(self):
        return 0
    
    def atender_paciente(self):
        return super().atender_paciente()
    
    def mostrar_informacion_base(self):
        print(f"Base: {self.nombre} - Direccion: {self.direccion} - Ambulancias: {self.get_cantidad_ambulancias()} - Tiempo Promedio: {self.tiempo_promedio}")
        