from datetime import date
import time
print("A Confederação nacional de natação precisa de seu ano de nascimento\npara classificá-lo de acordo com nossos parâmetros.")
ano=int(input("Insira o ano de nascimento: "))
idade= date.today().year - ano
print("Você tem {} anos" .format(idade))
print("Analisando a sua classificação...")
time.sleep(3)
if idade<=9:
    print("-=-"*20)
    print("Parabéns, você foi classificado na categoria \033[1;35mMIRIM\033[1;35;0m")
    print('-=-'*20)
elif idade<=14:
    print("-=-"*20)
    print("Parabéns, você foi classificado na categoria \033[1;32mINFANTIL\033[1;32;0m")
    print("-=-"*20)
elif idade<=19:
    print("-=-"*20)
    print("Parabéns, você foi classificado na categoria \033[1;33mJÚNIOR\033[1;33;0m")
    print("-=-"*20)
elif idade<=25:
    print("-=-"*20)
    print("Parabéns, você foi classificado na categoria \033[1;34mSÊNIOR\033[1;34;0m")
    print("-=-"*20)
else:
    print("-=-"*20)
    print("Parabéns, você foi classificado na categoria \033[1;31mMASTER\033[1;31;0m")
