import re
class producto:
    codigo:str
    nombre:str

    def __init__(self,cod,nombre) -> None:
        if re.findall(r"/w+-/d{5}-/d{4}",cod) != []:
            self.codigo = cod
        else:
            self.codigo = "TACNA".upper()+"-00000-"+"2024"
        self.nombre = nombre

    def __str__(self) -> str:
        palabras = self.codigo.split(sep="-")
        return f"se identifico {self.nombre} con {palabras[1]}"

productos = []
productos.append(producto("LIMA-00010-2023","Shampoo"))
print(productos[0])