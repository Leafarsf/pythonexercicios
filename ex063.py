termos = int(input("Quantos termos da sequência de Fibonacci você quer visualizar? "))
contador = 3
t1 = 0
t2 = 1
print(f"{t1} > {t2}", end='')
while contador <= termos:
    t3 = t1 + t2
    print(f" > {t3}", end='')
    t1 = t2
    t2 = t3
    contador +=1
print(" > FIM")