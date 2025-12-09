def calculer_imc(poids, taille):
   # IMC = poids / taille²
    return poids / taille**2

def interpreter_imc(imc):

# Retourne la catégorie
    match imc:

        case maigre if imc < 18.5:
            return "Maigre"

        case normal if 18.5 <= imc < 25:
            return "Normal"

        case surpoids if 25 <= imc < 30:
            return "Surpoids"

        case normal if 30 <= imc < 40:
            return "Obésité modérée"

        case maigre if imc <= 40:
            return "Obésité sévère"