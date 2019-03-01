par=0
for x in range(-1000000000000000000,1000000000000000):
    x=int(input("ingrese los numeros"))
    if x%2==0:
        x=x+1
    else:
        break
        print("hay ",par," numeros positivos")
