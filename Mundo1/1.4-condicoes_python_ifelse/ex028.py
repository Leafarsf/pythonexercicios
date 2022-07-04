import random
import pygame
from time import sleep
n=random.randint(1,5)
print("-=-"*10)
print("Vou pensar em um número de 1 a 5. Tente adivinhar...")
print("-=-" *10)
numero=int(input("Em que número eu pensei? "))
print("PROCESSANDO...")
sleep(3)
if numero == n:
    print("Parabéns, você acertou!")
    print("O número era: {}" .format(n))
else:
    print("Que pena, você errou...")
    pygame.mixer.init()
    pygame.init()
    pygame.mixer.music.load("errou.mp3")
    pygame.mixer.music.play(loops=0,start=0.0)
    pygame.event.wait()
    print("O número correto era: {}" .format(n))