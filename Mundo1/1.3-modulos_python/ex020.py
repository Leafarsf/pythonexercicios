import random
primeiro=str(input("Primeiro aluno:"))
segundo=str(input("Segundo aluno:"))
terceiro=str(input("Terceiro aluno:"))
quarto=str(input("Quarto aluno:"))
lista=[primeiro,segundo,terceiro,quarto]
#print("A ordem de apresentação será:",random.sample(lista,k=4))
#print("ou")
random.shuffle(lista)
print('A ordem de apresentação sera:')
print(lista)