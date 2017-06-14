# Anthony Gagnon: 111 129 416
# Louis Cusson: 111 142 104

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

def doNothing():
    print("C'est juste un test pour le drop down menu.")

def creersorcier(): ##fenetre qui demandera saisie à l'utilisateur pour le sorcier
    fenetre2 = Tk()

def creerguerrier(): ## fenetre qui demandera saisie à l'utilisateur pour le guerrier
    fenetre3 = Tk()

# Importe les classes contenues dans le module tkinter
from tkinter import *

# utilisation de la classe Tk() qui fait apparaître une fenêtre
fenetre1 = Tk()

menu_fichier = Menu(fenetre1)
fenetre1.config(menu = menu_fichier)

subMenu1 = Menu(menu_fichier)
menu_fichier.add_cascade(label = "Fichier", menu = subMenu1)
subMenu1.add_command(label = "Ouvrir", command = doNothing)
subMenu1.add_command(label = "Enregistrer", command = doNothing)
subMenu1.add_command(label = "Enregistrer Sous", command = doNothing)
subMenu1.add_command(label = "Fermer", command = doNothing)
subMenu1.add_command(label = "Quitter", command = doNothing)

# Création d'un objet/widget avec la classe Label()
texte1 = Label(fenetre1, text = "La fenêtre principal se tient ici.", fg = "red")
texte1.pack(side = LEFT) # Activation de la méthode pack()

# Création d'un objet/widget avec la classe Button()
bouton1 = Button(fenetre1, text = "Créer un sorcier", width = 15,command = creersorcier)
bouton1.pack(side = TOP) # Activation de la méthode pack()

bouton2 = Button(fenetre1, text = "Créer un guerrier", width = 15, command=creerguerrier)
bouton2.pack(side = TOP)

bouton3 = Button(fenetre1, text = "Attaquer", width = 15)
bouton3.pack(side = TOP)

bouton4 = Button(fenetre1, text = "Réinitialiser l'énergie", width = 15)
bouton4.pack(side = TOP)

bouton5 = Button(fenetre1, text = "Crier", width = 15)
bouton5.pack(side = TOP)

# Activation de la méthode mainloop() pour garder le programme actif en permanence
fenetre1.mainloop()



