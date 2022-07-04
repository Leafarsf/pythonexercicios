matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = 0
soma_terceira = 0

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(
            input(f"Digite o valor da posição [{linha}, {coluna}]: "))
        if matriz[linha][coluna] % 2 == 0:
            pares = pares + matriz[linha][coluna]
        while [coluna] == 3:
            soma_terceira = sum(matriz[linha])


for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f"[{matriz[linha][coluna]}]", end=" ")
    print()

for linha in range(0,3):
    soma_terceira += matriz[linha][2]
    
print(f"A soma de todos os valores pares digitados é igual a {pares}")
print(f"A soma dos valores da terceira coluna é igual a {soma_terceira}")
print(f"O maior valor da segunda linha é {max(matriz[1])} ")
