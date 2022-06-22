numeros = []
pares = []
impares = []

while True:
    n = int(input("Digite um valor inteiro: "))
    numeros.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    continuar = str(input("Quer continuar? [S/N] "))
    if continuar not in 'Ss':
        break
print(f"Todos os valores digitados foram {numeros}\n"
      f"Os valores pares digitados foram {pares}\n"
      f"Os valores ímpares digitados foram {impares}")