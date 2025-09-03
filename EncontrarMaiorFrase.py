import string

def encontrar_maior_palavra(frase):
    palavras = frase.split()
    maior_palavra = ''
    maior_tamanho = 0
    
    for palavra in palavras:
        palavra_limpa = palavra.strip(string.punctuation)
        if len(palavra_limpa) > maior_tamanho:
            maior_palavra = palavra_limpa
            maior_tamanho = len(palavra_limpa)
    
    return maior_palavra


if __name__ == "__main__":
    frase_usuario = input("Digite uma frase: ")
    
    if frase_usuario.strip():
        maior = encontrar_maior_palavra(frase_usuario)
        print(f"Maior palavra encontrada: {maior}")
    else:
        print("Nenhuma frase foi digitada.")

