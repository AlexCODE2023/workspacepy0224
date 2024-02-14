# Programa que filtre si eres apto

#resp = ""
msg = "No eres apto para iniciar un negocio"
resp = input("Eres mayor de edad? SI/NO: ")
if resp == "SI":
    resp = input("Tienes RUC? SI/NO: ")
    if resp == "SI":
        resp = input("Tienes nombre comercial? SI/NO: ")
        if resp == "SI":
            msg = "Eres apto para abrir un comercio"

print (msg)