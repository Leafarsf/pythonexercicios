continuar = "S"
soma = 0
contador = 0
maior = 0
menor = 0
while continuar == "S":
    n = int(input("Insira um valor inteiro: "))
    soma +=n
    contador +=1
    if contador == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    continuar = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
media = soma/contador
print(f"Você inseriu {contador} valores e a média entre eles é de {media}")
print(f"O menor valor foi {menor} e o maior valor foi {maior}")