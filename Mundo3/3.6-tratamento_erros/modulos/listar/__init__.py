def listarPessoas():
    with open("lista_pessoas.txt", "r") as arquivo:
        for linha in arquivo:
            print(f'O nome é {linha.split(";")[0]} e a idade é {linha.split(";")[1]}')
        arquivo.close()