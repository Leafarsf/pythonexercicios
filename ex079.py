nums = []
while True:
    n = int(input("Digite um número inteiro: "))
    if n not in nums:
        nums.append(n)
        print("Valor adicionado com sucesso...")
    else:
        print("Valor já adicionado!")
    continuar = str(input("Quer continuar? [S/N] "))
    if continuar not in 'Ss':
        break
print(f"Os valores inseridos em ordem crescente foram {sorted(nums)}")
