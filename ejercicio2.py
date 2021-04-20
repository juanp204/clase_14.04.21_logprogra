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
        break
    else:
        sum = sumar(num, sum)
        print(sum)