#constantes

force_defaut = 20
force_max = 80
perte_force_defaut = 2
gain_force_defaut = 10
force = 0

class Guerrier(    ):

    def __init__(self, nom, energie_depart, energie, force):
        """
        Le constructeur du Guerrier. Il doit initialiser le nom, l’énergie de départ, l’énergie courante et la force. 
        NB : pensez à optimiser votre code et utiliser le constructeur de la classe parente.
        Args:
            nom (str): Le nom du guerrier 
            energie_depart (int): L'énergie de départ du guerrier 
            energie (int): L'énergie courante du guerrier 
            force (int): La force du guerrier 
        """


    def to_string(self):
        """
        Retourne une chaîne du genre : "Le guerrier, nom de Personnage, a une énergie de valeur de 
        l’énergie et une force de valeur de la force."
 
        Returns (str): La chaîne représentant le guerrier. 
        """


    def valider_force(self, force):
        """
        Valide si la force en paramètre est valide (entre 0 et force_max inclusivement).
        Args:
            force (int): La force à valider 

        Returns (bool): True si la force est valide, False sinon
        """

    def crier(self):
        """
        Retourne le cri du guerrier : "Vous allez goûter à la puissance de mon épée!"
        Returns (str): Le cri du guerrier
        """


    def attaquer(self, force_attaque):
        """
        Lorsqu’un guerrier se fait attaquer, son énergie est diminuée de la force de l’attaque.  
        Si la force de l’attaque est plus grande que son énergie, l’énergie du guerrier devient 0 (il meurt).
        Lors d’une attaque, la force du guerrier est aussi modifiée.  Elle est diminuée, à chaque attaque, 
        de la valeur de perte_force_defaut jusqu’à concurrence de 0.  Si le guerrier meurt pendant l’attaque, 
        sa force est aussi mise à 0.
        Args:
            force_attaque (int): La force de l'attaque 
        """

    def reset_energie(self):
        """
        Permet de remettre l’énergie courante du guerrier à sa valeur de départ (héritage) et 
        augmente sa force (la valeur de force) par la valeur de gain_force_defaut jusqu’à concurrence de 
        la force maximale sans jamais la dépasser.       
        """

    # setter et getter, a vous de compléter