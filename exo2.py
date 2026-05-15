import csv

def charger_pokémons_csv(fichier):

    pokemons = {}

    with open(fichier, "r", encoding="utf-8") as f:

        lecteur_csv = csv.reader(f)

        for ligne in lecteur_csv:

            nom = ligne[0]

            stats = []

            for valeur in ligne[1:]:
                stats.append(int(valeur))

            pokemons[nom] = stats

    return pokemons


resultat = charger_pokémons_csv("pokemon.csv")

print(resultat)