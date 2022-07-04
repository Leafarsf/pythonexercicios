import time
jogador = {}
contador_gols = []
jogador['nome'] = str(input('Nome: '))
partidas = int(input(f"Quantas partidas o {jogador['nome']} jogou? "))
for i in range(partidas):
    contador_gols.append(int(input(f"Quantos gols na partida {i+1}? ")))
jogador['gols'] = contador_gols[:]
jogador['total'] = sum(contador_gols)
print('-=' * 30)
print('JOGADOR')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'Na partida {i} fez {v} gols.')
print(f"O total de gols foi {jogador['total']}.")
