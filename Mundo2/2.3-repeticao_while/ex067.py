n = int(input("Qual o número você deseja ver a tabuada? "))
while True:
    print("-=-"*20)
    if n > 0:
        for i in range(1,11):
            print(f"{n} x {i} = {n*i}")
    print("-=-"*20)
    if n <0:
        print("PROGRAMA ENCERRADO")
        break
    n = int(input("Qual número você deseja ver a tabuada? "))

