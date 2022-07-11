from modulos import dado
from modulos import moeda
valor = dado.leiaDinheiro()
aumentar = float(input('Digite a porcentagem de aumento: '))
diminuir = float(input('Digite a porcentagem de redução: '))
moeda.resumo(valor, aumentar, diminuir)


