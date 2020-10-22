# quantos anos você tem ?
# *idade
# se idade < 16
# - não pode votar

idade = int(input("Quantos anos você tem ?\n"))

if idade < 16:
    print("\nSua idade é:", idade, "\nVocê ainda não pode votar")
elif idade < 18 or idade > 70:
    print("\nSua idade é:", idade, "\nSeu voto é facultativo!")
else:
    print("\nSua idade é:", idade, "\nVocê é obrigado a votar! ")

print("\nObrigado, volte sempre!")
