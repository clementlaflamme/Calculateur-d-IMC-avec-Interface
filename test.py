import calculs
import historique
import interface

# Demande des infos une seule fois
nom, poids, taille = interface.demander_infos()

# Calcul de l'IMC
imc = calculs.calculer_imc(poids, taille)

# Interprétation
stat = calculs.interpreter_imc(imc)

# Affichage
interface.afficher_resultat(nom, imc, stat)

# Historique

historique.sauvegarder_calcul(nom, imc)

# historique.afficher_historique(f"{nom}.txt")

