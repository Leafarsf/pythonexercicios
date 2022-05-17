peso = []
for i in range(1,6):
    kg = float(input(f"Insira o peso da {i} pessoa em Kg: "))
    peso.append(kg)
peso = [float(i) for i in peso]
print(f"O menor peso é {min(peso)} e o maior peso é {max(peso)}")