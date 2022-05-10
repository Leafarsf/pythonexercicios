n = int(input("Digite um número e descubra se ele é um número primo ou não: "))
primo = False
for i in range (2,n):
    if n % 1 == 0 and n % n == 0:
        primo = True
        break
if primo == True:
    print(f"O número {n} é um número primo!")
else:
    print(f"O número {n} não é um número primo!")