from modulos import moeda


preco = float(input('Digite o preço: R$ '))
print(f'A metade de {preco} é {moeda.metade(preco, True)}')
print(f'O dobro de {preco} é {moeda.dobro(preco, True)}')
porcentagem_menor = float(input("Qual a porcentagem que você quer reduzir? "))
porcentagem_maior = float(input("Qual a porcentagem que você quer aumentar? "))
print(
    f'Aumentando {int(porcentagem_maior)}%, temos {moeda.aumentar(preco, porcentagem_maior, True)}')
print(
    f'Reduzindo {int(porcentagem_menor)}%, temos {moeda.diminuir(preco, porcentagem_menor, True)}')
