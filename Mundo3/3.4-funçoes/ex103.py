def fichaJogador(nome='<desconhecido>', gols=0):
    '''
    -> Função que recebe o nome e quantidade de gols de um jogador e retorna uma string com os dados do jogador.
    :param nome: nome do jogador (str)
    :param gols: quantidade de gols do jogador (int)
    :return: string com os dados do jogador (str)
    '''
    if nome == "":
        nome = '<desconhecido>'
    if gols.isnumeric():
        gols = gols
    else:
        gols = 0
    return f'O jogador {nome} fez {gols} gols.' 

print('-' * 20)
nome_jogador = str(input('Nome do jogador: '))
gols_jogador = input('Número de gols: ')
print(fichaJogador(nome_jogador, gols_jogador))