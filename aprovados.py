aprovado = [
    "Graziela Barro", "Juliano Moreira", "André Rebouças",
    "César Lattes", "Enedina Alves", "Machado de Assis",
    "Ayrton Senna", "Luiz Gama", "Ruth de Souza",
    "Nise da Silveira", "Johanna Dobereiner", "Carolina de Jesus",
    "Leopoldo Nachbin", "Antonieta de Barros", "Lima Barreto"
]

vagas = int(input("Qual número de vagas? \n"))

print("A lista, ", aprovado)
print("A primeira colocada é: ", aprovado[0])

# 1. Quantidade total de aprovados
print("O total de aprovados são", len(aprovado))

# 2. Primeira pessoa na condição de reserva
print("A primeira pessoa da reserva", aprovado[vagas])

# 3. Verifiicar se alguém está na lista
if "Graziela Barro" in aprovado:
    print("Graziela Barro está na lista")
else:
    print("Uma pena ela não está na lista")

# 4. Lista de Classificados
classificados = aprovado[:vagas]
print("Lista de Classificados\n", classificados)
# print("Lista de Classificados\n", aprovado[0:5])

# 5. Lista de reservas
reservas = aprovado[vagas:]
print("Lista de Reserva\n", reservas)

print("Último classifcado:", classificados[-1])
print("Último reserva:", reservas[-1])

# Modificar o elemento em uma determinada posição na lista
aprovado[9] = "Oswaldo Cruz"
if "Oswaldo Cruz" in aprovado:
    print("Oswaldo cruz está na lista")
else:
    print("Uma pena ela não está na lista")

classificados = aprovado[:vagas]
reservas = aprovado[vagas:]

if "Oswaldo Cruz" in reservas:
    # Fazer uma função para falar em qual posição ele ta!
    print("Ele está na lista reserva")
else:
    print("Ele não Está na lista de reserva")
print("Lista de Reserva\n", reservas)

# Adiciona um elemento ao final da lista
aprovado.append("Elon Lages")
print("\nLista completa novamente:\n", aprovado)

# Remover um elemento da lista
escolhaQuemRemover = input("Digite o nome de quem deseja remover: ")
aprovado.remove(escolhaQuemRemover)
print("\nLista novamente\n", aprovado)
