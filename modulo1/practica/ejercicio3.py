# Ingresar el ingreso y mostrar la salida de gastos y ahorro

print("Ingresos DEL HOGAR\n")
ing = float(input("Ingrese el ingreso mensual: "))
suma = 0
gasto = -1
while ing >= suma and gasto != 0:
    gasto = float(input("Ingrese gastos por separado: "))
    if ing < suma + gasto:
        print("NO ALCANZAN MAS GASTOS")
        continue
    else:
        suma += gasto

#Ingresos - Gastos = SUMA - Ahorro = Ingresos-suma
print("Ingresos totales: {}".format(ing))
print("Gastos totales: {}".format(suma))
print("Ahorros totales: {}".format(ing-suma))