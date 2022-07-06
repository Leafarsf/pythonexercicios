def calculaFatorial(num, show=False):
    '''Calcula o fatorial de um número definido.
    :param num: O número a ser calculado.
    :param show: Se True, mostra o cálculo.
    :return: O fatorial do número.'''
    fatorial = 1
    for i in range(num, 0, -1):
        if show:
            print(i, end='')
            if i != 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        fatorial *= i
    return fatorial

print('-' * 20)
print(calculaFatorial(6))
print(calculaFatorial(6, show=True))
print('-' * 20)