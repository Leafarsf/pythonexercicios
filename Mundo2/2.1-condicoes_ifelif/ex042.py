a=int(input("Insira o primeiro lado do triângulo: "))
b=int(input("Insira o segundo lado do triângulo: "))
c=int(input("Insira o terceiro lado do triângulo: "))
if a < b + c and b <a + c and c <a + b:
    print("Os seus segmentos podem formar um triângulo! ", end='')
    if a == b == c:
        print("O seu triângulo é \033[1;31mequilátero!\033[1;31;0m")
    elif a==b or b==c or c==a:
        print("O seu triângulo é \033[1;31mIsósceles!\033[1;31;0m")
    else:
        print("O seu triângulo é \033[1;31mEscaleno!\033[1;31;0m")

else:
    print("Os seus segmentos não podem formar um triângulo!")