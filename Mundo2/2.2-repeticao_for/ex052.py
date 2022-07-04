n = int(input("Digite um número e descubra se ele é um número primo ou não: "))
tot = 0
for i in range (1,n + 1):
    if n % i == 0:
        tot +=1
print(f'O número {n} foi divisível {tot} vezes')
if tot <= 2:
    print(f"O número {n} é um número primo!")
else:
    print(f"O número {n} não é um número primo!")

