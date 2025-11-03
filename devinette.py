print("La devinette")

nb_secret = 31

# Convertir l'entrée utilisateur en entier
nb_utilisateur = int(input("Entrez un nombre : "))

if nb_utilisateur == nb_secret:
    print("Gagné")
else:
    print("Perdu")
