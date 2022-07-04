import time
pessoa = {}
pessoa['nome'] = str(input('Nome: '))
pessoa['idade'] = 2022 - int(input('Ano de nascimento: '))
pessoa['CTPS'] = int(input('Carteira de trabalho (0 não tem): '))
if pessoa['CTPS'] != 0:
    pessoa['contratação'] = int(input('Ano de contratação: '))
    pessoa['salário'] = float(input('Salário: '))
    pessoa['aposentadoria'] = pessoa['idade'] + (35 - (2022 - pessoa['contratação']))
print('-=' * 30)
for k,v in pessoa.items():
    print(f'{k} tem o valor {v}')
    time.sleep(1)