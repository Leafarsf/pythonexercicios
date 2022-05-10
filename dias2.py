idade=int(input("Insira quantos anos você tem: "))
if idade>20:
    print("Você já viveu {} dias." .format(idade*365))
    print("E ainda irá viver em média {} dias" .format((80*365)-(idade*365)))
else:
    print("Você já viveu {} dias!" .format(idade*365))
    print("Você ainda tem muitos dias à sua frente!")