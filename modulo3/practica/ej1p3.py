class producto:
    nombre:str
    cantidad:int
    codigo:str
    def __init__(self,cod,nombre,cant) -> None:
        self.nombre = nombre
        self.cantidad = cant
        self.codigo = cod

    def __str__(self) -> str:
        return f"{self.codigo} {self.cantidad} {self.nombre}"

class catalogo:
    num_Catal:str
    lstProd = []

    def agregar(self,prod:producto):
        self.lstProd.append(prod)
        print("{} se agrego correctamente".format(prod))
    
    def mostrarProd(self):
        print("Productos :")
        for i in self.lstProd:
            print(f"{i.codigo} {i.nombre}")

op = None
cat = catalogo()
while op != "0":
    op = input("Elige una opcion: 1 agregar 2 mostrar ")
    match op:
        case "1":
            cod = input("Ingresa cod. del produto: ")
            nombre = input("Ingresa nombre del producto: ")
            cant = int(input("Ingresa cantidad: "))
            producto1 = producto(cod,nombre,cant)
            cat.agregar(producto1)
        case "2":
            cat.mostrarProd()
#lst = []
#lst.append(producto1)

