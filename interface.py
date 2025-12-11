import calculs 


def demander_infos():
    nom = input("Votre nom: ")
    poids = input("Votre poid en kilogramme: ")
    taille = input("Votre taille en metre: ")
    return nom, poids, taille
# Demande poids et taille



def afficher_resultat(nom, imc, stat):
    print(f"{nom}, ton IMC est {imc:.2f} → {stat}")
demander_infos()
afficher_resultat()
# Affiche joliment 