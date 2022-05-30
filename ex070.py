mais_de_1k = 0
total = 0
barato = 0
nome_barato = ""
cont = 0
print("-" * 20)
print("LOJÃO SALDÃO - TUDO BARATÃO!")
print("-" * 20)
while True:
    produto = str(input("Insira o nome do produto: "))
    preco = int(input("Insira o preço do produto: "))
    total += preco
    cont +=1
    if preco > 1000:
        mais_de_1k +=1
    if cont == 1:
        barato = preco
        nome_barato = produto
    else:
        if preco < barato:
            barato = preco
            nome_barato = produto
    continuar = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if continuar in "N":
        break
print(f"O total gasto na compra é de R${total}")
print(f"A sua cesta tem {mais_de_1k} produtos acima de R$1000")
print(f"E o produto mais barato {nome_barato} custa R${barato}")