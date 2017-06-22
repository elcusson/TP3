### Louis Cusson 111 142 104
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

    def __init__(self, nom=nom, energie_depart=energie_depart_defaut): # constructeur tester
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
            return True
        else:
            return False

        """
        Retourne vrai lorsque l’énergie du personnage est à 0.
        Returns (bool): True si le personnage est mort, False sinon.
        """


    def valider_nom(self, nom): # tester
        if len(str(nom)) < longueur_nom_min or len(str(nom)) > longueur_nom_max:
            return False
        else:
            return True

        """
        Valide le nom du personnage. Un nom de personnage est valide lorsqu’il a la bonne longueur 
        (entre min et max) bornes incluses.
        Args:
            nom (str): Le nom à valider

        Returns (bool): True si le nom est valide, False sinon.
        """


    def valider_energie_courante(self, energie_courante): # tester
        if int(energie_courante) < 0 or int(energie_courante) > energie_max:
            return False
        else:
            return True

        """
        Valide l'énergie courante. Elle doit être positive (0 inclus) et ne doit pas dépasser energie_max.
        Args:
            energie_courante (int): L'énergie à valider.

        Returns (bool): True si l'énergie est valide, False sinon.
        """

    def valider_energie_depart(self, energie_depart): # tester
        if int(energie_depart) < energie_depart_min or int(energie_depart) > energie_max:
            return False
        else:
            return True

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


    def get_energie_courante(self): #
        print(self.energie_courante)
        """
        Retourne l'énergie courante
        Returns (int): L'énergie courante
        """


    def set_energie_courante(self, energie_courante): # tester
        if self.valider_energie_courante(int(energie_courante)) == True:
            self.energie_courante = int(energie_courante)
            return True
        else:
            return False


        """
        Assigne l'énergie courante si elle est valide. 
        Args:
            energie_courante (int): L'énergie courante 

        Returns (bool): True si l'assignation a réussi, False sinon.
        """


    def get_nom(self): #
        print(self.nom)

        """
        Retourne le nom.
        Returns (str): Le nom.
        """


    def set_nom(self, nom): # tester
        if self.valider_nom(str(nom)) == True:
            self.nom = str(nom)
            return True
        else:
            return False

        """
        Assigne le nom s'il est valide. 
        Args:
            nom (str): Le nom

        Returns (bool): True si l'assignation a réussi, False sinon.
        """


    def get_energie_depart(self): #
        print(self.energie_depart)

        """
        Retourne l'énergie de départ.
        Returns (int): L'énergie de départ
        """


    def set_energie_depart(self, energie_depart): # tester
        if self.valider_energie_depart(int(energie_depart)) == True:
            self.energie_depart = int(energie_depart)
            return True
        else:
            return False

        """
        Assigne l'énergie de départ si elle est valide. 
        Args:
            energie_depart (int): L'énergie de départ 

        Returns (bool): True si l'assignation a réussi, False sinon.
        """

    # compléter la méthode manquante

if __name__ == "__main__":

    # méthode __init__
    tony = Personnage()                                         # J'insère les valeurs de départ
    assert tony.nom == ""                                       # Je vérifie si les variables de mon objet correspondent aux valeurs initiales
    assert tony.energie_depart == energie_depart_defaut

    # méthode set_nom
    tony.set_nom("Anthony Gagnon")                              # Je set un nom
    assert tony.nom == "Anthony Gagnon"                         # Je vérifie si la variable fonctionne bien
    tony.set_nom("Mo")
    assert tony.nom == "Anthony Gagnon"

    # méthode set_énergie_depart
    tony.set_energie_depart(89)
    assert tony.energie_depart == 89
    tony.set_energie_depart(-4)
    assert tony.energie_depart == 89

    # méthode set_énergie_courante
    tony.set_energie_courante(89-9)
    assert tony.energie_courante == 80
    tony.set_energie_courante(9999)
    assert tony.energie_courante == 80

    # méthode est_mort
    tony.energie_courante = -3
    assert tony.est_mort() == True

    # méthode reset_energie
    tony.reset_energie()
    assert energie_courante == energie_depart