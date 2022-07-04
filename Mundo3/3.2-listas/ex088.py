#Nao usei listas compostas, mas funcionou :)
import time
import random
lista = []
print('='*20)
print('JOGANDO NA LOTERIA')
print('='*20)

jogos = int(input("Quantos jogos você quer fazer? "))

print("-=" * 3, end='')
print(f"SORTEANDO {jogos} jogos", end='')
print("-=" * 3)
for jogo in range(jogos):
    for i in range(6):
        numero = random.randint(0,60)
        if numero not in lista:
            lista.append(numero)
        else:
            numero = random.randint(0,60)
            lista.append(numero)
    print(f"Jogo {jogo + 1} : {sorted(lista)}")
    lista.clear()
    time.sleep(0.9)
print("-=" * 3, end='')
print("BOA SORTE!", end='')
print("-=" * 3)
