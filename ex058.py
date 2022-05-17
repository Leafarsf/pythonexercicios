import random
import pygame
n = random.randint(0,10)
contador = 0
print("-=-"*20)
print("Vou pensar em um número de 0 a 10... Tente adivinhar!")
print("=-="*20)
numero = int(input("Em qual número pensei? "))
while numero != n:
    print("Que pena... Você errou.")
    pygame.mixer.init()
    pygame.init()
    pygame.mixer.music.load("errou.mp3")
    pygame.mixer.music.play(loops=0, start=0.0)
    numero = int(input("Tente novamente! Em qual número pensei? "))
    contador += 1
print(f"Parabéns! Você acertou o número depois de {contador} tentativas!")