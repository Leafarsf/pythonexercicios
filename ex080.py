import bisect
numeros = []
for i in range(0,5):
    n = int(input("Digite um valor inteiro: "))
    if i == 0 or n > numeros[-1]:
        print("Adicionando ao final da lista...")
    else:
        print(f"O valor {n} está sendo inserido na posição {organizar - 1}")
    bisect.insort(numeros,n)
    organizar = bisect.bisect(numeros, n, lo=0)
print(f"Os valores digitados em ordem são {numeros}")