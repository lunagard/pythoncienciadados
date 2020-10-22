X = "x"
O = "O"
VAZIO = " "
msgVitoria = "Parabéns você venceu!"
msgEmpate = "Empate"


tabuleiro = [VAZIO, VAZIO, VAZIO,
             VAZIO, VAZIO, VAZIO,
             VAZIO, VAZIO, VAZIO]

for casa in tabuleiro:
        #while tabuleiro[]
    if casa == VAZIO:
        escolharPosicao = int(input('Digite a posição que quer "de 0 a 9":\n'))
        escolharUsuario = input('\nEscolhar "X" ou "O":')
        tabuleiro[escolharPosicao] = escolharUsuario
        # Verificação Horizontal
        if tabuleiro[0:2] == X or tabuleiro[0:2] == O:
            print(msgVitoria)
        if tabuleiro[3:5] == X or tabuleiro[3:5] == O:
            print(msgVitoria)
        if tabuleiro[6:8] == X or tabuleiro[6:8] == O :
            print(msgVitoria)

        # Verificação Vertical
        if (tabuleiro[0]== X or tabuleiro[0]== O) and == (tabuleiro[3]== X or tabuleiro[3]== O) and == (tabuleiro[6]== X or tabuleiro[6]== O):
            print(msgVitoria)
        if (tabuleiro[1]== X or tabuleiro[1]== O) and == (tabuleiro[4]== K or tabuleiro[4]== O) and == (tabuleiro[7]== K or tabuleiro[7]== O):
            print(msgVitoria)
        if (tabuleiro[2]== K or tabuleiro[2]== O) and == (tabuleiro[5]== K or tabuleiro[5]== O) and ==  (tabuleiro[8]== K or tabuleiro[8]== O):
            print(msgVitoria)

        # Verificação cruzada
        if tabuleiro[2]== tabuleiro[4] == tabuleiro[6]: # TEm q fazer teste por que se é desse jeito, talvez com vazio dê erro
            print("Jogo acabou")
        if tabuleiro[0]== tabuleiro[4] == tabuleiro[8]:
            print("Jogo acabou")

            0 1 2
            3 4 5
            6 7 8

        PRINT(casa)
    else:
        print("A casa não está vazia")
        Aqui verificar se não aconteceu um empate
        }if tabuleiro



# POSSO FAZER A VERIFIÇÃO PARA VER SE A POSIÇÃO É VAZIA ANTES E PRINTAR TODAS A POSIÇÕES DISPONIVEIS CADA VEZ QUE O USUARIO digita
#E FAZER UMA VERIFICAÇÃO QUANDO O USUARIO DIGITA



#toda vez que um usario digita um valor tera que atribuir esse valor na posição do tabuleiro que o usuario escolher. FEITO
# o jogador só pode colocar na posição que estiver vazia
# depois verificar se as posições não estão todas completas.
# se não tiver nenhum vazio  e nenhuma sequencia de 3 do mesmo valor o jogo termina empatado.
