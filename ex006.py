n=int(input("Digite um número:"))
d=n*2
t=n*3
r=n**(1/2)
print("O dobro do número {} é {} e o triplo é {} e a raiz quadrada é {:.2f}" .format(n,d,t,r))
#ou
print("O dobro do número {} é {} o triplo é {} e a raiz quadrada é {:.2f}" .format(n,n*2,n*3,n**(1/2)))
#ou
print("O dobro do número {} é {}, o triplo é {} e a raiz quadrada é {:.2f}" .format(n,n*2,n*3,pow(n,(1/2))))


