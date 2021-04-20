palabras = []
palabra = ""
#oracion = input("oracion =")
for x in input("oracion = "):
    if " " in x:
        if palabra != "":
            print("apend")
            palabras.append(palabra)
        palabra = ""
    else:
        palabra +=x
if palabra != "":
    palabras.append(palabra)
if len(palabras) != 0:
    print("la cantidad de caracteres que tiene ´{}´ es {}".format(palabras[len(palabras)-1],len(palabras[len(palabras)-1])))