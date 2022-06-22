import bisect
numeros = []
for i in range(0,5):
    n = int(input("Digite um valor inteiro: "))
    bisect.insort(numeros,n)
    organizar = bisect.bisect(numeros, n, lo=0)
    print(f"O valor {n} está sendo inserido na posição {organizar - 1}")
print(f"Os valores digitados em ordem são {numeros})