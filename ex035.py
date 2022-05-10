import time
print("-=-"*10)
print("Analisador de triângulos")
print("-=-"*10)
a=int(input("Digite o primeiro lado do triângulo: "))
b=int(input("Digite o segundo lado do triângulo: "))
c=int(input("Digite o terceiro lado do triângulo: "))
print("Analisando...")
time.sleep(3)
if a+b>c:
    if b+c>a:
        if c+a>b:
            print("Os três números {}, {} e {} formam um triângulo" .format(a,b,c))
else:
            print("Os três números {}, {} e {} não formam um triângulo" .format(a,b,c))