n = int(input("Insira um número para descobrir a tabuada dele: "))
print("-"*10)
for i in range(1,11):
    t = i*n
    print(f"{n} x {i} = {t}")
print("-"*10)