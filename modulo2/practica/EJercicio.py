op = ""
def saludar():
    nombre = input("Cual es tu nombre? ")
    edad = input("Cual es tu edad? ")
    print(f"Hola {nombre}, tienes {edad} años de edad")

def mult(a,b):
    return a*b

def add_dict(lst):
    dic = {}
    nombre = input("Ingresa tu nombre: ")
    edad = input("Tu edad: ")
    correo = input("Tu correo: ")
    cursos = {}
    n = int(input("Numero de cursos: "))
    for i in range(n):
        nomb_cur = input("Ingrese Nombre de curso: ")
        notas = []
        n_notas = int(input("Ingrese numero de notas: "))
        while n_notas != 0:
            notas.append(int(input("Ingrese NOTAS: ")))
            n_notas -= 1

        cursos[nomb_cur] = notas
    dic["nombre"] = nombre
    dic["edad"] = edad
    dic["correo"] = correo
    dic["cursos"] = cursos
    lst.append(dic) 

def prom_dict(dic):
    arr = []
    prom = None
    prom2 = None
    for i in range(len(dic)):
        for ji in dic[i]["cursos"].values():
            prom = 0
            # LLegamos al las notas
            for k in ji:
                prom += k
            prom /= len(ji)
            #arr.append(prom)
            prom2 += prom
        prom2 /= len(dic[i]["cursos"])
        arr.append(prom2)
    print(arr)
    return arr


lst_dic = []  
notas_fin = []
op = None
while op != "0":
    op = input("Ingresa opcion: ")
    match op:
        case "1":
            saludar()
        case "2":
            a = float(input("Ingrese numero: "))
            b = float(input("Ingrese otro numero: "))
            print(f"La multiplicacion de {a} por {b} es {mult(a,b)}\n")
        case "3":
            add_dict(lst_dic)
            print()
        case "4":

            nota = prom_dict(lst_dic)
            #notas_fin.append(nota)
            print(nota)
            print()
        case "5":
            print()

