#constantes
import math
force_defaut = 20
force_max = 80
perte_force_defaut = 2
gain_force_defaut = 10
force = 0


class Guerrier():

    def __init__(self, nom, energie_depart, energie, force = force_defaut): # tester
        self.nom = str(nom)
        self.energie_depart = int(energie_depart)
        self.energie=int(energie)
        self.force = int(force)

        """
        Le constructeur du Guerrier. Il doit initialiser le nom, l’énergie de départ, l’énergie courante et la force. 
        NB : pensez à optimiser votre code et utiliser le constructeur de la classe parente.
        Args:
            nom (str): Le nom du guerrier 
            energie_depart (int): L'énergie de départ du guerrier 
            energie (int): L'énergie courante du guerrier 
            force (int): La force du guerrier 
        """


    def to_string(self): # tester
        print("Le guerrier, ", self.nom, ", a une énergie de ", self.energie, " et une force de ", self.force, ".", sep="")
        """
        Retourne une chaîne du genre : "Le guerrier, nom de Personnage, a une énergie de valeur de 
        l’énergie et une force de valeur de la force."
 
        Returns (str): La chaîne représentant le guerrier. 
        """


    def valider_force(self, force): # tester
        if int(force) > 0 and int(force) < force_max:
            return True
        else:
            return False

        """
        Valide si la force en paramètre est valide (entre 0 et force_max inclusivement).
        Args:
            force (int): La force à valider 

        Returns (bool): True si la force est valide, False sinon
        """

    def crier(self): # tester
        print("Vous allez goûter à la puissance de mon épée!")
        """
        Retourne le cri du guerrier : "Vous allez goûter à la puissance de mon épée!"
        Returns (str): Le cri du guerrier
        """


    def attaquer(self, force_attaque): # tester
        if self.energie < int(force_attaque):
            self.energie = 0
            self.force = 0
        else:
            self.energie -= int(force_attaque)
            self.force = max(self.force - perte_force_defaut, 0)
        """
        Lorsqu’un guerrier se fait attaquer, son énergie est diminuée de la force de l’attaque.  
        Si la force de l’attaque est plus grande que son énergie, l’énergie du guerrier devient 0 (il meurt).
        Lors d’une attaque, la force du guerrier est aussi modifiée.  Elle est diminuée, à chaque attaque, 
        de la valeur de perte_force_defaut jusqu’à concurrence de 0.  Si le guerrier meurt pendant l’attaque, 
        sa force est aussi mise à 0.
        Args:
            force_attaque (int): La force de l'attaque 
        """

    def reset_energie(self): # tester
        self.energie = self.energie_depart
        self.force = min(self.force + gain_force_defaut, force_max)

        """
        Permet de remettre l’énergie courante du guerrier à sa valeur de départ (héritage) et 
        augmente sa force (la valeur de force) par la valeur de gain_force_defaut jusqu’à concurrence de 
        la force maximale sans jamais la dépasser.       
        """

    # setter et getter, a vous de compléter


## Test Unitaire ##
if __name__ == "__main__":

    ##méthode __init___
    baltazar = Guerrier("baltazar",40,20,30)



