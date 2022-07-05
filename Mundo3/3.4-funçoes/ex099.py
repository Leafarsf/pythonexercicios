def maior(*num):
    print("-="*20)
    print("Analisando os valores passados...")
    for i in num:
        print(f"{i}", end=' ')
    print()
    print(f"Foram informados {len(num)} valores")
    print(f"O maior valor encontrado foi {max(num)}")
    print("-="*20)
    print()
    

maior(1,2,3,4,5,6,7)
maior(1,2)
maior(9,0,5,4,6,7,2)