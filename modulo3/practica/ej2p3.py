class producto:
    codigo:str
    nombre:str

    def __init__(self,cod,nombre) -> None:
        self.codigo = cod
        self.nombre = nombre

    def __str__(self) -> str:
        palabras = self.codigo.split(sep="-")
        return f"se identifico con {palabras[1]} en {palabras[0]}"