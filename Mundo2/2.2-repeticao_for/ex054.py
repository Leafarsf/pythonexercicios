#também podemos fazer utilizando um contador, mas optei por listas para prática.
from datetime import date
ano = []
maioridade = []
minoridade = []
for i in range(1,8):
    n = int(input(f"Em que ano a {i}ª pessoa nasceu? "))
    ano.append(n)
ano = [int(i) for i in ano]
for i in ano:
    if date.today().year - i >= 18:
        maioridade.append(i)
    else:
        minoridade.append(i)
for i in maioridade:
    print(f"O número de pessoas maiores de idade de acordo com o ano de nascimento é de: {len(maioridade)}")
    print(f"O número de pessoas menores de idade de acordo com o ano de nascimento é de: {len(minoridade)}")
    break
