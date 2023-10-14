from libro import Libro
from libro_error import LibroError

class UIConsola:

    def __init__(self, tienda_libros):
        self.tienda_libros = tienda_libros

    def retirar_libro_de_carrito_de_compras(self):
      
        isbn = input("Ingrese el ISBN del libro a retirar del carrito: ")

        try:
           
            self.tienda_libros.retirar_item_de_carrito(isbn)
            print("Libro retirado del carrito con éxito.")
        except LibroError as e:

            print(f"El libro con isbn : {e}")


    def agregar_libro_a_carrito_de_compras(self):
        try:
            isbn = input("Ingrese el ISBN del libro que desea agregar al carrito: ")
            cantidad = int(input("Ingrese la cantidad de unidades a agregar: "))
            self.tienda_libros.agregar_libro_a_carrito(isbn, cantidad)
            print(f"{cantidad} unidades del libro con ISBN {isbn} se han agregado al carrito con éxito.")
        except LibroError as e:
            print(f"Error: {e}")
        except ValueError as e:
            print("Error: La cantidad debe ser un número entero.")

    def adicionar_un_libro_a_catalogo(self):
        try:
            isbn = input("Ingrese el ISBN del libro: ")
            titulo = input("Ingrese el título del libro: ")
            precio = float(input("Ingrese el precio del libro: "))
            existencias = int(input("Ingrese la cantidad de existencias: "))
            self.tienda_libros.adicionar_libro_a_catalogo(isbn, titulo, precio, existencias)
            print("Libro agregado al catálogo con éxito.")
        except ValueError as e:
            print("Error: El precio debe ser un número decimal y las existencias deben ser un número entero.")
        except LibroError as e:
            print(f"Error: {e}")