import time
valor=float(input("Qual o valor do imóvel? R$"))
salario=float(input("Qual a sua renda? R$"))
anos=int(input("Qual a duração do financiamento em anos? "))
parcela=valor/(anos*12)
print("-=-"*20)
print("ANALISANDO...")
time.sleep(2)
print("-=-"*20)
if parcela>salario*(30/100):
    print("Para financiar um imóvel no valor de {:.2f} em {} anos você precisará pagar R${:.2f}" .format(valor,anos,parcela))
    print("O seu financiamento foi \033[1;31mnegado!\033[1;0m")
    print("Agradecemos a paciência!")
    print("-=-"*20)
else:
    print("Para financiar um imóvel no valor de {:.2f} em {} anos você precisará pagar R${:.2f}" .format(valor,anos,parcela))
    print("O seu financiamento foi \033[1;32maprovado!\033[1;0m Parabéns")
    print("Clique aqui para continuar...")
    print("-=-"*20)
