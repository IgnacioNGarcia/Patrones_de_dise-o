class Fecha_tomada_exception(Exception):
    def __init__(self, mensaje="La fecha no está disponible"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)