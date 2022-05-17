n = int(input("Digite um número: "))
soma = n
contador = 0
while n != 999:
    contador +=1
    n = int(input("Digite um número: "))
    soma +=n
print(f"Você levou {contador} tentativas para acertar o número e a soma total foi de {soma - 999}")

