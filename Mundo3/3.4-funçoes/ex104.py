def leiaInt(msg):
    numero = input(msg)
    while not numero.isnumeric():
        print('\033[31mERRO! Digite um número inteiro válido.\033[m')
        numero = input(msg)
    return int(numero)

n = leiaInt("Digite um número: ")
print(f"Você digitou o número {n}")
