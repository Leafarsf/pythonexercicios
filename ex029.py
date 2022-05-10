km=float(input("Insira a velocidade do carro: "))
print("{}Km/h" .format(km))
if km >80:
    print("Você foi multado! Calculando o valor da multa...")
    print("Você deverá pagar o valor de R${:.2f}" .format((km-80)*7.0))
else:
    print("Você está liberado!")
    print("Boa viagem!")