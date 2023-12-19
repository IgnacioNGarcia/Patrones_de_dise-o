from Observer.Clases.vuelo import Vuelo
class Pantalla():
    def __init__(self, vuelo :Vuelo) -> None:
        self.__vuelo = vuelo
    def get_vuelo(self):
        return self.__vuelo
    def set_vuelo(self,v):
        self.__vuelo = v
    vuelo = property(get_vuelo,set_vuelo)
    
    def mostrar_datos(self):
        print(f"Vuelo: {self.vuelo.get_nombre()} - Hora Local: {self.vuelo.get_fecha_hora()}")
        print("DESTINOS: \n")
        for sub in self.vuelo.get_subs():
            sub.mostrar_info()
            print("\n")