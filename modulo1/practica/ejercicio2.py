# Calcular area y perimetro de un circulo
import math as m

r = float(input("ingrese el radio del circulo: "))
print("\nSu perimetro es {} y su area es {}".format(2*m.pi*r,(r**2)*(m.pi)))