def primo(x):
    if x%2==0 or x%3==0 or x%5==0 or x%7==0 or x%11==0:
        return True
    else:
        return False
if primo(int(input("ingrese numero = "))):
    print("es primo")
else:
    print("no es primo")

