
from libro_error import LibroError

from libro import Libro

class LibroExistenteError(LibroError):
    def __init__(self, libro:Libro,titulo:Libro,isbn:Libro):
        super().__init__(libro)
        self.titulo=titulo
        self.isbn=isbn

    def __str__(self) -> str:
        return f"El libro con titulo {self.titulo} y  isbn {self.isbn} ya existen en el catalogo"	
    





    # Defina metodo inicializador

    # Defina metodo especial
