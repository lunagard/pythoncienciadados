X = "x"
O = "O"
VAZIO = " "


tabuleiro = [0, 1, 2,
             3, 4, 5
             6, 7, 8]

# Alinhamento horizontal
if tabuleiro[0]== tabuleiro[1] == tabuleiro[2]:
    print("Jogo acabou")
if tabuleiro[3]== tabuleiro[4] == tabuleiro[5]:
    print("Jogo acabou")
if tabuleiro[6]== tabuleiro[7] == tabuleiro[8]:
    print("Jogo acabou")

# Alinhamento vertical
if tabuleiro[0]== tabuleiro[3] == tabuleiro[6]:
    print("Jogo acabou")
if tabuleiro[1]== tabuleiro[4] == tabuleiro[7]:
    print("Jogo acabou")
if tabuleiro[2]== tabuleiro[5] == tabuleiro[8]:
    print("Jogo acabou")

# Alinhamento cruzado
if tabuleiro[2]== tabuleiro[4] == tabuleiro[6]:
    print("Jogo acabou")
if tabuleiro[0]== tabuleiro[4] == tabuleiro[8]:
    print("Jogo acabou")


# como eu pretendia resolvver
#for tabuleiro range
#if tabuleiro range == 3:
#    print("Jogo acabou")
