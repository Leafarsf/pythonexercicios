def criaTitulo(titulo):
    print(titulo)
    print('-'* len(titulo))

def calculaArea():
    for i in range(0,1):
        largura = float(input("Largura do terreno: "))
        comprimento = float(input("Comprimento do terreno: "))
        area = largura * comprimento
    print(f"A área do terreno de {largura} x {comprimento} é de {area} m²")

criaTitulo("Calculadora de área")
calculaArea()