numeros = []
cont = 0
while True:
    numeros.append(int(input("Digite um valor inteiro: ")))
    cont +=1
    continuar = str(input("Deseja continuar? [S/N] "))
    if continuar not in "Ss":
        break
print("="*20)
print(f"Você digitou {cont} valores.\n"
      f"A lista digitada em ordem decrescente é {sorted(numeros, reverse=True)}")
if 5 in numeros:
    print("O número 5 está na lista")
else:
    print("O número 5 NÃO está na lista.")
print("="*20)