#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa PA.
print("="*20)
print("10 TERMOS DE UMA P.A")
print("="*20)
lista_progressao=[]
primeiro_termo = int(input("Insira o primeiro termo de sua progressão aritmética: "))
razao = int(input("insira a razão de sua progressão aritmética: "))
for i in range(0,10):
    progressao = primeiro_termo + razao
    primeiro_termo = progressao
    lista_progressao.append(primeiro_termo)
progressao = str(lista_progressao)[1:-1]
print(f"Os dez primeiros termos dessa PA são {progressao}")