import adivinhacao
#import forca

print("Escolha qual jogo deseja jogar:")

jogo = int(input("Digite (1) Adivinhação (2) Forca: "))

if jogo == 1:
    print("Começando o jogo da adivinhação")
    adivinhacao.jogar()
elif jogo == 2:
    print("Começando o jogo da forca")