from libro_error import LibroError
from libro import Libro


class ExistenciasInsuficientesError(LibroError):

    def __init__(self,libro:Libro,cantidad_a_comprar:int,titulo:Libro,isbn:Libro):
        super().__init__(libro)
        self.cantidad_a_comprar=cantidad_a_comprar
        self.titulo=titulo
        self.isbn=isbn


    def __str__ (self):
        return f"El libro con titulo {self.titulo} y isbn {self.isbn}no tiene suficientesexistencias para realzar la compra :cantidad a comprar:{self.cantidad_a_comprar} , existencias "


    pass

    # Defina metodo inicializador

    # Defina metodo espcial
