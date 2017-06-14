# Anthony Gagnon: 111 129 416
# Louis Cusson: 111 142 104

# Importe les classes contenues dans le module tkinter
from tkinter import *

# utilisation de la classe Tk() qui fait apparaître une fenêtre
fenetre1 = Tk()

# Création d'un objet/widget avec la classe Label()
texte1 = Label(fenetre1, text = "La fenêtre principal se tient ici.", fg = "red")
texte1.pack(side = LEFT) # Activation de la méthode pack()

# Création d'un objet/widget avec la classe Button()
bouton1 = Button(fenetre1, text = "Créer un sorcier", width = 15)
bouton1.pack(side = TOP) # Activation de la méthode pack()

bouton2 = Button(fenetre1, text = "Créer un guerrier", width = 15)
bouton2.pack(side = TOP)

bouton3 = Button(fenetre1, text = "Attaquer", width = 15)
bouton3.pack(side = TOP)

bouton4 = Button(fenetre1, text = "Réinitialiser l'énergie", width = 15)
bouton4.pack(side = TOP)

bouton5 = Button(fenetre1, text = "Crier", width = 15)
bouton5.pack(side = TOP)

# Activation de la méthode mainloop() pour garder le programme actif en permanence
fenetre1.mainloop()