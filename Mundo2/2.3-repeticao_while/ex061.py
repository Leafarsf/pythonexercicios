print("-=-"*20)
print("DEZ TERMOS DE UMA P.A")
print("=-="*20)
primeiro_termo = int(input("Insira o primeiro termo da sua P.A: "))
razao = int(input("Insira a razão de sua P.A: "))
termo = primeiro_termo
contador = 1
while contador <= 10:
    print(f"{termo} > ", end='')
    termo = termo + razao
    contador +=1
print("FIM")

