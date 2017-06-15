

class Personnage:
    energie_depart_defaut = 20
    energie_depart_min = 1
    energie_max = 100
    longueur_nom_min = 3
    longueur_nom_max = 30
    nom= ""
    energie_depart = 0
    energie_courante = 0

    def __init__(self, nom, energie_depart):
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

    def est_mort(self):
        """
        Retourne vrai lorsque l’énergie du personnage est à 0.
        Returns (bool): True si le personnage est mort, False sinon.
        """


    def valider_nom(self, nom):

        nom = input("Veuillez insérer le nom du personnage:")

        if len(nom) < longueur_nom_min or len(nom) > longueur_nom_max:
            return False
        else:
            return True


    def valider_energie_courante(self, energie_courante):

        energie_courante = float(input("Veuillez insérer l'énergie courante du personnage:"))

        if energie_courante < 0 or if energie_courante > energie_max:
            return False
        else:
            return True

    def valider_energie_depart(self, energie_depart):
        """
        Valide l'énergie de départ. Elle est valide lorsqu’elle est entre energie_depart_min et 
        energie_max. (bornes incluses). 
        Args:
            energie_depart (int): L'énergie de départ 

        Returns (bool): True si l'énergie de départ est valide, False sinon.
        """

    def reset_energie(self):
        """
        Remet l’énergie courante du personnage à sa valeur de départ.
        """


    def get_energie_courante(self):
        """
        Retourne l'énergie courante
        Returns (int): L'énergie courante
        """


    def set_energie_courante(self, energie_courante):
        """
        Assigne l'énergie courante si elle est valide. 
        Args:
            energie_courante (int): L'énergie courante 

        Returns (bool): True si l'assignation a réussi, False sinon.
        """


    def get_nom(self):
        """
        Retourne le nom.
        Returns (str): Le nom.
        """


    def set_nom(self, ):
        """
        Assigne le nom s'il est valide. 
        Args:
            nom (str): Le nom

        Returns (bool): True si l'assignation a réussi, False sinon.
        """


    def get_energie_depart(self):
        """
        Retourne l'énergie de départ.
        Returns (int): L'énergie de départ
        """


    def set_energie_depart(self, energie_depart):
        """
        Assigne l'énergie de départ si elle est valide. 
        Args:
            energie_depart (int): L'énergie de départ 

        Returns (bool): True si l'assignation a réussi, False sinon.
        """

    # compléter la méthode manquante