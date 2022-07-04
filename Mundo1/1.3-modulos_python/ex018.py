import math
angulo=float(input("Insira o ângulo: º"))
seno=math.sin(math.radians(angulo))
cosseno=math.cos(math.radians(angulo))
tangente=math.tan(math.radians(angulo))
print("O ângulo de {} tem o SENO de {} {:.2f} {}" .format(angulo,'\033[1;34m',seno,'\033[0m'))
print("O ângulo de {} tem o COSSENO de {} {:.2f} {}" .format(angulo,'\033[1;33m',cosseno,'\033[0m'))
print("O ângulo de {} tem a TANGENTE de {} {:.2f} {}" .format(angulo,'\033[1;31m',tangente,'\033[1;31m'))