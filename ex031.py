km=float(input("Insira a distância de sua viagem: "))
if km <=200.00:
    print("O valor total de sua viagem é de R${:.2f}" .format(km*0.50))
    print("Boa viagem!")
else:
    print("O valor total de sua viagem é de R${:.2f}" .format(km*0.45))
    print("Boa viagem!")