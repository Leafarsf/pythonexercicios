cidade=str(input("Insira o nome de sua cidade: "))
print("O nome da cidade começa com Santo:", cidade.startswith("Santo"))
#ou, assim fica melhor pq joga tudo pra maiúsculo e consegue identificar a palavra
print(cidade[:5].upper() == 'SANTO')

