numeros = []
cont = 0
pares = []

while cont < 4:
    numero = int(input("Digite qualquer valor inteiro: "))
    numeros.append(numero)
    cont += 1

numeros = tuple(numeros)
print(f"Você digitou os números {numeros}")
print(f"O número 9 apareceu {numeros.count(9)} vezes")
if 3 in numeros:
    print(f"A primeira ocorrência do número 3 foi na posição {numeros.index(3)}")
else:
    print(f"O valor 3 não foi digitado em nenhuma posição!")
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
print(f"Os números pares digitados foram {pares}")
