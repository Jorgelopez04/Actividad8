from carro_compra import CarroCompras
from libro_existente_error import LibroExistenteError
from libro import Libro
from libro_error import LibroError
from libro_agotado_error import LibroAgotadoError
from existencias_insuficientes_error import ExistenciasInsuficientesError
class TiendaLibros:
    def __init__(self):
        self.catalogo = {}
        self.carrito= CarroCompras()

    def adicionar_libro_a_catalogo(self,isbn:str, titulo:str,precio:float ,existencias:int):
        if isbn in self.catalogo:
            raise LibroExistenteError(titulo,isbn)

        else:
            nuevo_libro = Libro(isbn, titulo, precio, existencias)
            self.catalogo[isbn] = nuevo_libro
            return nuevo_libro

    def agregar_libro_a_carrito(self,libro,cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad a comprar debe ser mayor que cero")

        if Libro.isbn not in self.catalogo:
            raise LibroError(f"El libro con ISBN {libro.isbn} no existe en el catálogo")

        existencias = self.catalogo[libro.isbn].existencias

        if existencias == 0:
            raise LibroAgotadoError(libro.titulo, libro.isbn)

        if cantidad > existencias:
            raise ExistenciasInsuficientesError(libro.titulo, libro.isbn, cantidad, existencias)

        self.carrito.agregar_item(libro, cantidad)
      
        self.catalogo[libro.isbn].existencias -= cantidad


    def retirar_item_de_carrito(self,isbn:Libro):
        self.carrito.quitar_item(isbn)

        


        
        pass
    # Defina metodo inicializador __init__

    # Defina metodo adicionar_libro_a_catalogo

    # Defina metodo agregar_libro_a_carrito

    # Defina metodo retirar_item_de_carrito
