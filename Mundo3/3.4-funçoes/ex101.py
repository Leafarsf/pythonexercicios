import datetime

def verificaVoto(ano):
    idade = datetime.datetime.now().year - ano
    if idade < 16:
        print(f"Com {idade} anos: voto negado!")
    elif idade > 16 and idade <= 17:
        print(f"Com {idade} anos: voto opcional!")
    elif idade > 18 and idade <= 65:
        print(f"Com {idade} anos: voto obrigatório!")
    elif idade > 65:
        print(f"Com {idade} anos: voto opcional!")

print('-' * 20)
ano = int(input("Digite o ano de nascimento: "))
verificaVoto(ano)


