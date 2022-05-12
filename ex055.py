peso = []
for i in range(0,5):
    kg = float(input("Insira o peso da pessoa em Kg: "))
    peso.append(kg)
peso = [float(i) for i in peso]
print(f"O menor peso é {min(peso)} e o maior peso é {max(peso)}")