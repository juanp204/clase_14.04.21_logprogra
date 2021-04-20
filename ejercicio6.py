def factorial(fac):
    re = fac
    for x in range((fac-1),0,-1):
        re = re*(fac-x)
    return re
def imprimir(fac):
    imp = "1"
    for x in range(2,(fac+1)):
        imp += "x{}".format(x)
    return imp
fac = int(input("!"))
print(imprimir(fac),"=",factorial(fac))

