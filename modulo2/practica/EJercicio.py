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
    for i in range(len(dic)): #dic es una lista
        prom2 = 0
        for ji in dic[i]["cursos"].values():
            prom = 0
            # LLegamos al las notas
            for k in ji:
                prom += k
            prom /= len(ji)
            #arr.append(prom)
            prom2 += prom
        prom2 /= len(dic[i]["cursos"])
        #print(len(dic[i]["cursos"]))
        arr.append(prom2)
    #print(arr)
    return arr

def mayor():
    a = float(input("Ingresa Un numero: "))
    b = float(input("Ingresa otro numero: "))
    if a< b:
        return b
    else:
        return a

lst_dic = []  
notas_fin = []
op = None
while op != "9":
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

            notas_fin = prom_dict(lst_dic)
            #notas_fin.append(nota)
            print(notas_fin)
            print()
        case "5":
            i= 0
            # Usa un index por separado range(len(notas_fin))
            print("Notas Aprobadas: ")
            if notas_fin != []:
                for nota in notas_fin:
                    if nota > 11:
                        print("{} {}".format(lst_dic[i]["nombre"],lst_dic[i]["correo"]))
                    i += 1
            else:
                print("Genera notas OPCION 4 ")
            print()
        case "6":
            i= 0
            # Usa un index por separado range(len(notas_fin))
            print("Notas Desaprobadas: ")
            if notas_fin != []:    
                for nota in notas_fin:
                    if nota <= 11:
                        print("{} {}".format(lst_dic[i]["nombre"],lst_dic[i]["correo"]))
                    i += 1
            else:
                print("Genera notas OPCION 4 ")
            print()
        case "7":
            i = int(input("Ingresa tu numero: "))
            def rangoN(num:int):
                arr = []
                for i in range(1,num+1):
                    if i % 2 == 0 and i % 5 == 0 and i% 7 == 0:
                        arr.append(i)
                print(arr)
                print(len(arr))
            rangoN(i)
        case "8":
            mayor()
            
        

