### Louis Cusson 111 142 104

#constantes

nbr_charmes_defaut = 20
nbr_charmes_max = 20
nbr_charmes = 0


class Sorcier( ):

    def __init__(self, nom, energie_depart, energie, nbr_charmes=nbr_charmes_defaut): # tester
        self.nom = str(nom)
        self.energie_depart = int(energie_depart)
        self.energie = int(energie)
        self.nbr_charmes = int(nbr_charmes)

        """
        Le constructeur du Sorcier. Il doit initialiser le nom, l’énergie de départ, l’énergie courante et
        le nombre de charmes. NB : pensez à optimiser votre code et utiliser le constructeur de la classe parente.
        Args:
            nom: Le nom du sorcier
            energie_depart:  L'énergie de départ du sorcier
            energie: L'énergie courante du sorcier
            nbr_charmes:  Le nombre de charmes du sorcier
        """

    def to_string(self): # tester
        print("Le sorcier ,",self.nom,", a une énergie de ",self.energie,"et ",self.nbr_charmes," charmes.")

        """
        Retourne une chaîne du genre "Le sorcier, nom de Personnage, a une énergie de, valeur de l’énergie et,
        valeur du nombre de charmes, charmes."
        Returns (str): La chaîne représentant le Sorcier.
        """

    def valider_nbr_charmes(self, nbr_charmes): # tester
        if int(nbr_charmes) > 0 and int(nbr_charmes) < nbr_charmes_max:
            return True
        else:
            return False

        """
        Valide que le nombre de charmes est positif (0 inclus) et ne doit pas dépasser nbr_charmes_max. 
        Args:
            nb_charmes (int): Le nombre de charmes à valider 

        Returns (bool): True si le nombre de charmes est valide, false sinon.
        """

    def crier(self): # tester
        print("Je vais tous vous anéantir!")

        """
        Retourne le cri du sorcier: "Je vais tous vous anéantir!"
        Returns: Le cri du sorcier
        """

    def attaquer(self, force_attaque): # tester
        if self.energie < int(force_attaque):
            self.energie = 0
        else:
            self.energie -= force_attaque
        """
        Lorsqu’un sorcier se fait attaquer son énergie est diminuée de la force de l’attaque. Si la force de l’attaque est
        plus grande que son énergie, l’énergie du sorcier devient 0 (il meurt). 
        Args:
            force_attaque (int): La force de l'attaque 
        """

    def get_nbr_charmes(self): # tester
        print(self.nbr_charmes)
        """
        Retourne le nombre de charmes du sorcier.
        Returns (int): Le nombre de charmes du sorcier.

        """

    def set_nbr_charmes(self, nbr_charmes):
        if self.valider_nbr_charmes(int(nbr_charmes)) == True:
            self.nbr_charmes = int(nbr_charmes)
            return True
        else:
            return False

        """
        Assigne le nombre de charmes du sorcier. Le nombre de charmes doit être valide.
        Args:
            nb_charmes (int): Le nombre de charmes  

        Returns (bool): True si le nombre de charmes est valide et a été modifié, False sinon.
        """

##test

## test unitaire ##
if __name__ == "__main__":

    louis = Sorcier("louis",2,3,4) #test unitaire pour la classe sorcier

assert louis.nom =="louis"  ##test si la saisie du nom est bien "louis"

assert louis.nbr_charmes == 4 #test si la saisie du nombre de charme est bien 4

assert louis.energie == 3

assert louis.energie_depart == 2

louis.set_nbr_charmes(2)

assert louis.nbr_charmes == 2

louis.nbr_charmes=20
louis = Sorcier("Louis",2,3) ## assigne des valeurs au sorcier
louis.attaquer(40)           ##force d'attaque de 40
print(louis.energie)         ## Energie courant du sorcier après l'attaque
louis.valider_nbr_charmes(3) ## Valide la valeurs de charmes entrée
louis.crier()                ## affiche le crie du sorcier
louis.set_nbr_charmes(-21)   ## nouveau nombre de charmes
louis.get_nbr_charmes()      ## affiche le nombre de charmes
louis.to_string()            ##Valide la chaine de caratère
