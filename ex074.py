import random
numeros = []
cont = 0
while cont < 5:
    numeros.append(random.randint(0,1000))
    cont += 1
numeros = tuple(numeros)
print(f"Os número selecionados de forma aleatória foram {numeros}")
print(f"O maior número é {max(numeros)} e o menor número é {min(numeros)}")