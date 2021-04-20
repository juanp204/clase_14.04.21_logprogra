def sumar(x,sum):
    sum += x
    return sum
sum = 0
while True:
    try:
        num = int(input("numero = "))
    except ValueError:
        print("solo numeros")
        continue
    if num == 0:
        sumd = 0
        for x in str(sum):
            sumd +=int(x)
        print("a suma de sus digitos es",sumd)
        break
    else:
        sum = sumar(num,sum)
        print(sum)