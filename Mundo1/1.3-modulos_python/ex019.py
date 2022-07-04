import random
n1=str(input("Insira o nome do aluno: "))
n2=str(input("Insira o nome do aluno: "))
n3=str(input("Insira o nome do aluno: "))
n4=str(input("Insira o nome do aluno: "))
alunos=[n1,n2,n3,n4]
print("O aluno escolhido para escrever no quadro é",random.choice(alunos))