from random import randint
import time
import emojis
itens=('PEDRA','PAPEL','TESOURA')
computador = randint(0,2)
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input("Qual é a sua jogada: "))
print("JO")
print("KEN")
time.sleep(0.5)
print("PÔ!")
print("=-"*10)
print("O computador escolheu {}" .format(itens[computador]))
print("Jogador jogou {}" .format(itens[jogador]))
print("-="*10)
if computador == 0:
    if jogador == 0:
        print("EMPATE!")
    elif jogador == 1:
        print("Você VENCEU! {}" .format(emojis.encode(":smiley:")))
    elif jogador == 2:
        print("Você PERDEU! {}" .format(emojis.encode(":sweat:")))
elif computador == 1:
    if jogador == 0:
        print("Você VENCEU! {}" .format(emojis.encode(":smiley:")))
    if jogador == 1:
        print("EMPATE!")
    if jogador == 2:
        print("Você PERDEU! {}" .format(emojis.encode(":sweat:")))

elif computador == 2:
    if jogador == 0:
        print("Você VENCEU! {}" .format(emojis.encode(":smiley:")))
    if jogador == 1:
        print("Você PERDEU! {}" .format(emojis.encode(":sweat:")))
    if jogador == 2:
        print("EMPATE!")


