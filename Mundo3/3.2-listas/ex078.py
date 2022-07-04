from more_itertools import locate
numeros = []
for i in range(0,5):
    num = int(input(f"Digite um valor inteiro para a posição {i}: "))
    numeros.append(num)
index_maximos = list(locate(numeros, lambda a: a == max(numeros)))
index_minimos = list(locate(numeros, lambda a: a == min(numeros)))
print(f"Os valores digitados foram {numeros} \n"
      f"O maior valor é {max(numeros)} na posição {index_maximos}\n"
      f"O menor valor é {min(numeros)} na posição {index_minimos}")