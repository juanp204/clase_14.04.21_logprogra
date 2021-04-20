print("digite ´salir´ para cerrar")
while True:
    num = input()
    if num == "salir":
        break
    sum = 0
    if int(num)<0:
        print("solo numeros positivos")
        continue
    for x in num:
        sum += int(x)
    if sum>=10:
        print("los digitos suman mas de 10")
    else:
        print("el numero suma menor que 10")

