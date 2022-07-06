def area(larg, comp):
    a = larg * comp
    print(f"A área do terreno de {larg} x {comp} é de {a} m²")

print("Controle de Terrenos")
print("-"*20)
larg = float(input("Largura do terreno: "))
comp = float(input("Comprimento do terreno: "))
area(larg, comp)