class Cliente():
    def __init__(self, nombre, dni, mail) -> None:
        self.__nombre = nombre
        self.__dni = dni
        self.__mail = mail
    
    def get_nombre(self):
        return self.__nombre
    def set_nombre(self,n):
        self.__nombre = n
    nombre = property(get_nombre,set_nombre)
    
    def get_dni(self):
        return self.__dni
    def set_dni(self,d):
        self.__dni = d
    dni = property(get_dni,set_dni)
    
    def get_mail(self):
        return self.__mail
    def set_mail(self,m):
        self.__mail = m
    mail = property(get_mail,set_mail)
    
        