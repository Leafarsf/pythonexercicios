s=float(input("Insira o seu salário: R$"))
if s>1250:
    print("O seu salário teve um aumento de 10% e você passará a receber o valor de R${:.2f}" .format(s+(s/10)))
else:
    print("O seu salário teve um aumento de 15% e você passará a receber o valor de R${:.2f}" .format(s+(s*0.15)))

