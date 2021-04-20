def sumdigitos():
    for x in range((len(numeros))):
        sum = 0
        for c in str(numeros[x]):
            sum += int(c)
        print(numeros[x],"=",sum)
def repeticion():
    print("se repite",numeros.count(int(input("cuatas veces se repite = "))))
def factorial(fac):
    re = fac
    for x in range((fac-1),0,-1):
        re = re*(fac-x)
    return re
numeros = []
c = True
while c:
    num = int(input("ingrese numero = "))
    for i in range(2, num):
        if num%i == 0:
            c = False
    if c:
        numeros.append(num)
numeros.sort(reverse=True)
print(numeros)
sumdigitos()
repeticion()
print("{}! = ".format(numeros[0]),factorial(numeros[0]))



