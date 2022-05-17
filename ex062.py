print("-=-"*20)
print("TERMOS DE UMA P.A")
print("=-="*20)
primeiro_termo = int(input("Insira o primeiro termo da sua P.A: "))
razao = int(input("Insira a razão de sua P.A: "))
n_termos = int(input("Insira o número de termos que você irá visualizar: "))
termo = primeiro_termo
contador = 0
termos = 0
while n_termos > 0:
    while contador < n_termos:
        print(f"{termo} > ", end='')
        termo = termo + razao
        contador += 1
        termos += 1
    print("FIM DA P.A")
    n_termos = int(input("Caso queira continuar, insira o número de termos: "))
    contador = 0
print(f"A P.A foi encerrada após {termos} termos")

