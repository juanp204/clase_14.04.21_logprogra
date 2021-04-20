def contar(num,ite):
    suma = 0
    for x in num:
        if x in ite:
            suma +=1
    return suma
suma = contar(input("digite un numero para analizar = "), input("cuanto se repite = "))
print("se repite", suma)