datos = {"nombre": "", "apellido": "","dni": "", "telefono": ""}

datos["nombre"] = input("Ingrese su nombre: ")
datos["apellido"] = input("Ingrese sus apellidos: ")
datos["dni"] = input("Ingrese su DnI: ")
datos["telefono"] = input("Ingrese su telefono: ")

print("Hola {}, {}".format(datos["nombre"],datos["apellido"]))
print("Tu DNI es {} y tu celular es {}".format(datos["dni"],datos['telefono']))
