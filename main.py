import calculs
import historique
import interface

#   *** MAIN ***

# Gestion de l'interface
nom, poids, taille = interface.demander_infos()

# Gestion des calculs ** poids en KG et taille en metre(1.68)
imc = calculs.calculer_imc(poids, taille)
stat = calculs.interpreter_imc(imc)

# Afficher Résultat
interface.afficher_resultat(nom, imc, stat)

# Gestion de la sauvegarde
historique.sauvegarder_calcul(nom, imc)
historique.afficher_historique(f"{nom}.txt")