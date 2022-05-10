from datetime import date
ano=int(input("Insira o ano de seu nascimento: "))
alist= date.today().year - ano
if alist == 18:
    print('-=-'*20)
    print("Quem nasceu em {} tem {} anos em {}" .format(ano,date.today().year-ano,date.today().year))
    print("\033[0;4;32mEstá na hora de você realizar o seu alistamento! Não esqueça!\033[0;4;32;0m")
    print("Você ira se alistar no ano de {}" .format(ano+18))
    print('-=-'*20)
elif alist<18:
    print("-=-"*20)
    print("Quem nasceu em {} tem {} anos em {}." .format(ano,date.today().year-ano,date.today().year))
    print("\033[0;4;36mVocê ainda não precisa se alistar!\033[0;4;36;0m")
    print("Ainda restam {:.0f} anos para o alistamento obrigatório." .format(18-alist))
    print("Você irá se alistar no ano de {}" .format(ano+18))
    print("-=-"*20)
else:
    print("-=-"*20)
    print("Quem nasceu em {} tem {} anos em {}." .format(ano,date.today().year-ano,date.today().year))
    print("\033[1;31mVocê já deveria ter se alistado há {} anos atrás\033[1;31;0m" .format(alist-18))
    print("O seu alistamento foi no ano de {}" .format(date.today().year-(alist-18)))
    print("-=-"*20)