import math
catetooposto=float(input("Insira o valor do cateto oposto: "))
catetoadjacente=float(input("Insira o valor do cateto adjacente: "))
hip=math.hypot(catetooposto,catetoadjacente)
print("A hipotenusa do triângulo é {} {:.2f} {}" .format('\033[1;33m',hip,'\033[0;m'))