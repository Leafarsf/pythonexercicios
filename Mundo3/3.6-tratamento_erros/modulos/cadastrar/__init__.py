
def novoCadastro():
    arquivo = open("lista_pessoas.txt", "a")
    try:
        nome = str(input('Nome: '))
    except (TypeError):
        print('\033[31mErro! Nome inválido.\033[m')
        novoCadastro()
    try:
        idade = int(input('Idade: '))
    except (TypeError, ValueError):
        print('\033[31mErro! Idade inválida.\033[m')
        novoCadastro()
    arquivo.write(f"{nome};{idade}\n")
    print('Cadastro realizado com sucesso!')
    arquivo.close()

