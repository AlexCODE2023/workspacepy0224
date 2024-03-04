import lib.op as op

a:None
b:None
while True:
    try:
        a = float(input("Primer numero: "))
        b = float(input("Segundo numero: "))
        print("el resultado es :{}".format(op.dividirOP(a,b)))
        break
    except Exception as e:
        print(e)
