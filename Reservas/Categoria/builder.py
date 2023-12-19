from Reservas.Categoria.categoria import Categoria
class Builder_categoria():
    def __init__(self) -> None:
        self.__categoria = None
    
    def get_categoria(self):
        return self.__categoria
    def set_categoria(self,c):
        self.__categoria = c
    categoria = property(get_categoria,set_categoria)
    
    def reset(self):
        self.categoria = Categoria()
    def set_nombre(self,n):
        self.categoria.set_nombre(n)
    
    def set_precio(self,p):
        self.categoria.set_precio(p)
    
    