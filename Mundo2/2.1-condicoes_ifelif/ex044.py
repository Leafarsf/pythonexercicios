import time
print("=-="*20,"LOJAS RAFAEL", "=-="*20)
preço=float(input("Insira o preço do produto a ser pago: R$"))
print('''Nós oferecemos as seguintes formas de pagamento:
       1)À vista no dinheiro: 10% de desconto
       2)À vista no cartão: 5% de desconto
       3)Em até 2x no cartão: preço padrão
       4)Em até 3x no cartão: 20% de juros''')
pag=str(input("Insira a forma de pagamento: "))
print("Calculando o preço total a ser pago...")
if pag=="1":
    print("O preço total a ser pago é de R${}" .format(preço-(preço/10)))
elif pag=="2":
    print("O preço total a ser pago é de R${}" .format(preço-((preço*5)/100)))
elif pag=="3":
    print("O preço total a ser pago é de R${}" .format(preço))
    print("Sua compra será feita em duas parcelas de R${} sem juros" .format(preço/2))
elif pag=="4":
    totparc=int(input("Qual o número de parcelas? "))
    total = preço+(preço*20/100)
    parcela=total/totparc
    print("Sua compra será feita em {} parcelas de R${:.2f} com juros" .format(totparc,parcela))
    print("O preço total a ser pago é de R${:.2f}" .format(preço+(preço*20)/100))
else:
    pag=0
    print("Opção INVÁLIDA de pagamento. Tente novamente.")
print("Agradecemos a preferência! Volte sempre!")
