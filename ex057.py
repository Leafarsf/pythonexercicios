sexo = str(input("Insira o seu sexo [M/F]: ")).strip().upper()[0]
while sexo not in "MmFf":
    sexo = str(input("Erro na formatação. Insira o seu sexo: ")).strip().upper()[0]
print(f"O sexo selecionado foi {sexo}.")



