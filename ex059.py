v1 = float(input("Insira o primeiro valor: "))
v2 = float(input("insira o segundo valor: "))
selecao = 0
while selecao == 0:
    print("Selecione a função que você gostaria de executar:")
    print('''
    [1]SOMA
    [2]MULTIPLICAÇÃO
    [3]MAIOR VALOR
    [4]NOVOS NÚMEROS
    [5]SAIR''')
    selecao = str(input("Selecione a sua opção: "))
while selecao not in "12345":
    selecao = str(input("Seleção inválida. Tente novamente: "))
if selecao == "4":
    while selecao == "4":
        v1 = float(input("Insira o primeiro valor: "))
        v2 = float(input("Insira o segundo valor: "))
        print("Selecione a função que você gostaria de executar:")
        print('''
            [1] SOMA
            [2]MULTIPLICAÇÃO
            [3]MAIOR VALOR
            [4]NOVOS NÚMEROS
            [5]SAIR''')
        selecao = str(input("Selecione a sua opção: "))
if selecao == "1":
    print(f'''Você escolheu a opção SOMA! O resultado é:
{v1} + {v2} = {v1+v2}''')
if selecao == "2":
    print(f'''Você escolheu a opção MULTIPLICAÇÃO! O resultado é:
{v1} x {v2} = {v1*v2}''')
if selecao == "3":
    maior = 0
    if v1 > v2:
        maior = v1
    else:
        maior = v2
    print(f"O maior valor inserido é {maior}")
else:
    print("PROGRAMA FINALIZADO!")
    quit()



