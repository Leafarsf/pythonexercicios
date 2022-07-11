from modulos import moeda


preco = float(input('Digite o preço: R$ '))
print(f'A metade de {preco} é R${moeda.metade(preco)}')
print(f'O dobro de {preco} é R${moeda.dobro(preco)}')
porcentagem_menor = float(input("Qual a porcentagem que você quer reduzir? "))
porcentagem_maior = float(input("Qual a porcentagem que você quer aumentar? "))
print(f'Aumentando {int(porcentagem_maior)}%, temos R${moeda.aumentar(preco, porcentagem_maior)}')
print(f'Reduzindo {int(porcentagem_menor)}%, temos R${moeda.diminuir(preco, porcentagem_menor):.2f}')