import calendar
from datetime import date
ano=int(input("Insira um ano para descobrir se é bissexto ou não: "))
if ano == 0:
    ano=date.today().year
print("O ano é de {} bissexto" .format(ano) if calendar.isleap(ano) else "O ano de {} não é bissexto" .format(ano))