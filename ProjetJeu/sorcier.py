class Sorcier( ):
    nbr_charmes_defaut=20
    nbr_charmes_max = 20
    nbr_charmes=0

    def __init__(self, nom, energie_depart, energie, nbr_charmes):

       nom = input("Veuillez donner un nom à votre sorcier")
       energie_depart = input("Veuillez entrer une énergie de départ pour votre sorcier")
       energie = input("Veuillez entrer énergie courante du sorcier")
       nbr_charmes = int(input("Veuillez entrer le nombre de charmes du sorcier"))

        """
        Le constructeur du Sorcier. Il doit initialiser le nom, l’énergie de départ, l’énergie courante et
        le nombre de charmes. NB : pensez à optimiser votre code et utiliser le constructeur de la classe parente.
        Args:
            nom: Le nom du sorcier
            energie_depart:  L'énergie de départ du sorcier
            energie: L'énergie courante du sorcier
            nbr_charmes:  Le nombre de charmes du sorcier
        """

    def to_string(self):

        print("Le sorcier,",nom ,", à une énergie de ",energie, "et",nbr_charmes,"charmes")

        """
        Retourne une chaîne du genre "Le sorcier, nom de Personnage, a une énergie de, valeur de l’énergie et,
        valeur du nombre de charmes, charmes."
        Returns (str): La chaîne représentant le Sorcier.
        """

    def valider_nbr_charmes(self, nb_charmes):

        if nb_charmes > 0 or nb_charmes < nbr_charmes_max :
            return True
        else:
            False

        """
        Valide que le nombre de charmes est positif (0 inclus) et ne doit pas dépasser nbr_charmes_max. 
        Args:
            nb_charmes (int): Le nombre de charmes à valider 

        Returns (bool): True si le nombre de charmes est valide, false sinon.
        """

    def crier(self):

        print("Je vais tous vous anéantir")

        """
        Retourne le cri du sorcier: "Je vais tous vous anéantir!"
        Returns: Le cri du sorcier
        """

    def attaquer(self, force_attaque):

        return energie-force_attaque

        if energie < force_attaque :
            energie = 0
        else:
            energie = energie-force_attaque


        """
        Lorsqu’un sorcier se fait attaquer son énergie est diminuée de la force de l’attaque. Si la force de l’attaque est
        plus grande que son énergie, l’énergie du sorcier devient 0 (il meurt). 
        Args:
            force_attaque (int): La force de l'attaque 
        """

    def get_nbr_charmes(self):

        return nbr_charmes
        """
        Retourne le nombre de charmes du sorcier.
        Returns (int): Le nombre de charmes du sorcier.

        """

    def set_nbr_charmes(self, nb_charmes):

        nb_charmes = input("Veuillez entrer le nombre de charmes du sorcier:")
        if nb_charmes > 0 or nb_charmes <nbr_charmes_max:
            return True
        else:
            return False

        """
        Assigne le nombre de charmes du sorcier. Le nombre de charmes doit être valide.
        Args:
            nb_charmes (int): Le nombre de charmes  

        Returns (bool): True si le nombre de charmes est valide et a été modifié, False sinon.
        """
