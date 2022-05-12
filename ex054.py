ano = []
maioridade = []
for i in range(0,7):
    n = int(input("Insira o ano de nascimento: "))
    ano.append(n)
ano = [int(i) for i in ano]
for i in ano:
    if 2022 - i >= 18:
        maioridade.append(i)
for i in maioridade:
    print(f"O número de pessoas maiores de idade de acordo com o ano de nascimento é de: {len(maioridade)}")
    break
