times = (
    'Palmeiras',
    'Corinthians',
    'Athlético - PR',
    'Atlético - MG',
    'Internacional',
    'Fluminense',
    'Botafogo',
    'Santos',
    'São Paulo',
    'Bragantino',
    'Avaí',
    'Atlético - GO',
    'Ceará SC',
    'Flamengo',
    'Coritiba',
    'América - MG',
    'Goiás',
    'Cuiabá',
    'Fortaleza',
    'Juventude',
)
escolha = str(input("Digite [1] para visualizar o top 5 do brasileirão \n"
                    "Digite [2] para visualizar todos os times em ordem alfabética \n"
                    "Digite [3] para visualizar a posição do Athlético - PR no brasileirão \n"
                    "Digite [4] para visualizar os 4 últimos colocados da tabela \n"
                    "escolha: "))
while escolha not in '1234':
    escolha = str(input("Digite [1] para visualizar o top 5 do brasileirão \n"
                        "Digite [2] para visualizar todos os times em ordem alfabética \n"
                        "Digite [3] para visualizar a posição do Athlético - PR no brasileirão \n"
                        "Digite [4] para visualizar os 4 últimos colocados da tabela \n "
                        "escolha: "))
if escolha == '1':
    for time in times[0:5]:
        print(time)
elif escolha == '2':
    for time in sorted(times):
        print(time)
elif escolha == '3':
    print(f'O time Athlético - PR está na posição {times.index("Athlético - PR") + 1} da tupla.')
elif escolha == '4':
    cont = 20
    for time in times[16:21]:
        print(f"O {cont}º colocado do brasileirão é {time}")
        cont = cont -1


