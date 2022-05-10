n = int(input("Insira um número para descobrir a tabuada dele: "))
for i in range(1,11):
    print("-"*10)
    t = i*n
    print(f"{n} x {i} = {t}")