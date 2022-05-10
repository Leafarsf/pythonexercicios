import math
num=float(input("Digite um número: "))
ni= math.trunc(num)
print("O valor digitado foi {} e sua porção inteira é {}" .format(num,ni))
#ou
print("O valor digitado foi {} e sua porção inteira é {:.0f}" .format(num,num))
#ou
print("O valor digitado foi {} e sua porção inteira é {}" .format(num,math.trunc(num)))