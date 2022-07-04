import random
print("-"*20)
print("Vamos jogar PAR ou ÍMPAR?")
print("-"*20)
contador = 0
while True:
    selecao = str(input("SELECIONE:\n"
                        "[1] PAR\n"
                        "[2] ÍMPAR\n"))
    if selecao == "1":
        n_jogador = int(input("Digite o seu número de 0 a 10: "))
        n_computador = random.randint(1,10)
        produto = n_jogador + n_computador
        if produto % 2 == 0:
            print(f"O computador jogou {n_computador}")
            print(f"Você jogou {n_jogador}")
            print(f"A soma é {produto} e você GANHOU!")
            contador +=1
        if produto % 2 > 0:
            print(f"O computador jogou {n_computador}")
            print(f"Você jogou {n_jogador}")
            print(f"A soma é {produto} e você perdeu após {contador} vitórias!")
            break
    if selecao == "2":
        n_jogador = int(input("Digite o seu número de 0 a 10: "))
        n_computador = random.randint(1, 10)
        produto = n_jogador + n_computador
        if produto % 2 > 0:
            print(f"O computador jogou {n_computador}")
            print(f"Você jogou {n_jogador}")
            print(f"A soma é {produto} e você GANHOU!")
            contador += 1
        if produto % 2 == 0:
            print(f"O computador jogou {n_computador}")
            print(f"Você jogou {n_jogador}")
            print(f"A soma é {produto} e você PERDEU após {contador} vitorias")
            print("FIM DE JOGO!")
            break





