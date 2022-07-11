from modulos import moeda
valor = float(input('Digite o preço: R$ '))
aumentar = float(input('Digite a porcentagem de aumento: '))
diminuir = float(input('Digite a porcentagem de redução: '))

moeda.resumo(valor, aumentar, diminuir)