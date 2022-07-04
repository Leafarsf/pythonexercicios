somaidade = 0
mediadade = 0
maioridadehomem = 0
nomemaisvelho = ''
for i in range (1,5):
    print('----- {}ª PESSOA -----' .format(i))
    nome = str(input('Insira o nome:')).strip()
    idade = int(input('Insira a idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    mediaidade = somaidade / 4
    if i == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomemaisvelho = nome
    if sexo in "Mm" and idade > maioridadehomem:
        maioridadehomem = idade
        nomemaisvelho = nome
print(f"A média de idade do grupo é de {mediaidade}")
print(f"O homem mais velho tem {maioridadehomem} e se chama {nomemaisvelho}")
