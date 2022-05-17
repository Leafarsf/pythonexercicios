n = int(input("Digite um número [999 para parar o programa]: "))
soma = n
contador = 0
while n != 999:
    contador +=1
    n = int(input("Digite um número [99 para parar o programa]: "))
    soma +=n
print(f"Você digitou {contador} números e a soma total foi de {soma - 999}")

