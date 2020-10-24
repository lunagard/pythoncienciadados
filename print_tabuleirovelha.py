X = "x"
O = "O"
VAZIO = " "
tabuleiro = [X, O, O,
             O, O, X,
             X, O, X]

alinhamento = False
vencedor = VAZIO

# Alinhamento horizontal
for i in range(0, 9, 3):
    if tabuleiro[i] == tabuleiro[i+1] == tabuleiro[i+2]:
        alinhamento = True
        vencedor = tabuleiro[i]


# Alinhamento vertical
if not alinhamento:
    for i in range(3):
        if tabuleiro[i] == tabuleiro[i+3] == tabuleiro[i+6]:
            alinhamento = True
            vencedor = tabuleiro[i]


# Alinhamento cruzado
if not alinhamento:
    for i in range(0, 3, 2):
        if tabuleiro[0+i] == tabuleiro[4] == tabuleiro[8-i]:
            alinhamento = True
            vencedor = tabuleiro[i]

if alinhamento:
    print("Vencedor:", vencedor)
else:
    if not VAZIO in tabuleiro:
        print("Deu velha: Grande clássico entre vocês!")
