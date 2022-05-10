n1=int(input("Insira um número: "))
n2=int(input("Insira outro número: "))
if n1>n2:
    print("O primeiro valor inserido, {}, é o maior valor." .format(n1))
elif n2>n1:
    print("O segundo valor inserido, {}, é o maior valor." .format(n2))
elif n1==n2:
    print("Os dois valores inseridos são iguais.")