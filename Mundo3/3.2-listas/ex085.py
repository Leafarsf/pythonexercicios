numeros = []
pares = []
impares = []
for i in range(0, 7):
    n = int(input(f"Digite o {i+1}º valor: "))
    if n % 2 == 0:
        pares.append(n)
        numeros.append(pares[:])
    else:
        impares.append(n)
        numeros.append(impares[:])
print("=-=" * 20)
print(
    f"Os valores pares digitados em ordem crescente foram foram: {sorted(pares)}")
print(
    f"Os valores ímpares digitados em ordem crescente foram: {sorted(impares)}")
