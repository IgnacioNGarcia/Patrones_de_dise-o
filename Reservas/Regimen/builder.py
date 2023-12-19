from Reservas.Regimen.regimen import Regimen
class Builder_regimen():
    def __init__(self) -> None:
        self.__regimen = None
    
    def get_regimen(self):
        return self.__regimen
    def set_regimen(self,r):
        self.__regimen = r
    regimen = property(get_regimen,set_regimen)
    
    def set_nombre(self,n):
        self.regimen.set_nombre(n)
    def set_porcentaje(self,p):
        self.regimen.set_porcentaje(p)
    
    def reset(self):
        self.regimen = Regimen()