class ItemCompra:

    def __init__(self,libro,cantidad):
        self.libro=libro
        self.cantidad=cantidad

    def calcular_subtotal(self):
        return self.libro.precio * self.cantidad

    pass
