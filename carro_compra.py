from item_compra import ItemCompra

class CarroCompras:
    def __init__(self):
        self.item:list=[]

    def agregar_item(self,libro,cantidad:int):
        item_creado=ItemCompra(libro,cantidad)
        self.item.append(item_creado)
        return item_creado
    
    def calcular_total(self):
        total=sum(self.item)

        return total
    
    def quitar_item(self,isbn):
        self.item=[i for i in self.item if i.Libro.isbn !=isbn]
        return self.item
    pass
    # Defina metodo inicializador __init__(self)

    # Defina el metodo agregar_item

    # Defina el metodo calcular_total

    # Defina el metodo quitar_item
