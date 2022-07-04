aluno = {}
for c in range(0,1):
    aluno['nome'] = str(input(' Insira o nome do aluno: '))
    aluno['média'] = int(input('Insira a média: '))
    if aluno['média'] >= 7:
        aluno['situação'] = 'Aprovado'
    else:
        aluno['situação'] = 'Reprovado'

print(f"O nome do aluno é igual a {aluno['nome']}")
print(f'A média do aluno é {aluno["média"]}')
print(f'A situação do aluno é {aluno["situação"]}')