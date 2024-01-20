

import random

def escolher_palavra():
    palavras = ["python", "programacao", "computador", "desenvolvimento", "linguagem"]
    return random.choice(palavras)

def exibir_palavra_secreta(palavra, letras_corretas):
    return ' '.join(letra if letra in letras_corretas else '_' for letra in palavra)

def jogo_forca():
    palavra_secreta = escolher_palavra()
    letras_corretas = set()
    tentativas_maximas = 6
    erros = 0

    print("Bem-vindo ao Jogo da Forca!")

    while erros < tentativas_maximas:
        print("\nPalavra: ", exibir_palavra_secreta(palavra_secreta, letras_corretas))
        letra = input("Digite uma letra: ").lower()

        if letra in letras_corretas:
            print("Você já tentou essa letra. Tente outra.")
        elif letra in palavra_secreta:
            letras_corretas.add(letra)
            if set(letras_corretas) == set(palavra_secreta):
                print("Parabéns! Você acertou a palavra!")
                break
        else:
            erros += 1
            print(f"Letra '{letra}' não está na palavra. Tentativas restantes: {tentativas_maximas - erros}")

    if erros == tentativas_maximas:
        print(f"Fim do jogo. Você excedeu o número máximo de tentativas. A palavra secreta era: {palavra_secreta}")

if __name__ == "__main__":
    jogo_forca()
