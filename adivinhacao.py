import random

def jogar():
    numero_secreto = random.randrange(1, 101, 1)
    total_de_tentativas = 0
    dificuldade = 0

    print("Jogo da adivinhação")
    print("Qual o nível de dificuldade do jogo?")
    dificuldade = int(input("Digite (1) Fácil (2) Médio (3) Difícil: "))

    if dificuldade == 1:
        total_de_tentativas = 20
    elif dificuldade == 2:
        total_de_tentativas = 10
    elif dificuldade == 3:
        total_de_tentativas = 5

    i = 1
    for i in range(1, total_de_tentativas+1):
        print("Tentativa {}".format(i))
        chute = int(input("Digite o seu número entre 1 e 100: "))

        if (chute < 1):
            print("O número deve ser maior do que 0.")
            continue

        acertou = chute == numero_secreto
        chute_maior = chute > numero_secreto
        chute_menor = chute < numero_secreto

        if (acertou):
            print("Você acertou!")
            break
        else:
            if (chute_maior):
                print("Você errou! O número mágico é menor do que seu chute!")
            elif (chute_menor):
                print("Você errou! O número mágico é maior do que seu chute!")

        i += 1

    print("Fim do jogo!")

if (__name__ == "__main__"):
    jogar()