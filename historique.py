# sauvegarde dans un fichier au format nom.txt

def sauvegarder_calcul(nom, imc):
    file = open(f"{nom}.txt", 'w')
    file.write(f"""=-=-= Calcul de l'IMC =-=-=\n
    Nom: {nom}
    IMC: {imc}
    """)
    file.close()

# lecture d'un fichier créé précédemment
def afficher_historique(file):
    file = open(file)
    # print(file.read())
    file.close()

# #tests
# sauvegarder_calcul("Math", "81")
# afficher_historique("Math.txt")
