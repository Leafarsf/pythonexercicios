c = ('\033[m',  #0 sem cor;
    '\033[0;30;41m', #1 vermelho
)

def meAjuda(comando):
    help(comando)

def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print("~" * tam)
    print(f'  {msg}')
    print("~" + msg + "~")
    print(c[0], end='')

comando = ""
while True:
    titulo("Sistema de Ajuda!")
    comando = str(input("Digite um comando: "))
    if comando.upper() == "FIM":
        break
    else: 
        meAjuda(comando)
    titulo("ATÉ LOGO!")
