def mensagemDiferente(msg):
    print('-' * len(msg))
    print(msg)
    print('-' * len(msg))

mensagemDiferente("Sistema de alunos!")


def soma(a, b):
    print(a + b)

soma(8,9)
soma(4,5)
soma(2,1)

#empacotar, passar varios parametros de forma que o programa possa entender
def contador(*num):
    for valor in num:
        print(f"{valor} ", end='')
    print("FIM!")
        


contador(2, 1, 7)
contador(8,0)
contador(4,4,7,6,2)

valores = [6,3,9,1,0,2]
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos +=1

dobra(valores)
print(valores)