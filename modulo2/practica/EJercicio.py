op = ""
def saludar():
    nombre = input("Cual es tu nombre? ")
    edad = input("Cual es tu edad? ")
    print(f"Hola {nombre}, tienes {edad} años de edad")

def suma(a,b):
    return a*b

while op != "0":
    match op:
        case "1":
            saludar()
