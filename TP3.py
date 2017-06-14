# Anthony Gagnon: 111 129 416
# Louis Cusson: 111 142 104

# Importe les classes contenues dans le module tkinter
from tkinter import *

# utilisation de la classe Tk() qui fait apparaître une fenêtre
fenetre1 = Tk()

# Création d'un objet/widget avec la classe Label()
texte1 = Label(fenetre1, text = "Bonjour les copains!", fg = "red")

# Activation de la méthode pack()
texte1.pack()

# Création d'un objet/widget avec la classe Button()
bouton1 = Button(fenetre1, text = "Quitter", command = fenetre1.destroy)

# Activation de la méthode pack()
bouton1.pack()

# Activation de la méthode mainloop() pour garder le programme actif en permanence
fenetre1.mainloop()