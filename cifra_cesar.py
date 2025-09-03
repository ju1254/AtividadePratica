ALFABETO = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def cifra_de_cesar(cifra, salto):
    decifra = []
    for letra in cifra:
        if letra in ALFABETO:
            id = ALFABETO.index(letra)
            if (id + salto) >= len(ALFABETO):
                nova_letra = (id + salto) % len(ALFABETO)
                decifra.append(ALFABETO[nova_letra])
            else:
                nova_letra = id + salto
                decifra.append(ALFABETO[nova_letra])
        else:
            decifra.append(letra)
    print("".join(decifra))



cifra = input("Digite a cifra: ")
salto = int(input("Digite o salto da cifra: "))

cifra_de_cesar(cifra,salto)

cifra_de_cesar("oi",1)

cifra_de_cesar("pj",-1)