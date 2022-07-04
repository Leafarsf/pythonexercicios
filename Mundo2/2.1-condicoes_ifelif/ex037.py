n=int(input("Digite um número: "))
e=int(input("Você deseja converter esse número para: \n"
'1)binário\n'
'2)octal\n'
'3)hexadecimal\n'
 'digite sua escolha: '))
if e==1:
    print("O seu número convertido em binário é: {}" .format(bin(n)))
elif e==2:
    print("O seu número convertido em octal é: {}" .format(oct(n)))
elif e==3:
    print("O seu número convertido em hexadecimal é: {}" .format(hex(n)))
else:
    print("\033[1;31mEscolha uma opção válida!\033[1;0m")