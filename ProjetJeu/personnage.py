#constantes

energie_depart_defaut = 20
energie_depart_min = 1
energie_max = 100
longueur_nom_min = 3
longueur_nom_max = 30
nom= ""
energie_depart = 0
energie_courante = 0


class Personnage:

    def __init__(self, nom = nom, energie_depart = energie_depart_defaut): # constructeur tester
        self.nom = str(nom)
        self.energie_depart = int(energie_depart)

        """
        Le constructeur du Personnage. Il doit initialiser le nom, l’énergie de départ et l’énergie courante. 
        À la création d’un objet personnage, l’énergie courante égale à l’énergie de départ.
        Args:
            nom (str): Le nom du personnage  
            energie_depart (int): L'énergie de départ 
        """

    def crier(self):
        """
        Méthode abstraite (sans code) utile pour l’héritage, cela forcera la classe dérivée à surcharger 
        la méthode (polymorphisme).
        """

    def attaquer(self, force_attaque):
        """
        Méthode abstraite (sans code) utile pour l’héritage, cela forcera la classe dérivée à surcharger 
        la méthode (polymorphisme).
        """

    def est_mort(self): # tester
        if self.energie_courante <= 0:
            print("True")
        else:
            print("False")

        """
        Retourne vrai lorsque l’énergie du personnage est à 0.
        Returns (bool): True si le personnage est mort, False sinon.
        """


    def valider_nom(self, nom): # tester
        self.nom = str(nom)
        if len(self.nom) < longueur_nom_min or len(self.nom) > longueur_nom_max:
            print("False")
        else:
            print("True")


    def valider_energie_courante(self, energie_courante): # tester
        self.energie_courante = int(energie_courante)
        if energie_courante < 0 or energie_courante > energie_max:
            print("False")
        else:
            print("True")

    def valider_energie_depart(self, energie_depart): # tester
        self.energie_depart = int(energie_depart)
        if self.energie_depart < energie_depart_min or self.energie_depart > energie_max:
            print("False")
        else:
            print("True")

        """
        Valide l'énergie de départ. Elle est valide lorsqu’elle est entre energie_depart_min et 
        energie_max. (bornes incluses). 
        Args:
            energie_depart (int): L'énergie de départ 

        Returns (bool): True si l'énergie de départ est valide, False sinon.
        """

    def reset_energie(self): # tester
        self.energie_courante = self.energie_depart
        """
        Remet l’énergie courante du personnage à sa valeur de départ.
        """


    def get_energie_courante(self): # tester
        print(self.energie_courante)
        """
        Retourne l'énergie courante
        Returns (int): L'énergie courante
        """


    def set_energie_courante(self, energie_courante): # tester
        self.energie_courante = int(energie_courante)
        print("True ou False...")


        """
        Assigne l'énergie courante si elle est valide. 
        Args:
            energie_courante (int): L'énergie courante 

        Returns (bool): True si l'assignation a réussi, False sinon.
        """


    def get_nom(self): # tester
        print(self.nom)

        """
        Retourne le nom.
        Returns (str): Le nom.
        """


    def set_nom(self, nom): # tester
        self.nom = str(nom)
        print("True ou False...")

        """
        Assigne le nom s'il est valide. 
        Args:
            nom (str): Le nom

        Returns (bool): True si l'assignation a réussi, False sinon.
        """


    def get_energie_depart(self): # tester
        print(self.energie_depart)

        """
        Retourne l'énergie de départ.
        Returns (int): L'énergie de départ
        """


    def set_energie_depart(self, energie_depart): # tester
        self.energie_depart = int(energie_depart)
        print("True ou False...")
        """
        Assigne l'énergie de départ si elle est valide. 
        Args:
            energie_depart (int): L'énergie de départ 

        Returns (bool): True si l'assignation a réussi, False sinon.
        """

    # compléter la méthode manquante

if __name__ == "__main__":
    tony = Personnage()                                         # J'insère les valeurs de départ

############## VOILÀ UN TEST UNITAIRE (VOIR TD 13 JUIN 2017)
    assert tony.nom == ""

    tony.set_nom("Anthony Gagnon")                              # Je set un nom

    assert tony.nom == "Anthony Gagnon"

############# FIN DU TEST UNITAIRE


    tony.valider_nom("Anthony Gagnon")                          # Je donne un nom
    tony.valider_energie_depart(5)                              # Je valide une valeur pour l'énergie au départ
    tony.valider_energie_courante(20)                           # Je valide une valeur pour l'énergie au cours du programme
    tony.est_mort()                                             # Je vérifie si le personnage est mort
    tony.set_energie_courante(-1)                               # Je donne une nouvelle valeur d'énergie négative
    tony.est_mort()                                             # Je suis maintenant mort
    tony.get_nom()                                              # Je print le nom
    tony.set_nom("Tony Malone")                                 # Je set un nouveau nom
    tony.get_nom()                                              # Je print le nouveau nom
    tony.get_energie_depart()                                   # Je print l'énergie de départ
    tony.set_energie_depart(10)                                 # J'insère une nouvelle valeur pour l'énergie de départ
    tony.reset_energie()                                        # Je remets l'énergie à sa valeur de départ
    tony.get_energie_courante()                                 # Je print l'énergie courante