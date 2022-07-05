import time # Importa o módulo time


def contador(inicio, fim, passo):
    print("-="*20)
    print(f"Contagem de {inicio} até {fim} de {passo} em {passo}")
    for i in range(inicio, fim, passo):
        print(i+1, end=' ')  # end=' ' para não quebrar a linha]
        time.sleep(0.3)
    print("FIM!")
    print("-="*20)
    print(f"Contagem de {fim} até {inicio} de 2 em 2")
    for i in range(fim, -1, -2):
        print(i, end=' ')
        time.sleep(0.3)
    print()
    print("Agora é sua vez de personalizar a contagem!")
    inicio = int(input("Início: "))
    fim = int(input("Fim: "))
    passo = int(input("Passo: "))
    if passo < 0:
        passo = passo * -1
    if passo == 0:
        passo = 1
    print(f"Contando de {inicio} até {fim} de {passo} em {passo}")
    for i in range(inicio, fim, passo):
        time.sleep(0.5)
        print(i, end=' ')
    print("FIM!")
    print("-="*20)


contador(0, 10, 1)