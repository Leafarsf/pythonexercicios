n = int(input("Insira um número para descobrir o seu fatorial: "))
total = 0
c = n
fatorial = 1
print(f"Calculando {n}! = ", end='')
while c > 0:
    print(f"{c}",end = '')
    print(' x ' if c > 1 else ' = ', end='')
    fatorial *= c
    c -= 1
print(f"{fatorial}")

