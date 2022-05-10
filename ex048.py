soma = 0
contador = 0
for i in range(0,500):
    if i % 2 !=0 and i % 3 == 0:
        soma += i
        contador +=1
print(f"A soma dos {contador} números ímpares no intervalo de 1 a 500 é de {soma}")