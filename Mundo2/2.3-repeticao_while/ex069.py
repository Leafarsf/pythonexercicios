contador_maior = 0
contador_homens = 0
contador_mulheres = 0
from datetime import date
while True:
    print("-"*20)
    nome = str(input("Insira o nome: "))
    sexo = str(input("Insira o sexo [M/F]: ")).strip().upper()
    ano = int(input("Insira o ano de nascimento: "))
    idade = 2022 - ano
    if sexo in "Mm":
        contador_homens +=1
    if idade > 18:
        contador_maior +=1
    if sexo in "Ff" and idade < 20:
        contador_mulheres +=1
    continuar = str(input("Quer continuar? [S/N] "))
    if continuar in "Nn":
        print("-"*10)
        print(f"A partir dos dados inseridos temos:\n"
              f"{contador_maior} pessoas maiores de idade\n"
              f"{contador_homens} homens\n"
              f"{contador_mulheres} mulher(es) com menos de 20 anos")
        print("-"*10)
        break
