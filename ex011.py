l=float(input("Insira a largura da sua parede: "))
a=float(input("Insira a altura de sua parede: "))
ar=l*a
t=ar/2
print("A dimensão de sua parede é igual a {}m² \ne o número de litros de tinta necessários para pintá-la é de {:.2f}l" .format(ar,t))
