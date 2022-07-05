pessoa = dict()
pessoas = list()
soma = media = 0
mulheres = []
while True:
    pessoa.clear()
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper()[0]
    pessoa['nome'] = nome
    pessoa['idade'] = idade
    pessoa['sexo'] = sexo
    soma += pessoa['idade']
    if pessoa['sexo'] not in "MF":
        print('ERRO! Por favor, digite apenas M ou F.')
    if pessoa['sexo'] in "F":
        mulheres.append(pessoa['nome'])
    pessoas.append(pessoa.copy())
    while True:
        continuar = str(input('Deseja continuar? [S/N] ')).upper()[0]
        if continuar in 'SN':
            break
        print("ERRO! RESPONDA APENAS S OU S")
    if continuar == 'N':
        break
print("-=" * 30)
print(f"Foram inseridas um total de {len(pessoas)} pessoas!")
print(f"A média de idade é de {soma / len(pessoas):5.2f} anos.")
print("As mulheres cadastradas foram: ", end='')
for m in mulheres:
    print(f"{m}", end=' ')
print()
print("As pessoas acima da media são: ", end='')
for p in pessoas:
    if p['idade'] > soma / len(pessoas):
        print(f"{p['nome']}", end=' ')