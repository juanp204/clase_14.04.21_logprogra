def validar_email(x):
    if ("@" in x) and ((".com" in x) or (".co" in x)):
        return True
    else:
        return False
while True:
    if validar_email(input("email = ")):
        print("valido")
        break
    else:
        print("invalido")
        continue