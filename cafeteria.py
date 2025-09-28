Catalogo= {
    "Cafe solo": 1000,
    "Cafe con leche" : 2000,
    "Sandwich" : 2500,
    "Medialunas": 750
}


class Pedidos:
    def __init__(self,cliente,producto,cantidad):
        self.cliente= cliente
        self.producto = producto
        self.precio= Catalogo[producto]
        self.cantidad= cantidad
    
    def total(self):
        total= self.precio * self.cantidad
        return total  
    
    def __str__(self):
        return  (f"Pedido de {self.cantidad} {self.producto}(s) para el cliente: {self.cliente} - "
                f"Precio unitario ${self.precio}, Total: {self.total()}")
    
    
class Cafeteria:
    def __init__(self):
        self.pedidos= []
        
        
    def agregar_pedido(self,pedido):
        self.pedidos.append(pedido)
        print( pedido, "Fue agregado con exito!")
    
    def vacio(self):
        if len(self.pedidos) == 0:
            return True
        else:
            return False
    
    def eliminar_pedido(self):
        if self.vacio():
            print("No ingresaron pedidos!")
        else:
            print(f"{self.pedidos.pop()} Eliminado con exito!")
        
    def mostrar_pedido(self):
        if self.vacio():
            print("No hay pedidos registrados!")
        else:
            print("Lista de pedidos:")
            for pedidoss in self.pedidos:
                print(pedidoss)
        
    def menu(self):
        catalogo= {}
  
          
def main():
    gestor = Cafeteria()
    while True:
        print("Que desea hacer?")
        print("1)- Agregar pedido")
        print("2)- Eliminar el ultimo pedido")
        print("3)-Ver pedidos pendientes")
        print("4)-Finalizar el dia")
        opcion= input("Ingrese la opcion deseada: ")
        if opcion == "1":
            try:
                cliente= input("Ingrese el nombre del cliente: ").capitalize()
                print("----Catalogo----")
                for i, (producto,precio) in enumerate (Catalogo.items(), start=1):
                    print(f"{i}- {producto} - ${precio}")
                eleccion= int(input("Seleccione un producto (numero): "))
                producto= list(Catalogo.keys())[eleccion - 1]
                cantidad= int(input("Ingrese la cantidad a llevar: "))
                pedido= Pedidos(cliente,producto,cantidad)
                gestor.agregar_pedido(pedido)
            except ValueError:
                print("Ingrese un dato numerico!")
            except IndexError:
                print("Ingrese un numero que se encuentre en el menu")
        elif opcion == "2":
            gestor.eliminar_pedido()
        elif opcion == "3":
            gestor.mostrar_pedido()
        elif opcion == "4":
            print("Dia finalizado!")
            break
        else:
            print("Ingrese una opcion valida!")
            
main()