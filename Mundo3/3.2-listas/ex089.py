alunos = []
dados = []
import sys
while True:
    dados.append(str(input("Digite o nome do aluno: ").strip().upper()))
    dados.append(float(input("Digite a primeira nota do aluno: ")))
    dados.append(float(input("Digite a segunda nota do aluno: ")))
    alunos.append(dados[:])
    continuar = str(input("Deseja continuar? [S/N] ")).strip().upper()
    dados.clear()
    while continuar not in "Nn" and continuar not in 'Ss':
        print("Opção inválida. Tente novamente.")
        continuar = str(input("Deseja continuar? [S/N] ")).strip().upper()
    if continuar in "Nn":
        break
print("-="*30, end='')
print("MEDIAS DOS ALUNOS!", end='')
print("-="*30)

for i in range(len(alunos)):
    print(f"Nome do aluno: {alunos[i][0]}")
    print(f"Média do aluno: {(alunos[i][1] + alunos[i][2])/2:.2f}\n")

while True:
    for i in range(len(alunos)):
        print(f"O aluno {alunos[i][0]} está disponível para consulta das notas individuais.")
    for i in range(len(alunos)):
        consulta = str(input("Digite o nome do aluno para consulta: ")).strip().upper()
        for i in range(len(alunos)):
            if consulta in alunos[i][0]:
                print(f"Nome do aluno: {alunos[i][0]}")
                print(f"Notas do aluno: {alunos[i][1]} e {alunos[i][2]}\n")
                sys.exit()

