from modulos import cadastrar
from modulos import listar
from modulos import limpar

print("--"*30)
print("Sistema de Cadastro de Pessoas")
print("--"*30)
while True:
    escolha = int(input(
        '\033[32m1 - Cadastrar\n2 - Listar\n3 - Sair\n4- Limpar a lista\033[m\nEscolha uma opção: '))
    if escolha == 1:
        cadastrar.novoCadastro()
    elif escolha == 2:
        print("--"*30)
        print("Lista de Pessoas:")
        print()
        listar.listarPessoas()
        print("--"*30)
    elif escolha == 3:
        print('\033[31mSaindo do sistema...\033[m')
        break
    elif escolha == 4:
        limpar.limparLista()
