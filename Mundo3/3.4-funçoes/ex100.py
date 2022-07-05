numeros = list()
import random


def sorteia():
    for i in range(0, 5):
        n = random.randint(1, 1000)
        numeros.append(n)
        print(f"O {i+1}º valor sorteado foi {n}")
    print()
    print("E a soma dos valores pares da lista é:", end=' ')
    somaPares()
    

def somaPares():
    soma = 0
    for i in numeros:
        if i % 2 == 0:
            soma += i
    print(soma)

sorteia()