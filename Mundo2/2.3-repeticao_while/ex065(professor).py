num =[[],[]]
valor = 0
for c in range(1,8):
    valor = int(input(f'Digite o {c}o.valor:'))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)

print(f'Todos os valores: {num}')
print(f"Somente os valores pares: {num[0]}")
print(f"Somente os valores pares: {num[1]}")