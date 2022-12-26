import random

def jogar():

    print("Jogo da forca")

    palavras = []

    with open("palavras.txt") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)

    numero_randomico = random.randrange(0,len(palavras))
    palavra_secreta = palavras[numero_randomico]

    palavra_secreta = palavra_secreta.upper()
    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0

    while (not enforcou and not acertou):

        chute = input("Qual a letra?")
        chute = chute.strip().upper()

        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if chute == letra:
                    print("Encontrei a letra '{}' na posição {}".format(chute, index))
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if acertou:
        print("Parabéns! Você acertou!")
    else:
        print("Você excedeu o número de tentativas.")


    print("Fim do jogo!")



if (__name__ == "__main__"):
    jogar()