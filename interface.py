# Demande poids et taille
def demander_infos():
    nom = input("\nEntrer votre nom : ")
    poids = float(input("Votre poid en kilogramme : "))
    taille = float(input("Votre taille en metre : "))
    return nom, poids, taille

def afficher_resultat(nom, imc, stat):
    print(f"\n{nom}, ton IMC est de {imc:.2f} → {stat}")


##TEST
# demander_infos()
# afficher_resultat()
