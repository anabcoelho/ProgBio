vogal = lambda caractere: caractere.upper() in "AÁÀÂÃEÉÊIÍÎOÓÕÔUÚÛÜ" #se é vogal (com acentuação) retorna True
consoante = lambda caractere: caractere.upper() in "BCDFGHJKLMNPQRSTUVXWZ"#se é consoante retorna True
numero = lambda caractere: caractere in "1234567890" #se é numero retorna true

frase = input("Digite uma frase: ")

tvogal = 0
tconsoante = 0
tnumero = 0
toutros = 0

for caractere in frase:
    if vogal(caractere):
        tvogal += 1
    elif consoante(caractere):
        tconsoante += 1
    elif numero(caractere):
        tnumero += 1
    else:
        toutros += 1

print("Total de consoantes = %d" % tconsoante)
print("Total de vogais = %d" % tvogal)
print("Total de números = %d" % tnumero)
print("Total de outros = %d" % toutros)