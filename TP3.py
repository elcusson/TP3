# Anthony Gagnon: 111 129 416
# Louis Cusson: 111 142 104

# NOTE: ne pas toucher aux classes "gestion_personnages" et "interface". Elles seront utilisées dans le TP4.
# Le TP3 s'occupe des données et le TP4 s'occupe de la manipulation des données.

## Definition de la classe Personnage
class Personnage: #attributs de la classe personnage
    energie_depart_defaut = 20
    energie_depart_min = 1
    energie_max = 100
    longueur_nom_min = 3
    longueur_nom_max = 30
    nom= ""
    energie_depart = 0
    energie_courante = 0

### Définition de la classe Guerrier
class Guerrier: ## les attributs de la classe guerrier
    force_defaut = 20
    force_max = 80
    perte_force_defaut=2
    gain_force_defaut = 10
    force = 0

### Définition de la classe Sorcier
class Sorcier: #attributs de la classe sorcier
    nbr_charmes_defaut=20
    nbr_charmes_max = 20
    nbr_charmes=0



