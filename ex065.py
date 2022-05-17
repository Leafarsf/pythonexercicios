continuar = "S"
soma = 0
contador = 0
while continuar == "S":
    n = int(input("Insira um valor inteiro: "))
    soma +=n
    contador +=1
    continuar = str(input("Quer continuar? [S/N] ")).strip().upper()[0]


media = soma/contador
print(f"Você inseriu {contador} valores e a média entre eles é de {media}")
