soma = 0
lista = []
n = 6
for i in range(0,n):
    ins = int(input("Insira um número: "))
    lista.append(ins)
for i in lista:
    if i % 2 == 0:
        soma = soma + i
print(f"A soma dos valores pares da lista é de {soma}")

