import unidecode
def palindromo(str):
    str = str.replace(" ","")
    str = unidecode.unidecode(str)
    str = str.lower()
    return str == str[::-1]
frase = str(input("Insira a frase e descubra se ela é um palíndromo: "))
if palindromo(frase):
    print("Sim, essa frase é um palíndromo!")
else:
    print("Não, essa frase não é um palíndromo!")

