
def notas(*num, sit=False):
    '''-> Função para analisar as notas e situação de varios alunos.
    param num: uma ou mais notas de alunos
    param sit: valor opcional, para verificar se a situação da turma está RUIM RAZOÁVEL OU BOA
    retorna um dicionário com as informações da turma '''
    r = dict()
    r['total'] = len(num)
    r['maior'] = max(num)
    r['menor'] = min(num)
    r['média'] = float(format(sum(num) / len(num), ".2f"))
    if sit:
        r['situação'] = ''
        if r['média'] >= 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r




print('-' * 30)
print("SITUAÇÃO DA TURMA: ")
resp = notas(1.5, 2.8, 7.8, 4.4, 5.5, 6.9, sit=True)
print(resp)
