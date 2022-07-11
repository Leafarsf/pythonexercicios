
def dobro(num, formatacao=False):
    if moeda:
        return moeda(num * 2)
    else:
        return num * 2


def metade(num, formatacao=False):
    if formatacao == True:
        return moeda(num / 2).replace('.', ',')
    else:
        return num / 2


def aumentar(num, porcentagem, formatacao=False):
    if formatacao == True:
        return moeda(num + (num * (porcentagem / 100)))
    else:
        return num + (num * (porcentagem / 100))


def diminuir(num, porcentagem, formatacao=False):
    if formatacao == True:
        return moeda(num - (num * (porcentagem / 100)))
    else:
        return num - (num * (porcentagem / 100))


def moeda(num):
    return f'R${num:.2f}'.replace('.', ',')


def resumo(preco, aumento, reducao):
    print("-" * 30)
    print("RESUMO DO VALOR".center(30))
    print("-" * 30)
    print(f"Preço analisado: \t{moeda(preco)}")
    print(f'A metade de R${preco}:  \t{metade(preco, True)}')
    print(f'O dobro de R${preco}:  \t{dobro(preco, True)}')
    print(f'Aumentando {int(aumento)}%:  \t{aumentar(preco, aumento, True)}')
    print(f'Reduzindo {int(reducao)}%:  \t{diminuir(preco, reducao, True)}')
    print("-" * 30)
