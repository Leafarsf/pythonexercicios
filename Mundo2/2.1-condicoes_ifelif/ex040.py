import time
import emojis
n1=float(input("Insira a primeira nota do aluno: "))
n2=float(input("Insira a segunda nota do aluno: "))
m=(n1+n2)/2
print("Calculando a sua nota...")
time.sleep(3)
if m>=7:
    print("-=-"*20)
    print("Parabéns, você foi \033[1;32maprovado!\033[1;32;0m Sua média foi {:.1f}" .format(m))
    print("Boas férias! {}" .format(emojis.encode(':smile:')))
    print("-=-"*20)
elif m < 5:
    print("-=-" * 20)
    print("Você está \033[1;31mreprovado.\033[1;31;0m A sua média final foi de {:.1f}".format(m))
elif m <=6.9:
    print("-=-"*20)
    print("Você está em \033[1;33mrecuperação.\033[1;33;0m A sua média foi de {:.1f}" .format(m))
    print("Entre em contato com a secretaria.")
    print("-=-"*20)
