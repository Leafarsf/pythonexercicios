pessoas = []
dados = []
maior = 0
menor = 0
cont = 0
nome_pesado = ''
nome_leve = ''
while True:
    dados.append(str(input("Digite o nome: ")))
    dados.append(float(input("Digite o peso: ")))
    pessoas.append(dados[:])
    dados.clear()
    cont += 1
    continuar = str(input("Deseja continuar? [S/N] ")).strip().upper()
    if continuar in "Nn":
        break
for p in pessoas:
    if p[1] > maior:
        maior = p[1]
        nome_pesado = p[0]
    elif p[1] > 0 or p[1] < menor:
        menor = p[1]
        nome_leve = p[0]
print("=-=" * 20)
print(f"No total, você cadastrou {cont} pessoas.")
print(f"O maior peso foi de {maior}. Peso de {nome_pesado}")
print(f"O menor peso foi de {menor}. Peso de {nome_leve}")
