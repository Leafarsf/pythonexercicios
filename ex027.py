nome=str(input("Digite o seu nome: ")).strip()
n=nome.split()
print("Prazer em conhecê-lo(a) {}" .format(nome))
print("Seu primeiro nome é {}" .format(n[0]))
print("Seu último nome é {}" .format(n[len(n)-1]))

