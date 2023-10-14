from libro_error import LibroError


class LibroAgotadoError(LibroError):
    def __init__(self,titulo,isbn):
        super().__init__()
        self.titulo=titulo
        self.isbn=isbn


    def __str__(self):
        return f"El libro con título '{self.titulo}' y ISBN {self.isbn} está agotado"
    pass

    # Defina metodo inicializador

    # Defina metodo especial
