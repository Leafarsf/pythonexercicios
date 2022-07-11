def leiaInt(msg):
    while True:
        try:
            numero = int(input(msg))
        except (KeyboardInterrupt):
            print('\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        except ValueError as erro:
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')
            print(f'\033[31mErro: {erro.__class__}\033[m')
            numero = leiaInt(msg)
        return numero

def leiaFloat(msg):
    while True:
        try:
            numero = float(input(msg))
        except (KeyboardInterrupt):
            print('\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        except ValueError as erro:
            print('\033[31mERRO! Digite um número real válido.\033[m')
            print(f'\033[31mErro: {erro.__class__}\033[m')
            numero = leiaFloat(msg)
        return numero
    
n = leiaInt("Digite um número: ")
n2 = leiaFloat("Digite um número: ")
print(f"Você digitou o número inteiro {n} e o número real {n2}")
