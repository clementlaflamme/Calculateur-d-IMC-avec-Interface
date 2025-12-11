def calculer_imc(poids, taille):
   # IMC = poids(KG) / taille(metre ex.: 1.68)²
    return int(poids / taille**2)

def interpreter_imc(imc):

# Retourne la catégorie
    match imc:

        case maigre if imc < 18.5:
            return "Maigre"

        case normal if 18.5 <= imc < 25:
            return "Normal"

        case surpoids if 25 <= imc < 30:
            return "Surpoids"

        case obesite_moderee if 30 <= imc < 40:
            return "Obésité modérée"

        case obesitee_severe if imc <= 40:
            return "Obésité sévère"
        
