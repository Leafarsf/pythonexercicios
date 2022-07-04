cont = 0
soma = 0
while True:
    n = int(input("Insira um número [999 para parar]: "))
    cont +=1
    if n == 999:
        break
    soma +=n
print(f"Você inseriu {cont} valores e a soma entre eles é igual a {soma}")