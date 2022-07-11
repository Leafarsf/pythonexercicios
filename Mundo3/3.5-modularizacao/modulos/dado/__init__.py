def leiaDinheiro():
    while True:
        try:
            valor = str(input('Digite o preço: R$ '))
            return float(valor.replace(',', '.'))
        except ValueError:
            print('\033[31mERRO! Digite um valor válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mPrograma interrompido.\033[m')
            return 0
        else:
            break
