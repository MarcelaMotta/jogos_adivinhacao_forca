def jogar():

    print("Jogo da forca")

    palavra_secreta = "banana"

    enforcou = False
    acertou = False

    while (not enforcou and not acertou):

        chute = input("Qual a letra?")
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            if chute.upper() == letra.upper():
                print("Encontrei a letra '{}' na posição {}".format(chute, index))
            index += 1


    print("Qual o nível de dificuldade do jogo?")
    dificuldade = int(input("Digite (1) Fácil (2) Médio (3) Difícil: "))



if (__name__ == "__main__"):
    jogar()