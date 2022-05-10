import time
print("-=-"*20)
print("\033[1;31mCALCULADORA DE IMC\033[1;31;0m")
peso=float(input("Insira o seu peso: "))
altura=float(input("Insira a sua altura: "))
print("CALCULANDO...")
time.sleep(4)
IMC=peso/(altura**2)
if IMC<18.5:
    print("Você está \033[1;34mabaixo do peso\033[1;34;0m e o seu IMC é de {:.1f}" .format(IMC))
elif 18.5<=IMC<25:
    print("Você está no \033[1;34mpeso ideal\033[1;34;0m e o seu IMC é de {:.1f}" .format(IMC))
elif 25<=IMC<30:
    print("Você está com \033[1;34msobrepeso\033[1;34;0m e o seu IMC é de {:.1f}" .format(IMC))
elif 30<=IMC<40:
    print("Você está em \033[1;34mobesidade\033[1;34;0m e o seu IMC é de {:.1f}" .format(IMC))
elif IMC>=40:
    print("Você está em condição de \033[1;34;mobesidade grave\033[1;34;0m e o seu IMC é de {:.1f}" .format(IMC))