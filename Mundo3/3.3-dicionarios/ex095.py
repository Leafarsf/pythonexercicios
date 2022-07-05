import time
jogadores = []
jogador = {}
partidas = []
while True:
    jogador['nome'] = str(input('Nome do jogador: '))
    total = int(input('Número de partidas: '))
    partidas.clear()
    for g in range(0,total):
        partidas.append(int(input(f'Quantos gols na partida {g}: ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    jogadores.append(jogador.copy())
    continuar = str(input('Deseja continuar? [S/N] ')).upper()[0]
    while True:
        if continuar in'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if continuar == 'N':
        break
print('-' * 40)
print("TABELA DE JOGADORES:")
print("cod ", end='')
for i in jogador.keys():
    print(f'{i:<15}', end=' ')
print()
print("-" * 40)
for k, j in enumerate(jogadores):
    print(f'{k:>4} ', end='')
    for d in j.values():
        print(f'{str(d):<15} ', end='')
    print()
print('-' * 40)
while True:
    escolha = int(input('Mostrar dados de qual jogador? (999 para parar):  '))
    if escolha == 999:
        break
    if escolha >= len(jogadores):
        print('Não existe jogador com esse código.')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {jogadores[escolha]["nome"]}:')
        for i, g in enumerate(jogadores[escolha]['gols']):
            print(f'    No jogo {i+1} fez {g} gols.')
            time.sleep(0.5)
print('-' * 40)
print('VOLTANDO AO MENU PRINCIPAL...')
print('-' * 40)



    
