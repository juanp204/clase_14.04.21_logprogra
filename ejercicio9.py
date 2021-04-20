def longitud(ced):
    if len(ced)==10:
        return True
    else:
        return False
while True:
    try:
        cedula = int(input("cedula = "))
    except ValueError:
        print("solo numeros")
        continue
    if longitud(str(cedula)):
        print("es valido")
        break
    else:
        print("no es valido")
        break

