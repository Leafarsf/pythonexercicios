from modulos import moeda


preco = float(input('Digite o preço: R$ '))
print(f'A metade de {preco} é {moeda.moeda(moeda.metade(preco))}')
print(f'O dobro de {preco} é {moeda.moeda(moeda.dobro(preco))}')
porcentagem_menor = float(input("Qual a porcentagem que você quer reduzir? "))
porcentagem_maior = float(input("Qual a porcentagem que você quer aumentar? "))
print(
    f'Aumentando {int(porcentagem_maior)}%, temos {moeda.moeda(moeda.aumentar(preco, porcentagem_maior))}')
print(
    f'Reduzindo {int(porcentagem_menor)}%, temos {moeda.moeda(moeda.diminuir(preco, porcentagem_menor))}')
