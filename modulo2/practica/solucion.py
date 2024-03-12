import math
flagProgram=True
dict_cursos={}
lista_aprobados=[]
lista_desaprobados=[]
def saludar():
    name=input("Ingrese su nombre completo: ")
    correo=input("Ingrese su correo: ")
    msg=f'Hola ,{name} con usuario {correo}'
    return msg

def fxMath():
    numberOne=input('ingrese primer numero')
    numberTwo=input('ingrese segundo numero')
    print(numberOne+numberTwo)

def lista_dicts():
    list_dict_tmp=[{
        'nomnbre':'name',
        'edda':20,
        'correo':'correo@gmail.com',
        'cursos':[
             {'curso': 'Python', 'notas': [10, 20, 15]},
            {'curso': 'SQL', 'notas': [13, 12, 18]},
            {'curso': 'Power BI', 'notas': [14, 15, 15]}
        ]
    }]
    dict_cursos=list_dict_tmp
    print(dict_cursos)

def calcular_promedio():
    for i in dict_cursos:
        lenNotas=i['cursos']['notas']
        sum=0
        for j in lenNotas:
            sum+=j
        promedio=sum/len(lenNotas)
        i['cursos']['promedio']=promedio
    
def alumnosAprobados():
    lista_aprobados=[]
    for i in dict_cursos:
        if i['cursos']['promedio']>=10:
            lista_aprobados.append(i)
        else:
            lista_desaprobados.append(i)        

def numbers_random():
    limit=int(math.pow(10,10))
    lista_final=[]
    for i in range(0,limit,15000):
        if i%2 == 0 and i%5 ==0 and i%7==0:
            lista_final.append(i)
    print(len(lista_final))

def two_number(a:int,b:int):
    if a>b:
        return a
    else:
        return b

while flagProgram:

    opcionInput=input('Ingrese una opcion')
    opcion=int(opcionInput)

    if opcion==1:
        saludo=saludar()
        print(saludo)

    elif opcion == 2:
        fxMath()
    elif opcion ==3:
        lista_dicts()
    elif opcion ==4:
        calcular_promedio()
    elif opcion ==5:
        alumnosAprobados()
        print(lista_aprobados)
    elif opcion ==6:
        alumnosAprobados()
        print(lista_aprobados)
    elif opcion == 7:
        print("entro")
        numbers_random()
    elif opcion ==8:
        numberOne=int(input('ingrese primer numero'))
        numberTwo=int(input('ingrese segundo numero'))
        two_number
    else:
        print("Elije una opcion correcta")