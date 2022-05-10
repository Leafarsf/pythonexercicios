print("Os seres humanos vivem em média 80 anos. Vamos descobrir quantos dias você já viveu?")
idade=int(input("Quantos anos você tem? "))
dias=(80*365)-(idade*365)
print("Você tem {} anos e já viveu {} dias! Você ainda viverá em media mais {} dias" .format(idade, (idade*365), dias))
