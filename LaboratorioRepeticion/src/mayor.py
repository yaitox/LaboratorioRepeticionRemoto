pos=0
neg=0
zero=0

for x in range(0,10):
    x=int(input("escriba los numeros"))
    if x<0:
        pos=pos+1
    else:
        if x==0:
            zero=zero+1
        else:
         pos=pos+1

print("hay ",pos," numeros positivos")
print("hay ",zero," ceros")
print("hay ",neg," negativos")