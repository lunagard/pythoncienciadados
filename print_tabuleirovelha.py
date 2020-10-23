X = "x"
O = "O"
VAZIO = " "
msgVitoria = "Parabéns você venceu!"
msgEmpate = "Empate"


tabuleiro = [VAZIO, VAZIO, VAZIO,
             VAZIO, VAZIO, VAZIO,
             VAZIO, VAZIO, VAZIO]


def verificacao():
    if all(casa != VAZIO for casa in range(len(tabuleiro))):
        print(msgEmpate)
    else:
        print(casa)
        escolharPosicao = int(
            input('Digite a posição que quer "de 0 a 9": \n'))
        escolharUsuario = input('\n Escolhar "X" ou "O":')
        tabuleiro[escolharPosicao] = escolharUsuario

        # Verificação Horizontal
        if tabuleiro[0:2] == X or tabuleiro[0:2] == O:
            print(msgVitoria)
        if tabuleiro[3:5] == X or tabuleiro[3:5] == O:
            print(msgVitoria)
        if tabuleiro[6:8] == X or tabuleiro[6:8] == O:
            print(msgVitoria)

    # Verificação Vertical
        if tabuleiro[0] == tabuleiro[3] == tabuleiro[6]:
            print(msgVitoria)
        if tabuleiro[1] == tabuleiro[4] == tabuleiro[7]:
            print(msgVitoria)
        if tabuleiro[2] == tabuleiro[5] == tabuleiro[8]:
            print(msgVitoria)

    # Verificação cruzada
        if tabuleiro[2] == tabuleiro[4] == tabuleiro[6]:
            print(msgVitoria)
        if tabuleiro[0] == tabuleiro[4] == tabuleiro[8]:
            print(msgVitoria)


for casa in tabuleiro:
    verificacao()

# POSSO FAZER A VERIFIÇÃO PARA VER SE A POSIÇÃO É VAZIA ANTES E PRINTAR TODAS A POSIÇÕES DISPONIVEIS CADA VEZ QUE O USUARIO digita
# E FAZER UMA VERIFICAÇÃO QUANDO O USUARIO DIGITA


# toda vez que um usario digita um valor tera que atribuir esse valor na posição do tabuleiro que o usuario escolher. FEITO
# o jogador só pode colocar na posição que estiver vazia
# depois verificar se as posições não estão todas completas.
# se não tiver nenhum vazio  e nenhuma sequencia de 3 do mesmo valor o jogo termina empatado.
