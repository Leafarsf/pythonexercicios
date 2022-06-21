tupla = ('zero','um', 'dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','catorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
escolha = int(input("Digite um número de 0 a 20: "))
while escolha > 20 or escolha < 0:
    escolha = int(input("Tente novamente. Digite um número de 0 a 20: "))
for num in tupla:
    print(f"O número digitado por extenso é {tupla[escolha]}")
    break
