itens = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Régua', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro Didático', 34.90)
print("="*30)
print("LISTAGEM DE PREÇOS")
print("="*30)
for posicao in range(0, len(itens)):
    if posicao % 2 == 0:
        print(f"{itens[posicao]:.<30}", end='')
    else:
        print(f"R${itens[posicao]:>7.2f}")