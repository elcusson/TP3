# Jeux d'essai

#A)
# Essai #1  32 Fahrenheit -> 0 Celsius
# Essai #2 0 Fahrenheit -> -17.78 Celsius
# Essai #3 80 Fahrenheit -> 26.67 Celsius

#B)
# Essai #1   Rayon = 15 -> Aire = 706.86
# Essai #2   Rayon = 20 -> Aire = 1256.64

#C)
#Essai #1 exam1 = 15, exam2 = 30, exam3 = 100 -> notefinale = 66.25%
#Essai #2 exam1 = 100, exam2 = 90, exam3 = 30 -> notefinale = 58.5%

#D)
#Essai #1  heures = 38 -> cout = 24$
#Essai #2 heures = 76 -> cout = 42$

#E)
#Essai # 1 passagers = 0, consommation = 7, distance = 2000, prixessence = 1.20 ->
                                        # nblitresconsommés = 140, prix aller = 168$, prix aller-retour = 336$
#Essai # 2 passagers = 3, consommation = 9, distance = 1000, prixessence = 1.10 ->
                                        # nblitresconsommés = 103.5, prix aller = 113.85$, prix aller-retour = 227.7$

import math #Pour pouvoir utiliser les fonctions du package math

def Notefinale(exam1 ,exam2 , exam3): # fonction qui traite affiche la note finale basée sur les résultats demandés
    notefinale = 0.15 * exam1 + 0.30 * exam2 + exam3*0.55
    return notefinale

choixutilisateur = "m" #On affiche les options lors du début du programme

while choixutilisateur == "M" or choixutilisateur == "m": #Tant que l'utilisateur n'aura pas fait de choix les options vont être affichées
    print("Veuillez choisir parmi les options suivantes:", "\n A = Convertir Fahrenheit en Celsius;",
          "\n B = Calculer Aire cercle;", "\n C = Calculer et afficher note finale;", "\n D = Calculer et afficher le montant pour le stationnement;",
          "\n E = Calculer le cout d'un voyage;", "\n M = Réafficher les options du menu;", "\n Q = Quitter le programme.")

    # Initialisation
    choixutilisateur = input()

    # (A) Conversion de température (Fahrenheit en Celsius)

    if choixutilisateur == "A" or choixutilisateur == "a":
        Fahrenheit = int(input("Veuillez entrer une température en Fahrenheit"))
        print(Fahrenheit, "degrés Fahrenheit est l'équivalent à", round((float(Fahrenheit)-32)*5/9, 2), "degrés Celsius.")
        print() # Espace pour meilleure visibilité
        choixutilisateur = "M"

    # (B) Calcul Aire du cercle

    elif choixutilisateur == "B" or choixutilisateur == "b":
        rayon = int(input("Veuillez entrer la valeur d'un rayon"))
        Aire = round(math.pi * float(rayon) ** 2, 2)
        print("L'aire du cercle est de ", Aire,"unités" )
        print() # Espace pour meilleure visibilité
        choixutilisateur = "M"

    # (C) Calculer et afficher note finale
    elif choixutilisateur == "C" or choixutilisateur == "c":

        exam1 = float(input("Veuillez entrez la note de votre premier examen"))
        while exam1 < 0 or exam1 > 100: #tant que les notes ne sont pas valides on demande à l'utilisateur
            exam1 = float(input("Veuillez entrer une note entre 0 et 100 pour votre premier examen"))
        else:
            exam1 = exam1
        exam2 = float(input("Veuillez entrez la note de votre deuxième examen"))
        while exam2 < 0 or exam2 > 100:
            exam2 = float(input("Veuillez entrer une note entre 0 et 100 pour votre deuxième examen"))
        else:
            exam2 = exam2
        exam3 = float(input("Veuillez entre la note de votre examen final"))
        while exam3 < 0 or exam3 > 100:
            exam3 = float(input("Veuillez entrer une note entre 0 et 100 pour votre examen final"))
        else:
            exam3=exam3
        print("La note finale obtenue est de", Notefinale(exam1,exam2,exam3), "%.")
        print() #Espace pour meilleure visibilité
        choixutilisateur = "M"

    # (D) Calculer et afficher le montant pour le stationnement

    elif choixutilisateur == "D" or choixutilisateur == "d":
        heures = int(input("Veuillez entrer une nombre d'heures de stationnement"))

        if float(heures % 24) > 0 and float(heures % 24) <= 3:
            tarif = 5
        elif float(heures % 24) > 3:
            tarif = min(5+(float(heures % 24)-3), 12)
        elif float(heures) < 0:
            heures = 0
            tarif = 0
        else:
            tarif = 0

        print("Le cout s'élève à un montant de", (heures // 24) * 12 + tarif , "$.")
        print()#espace pour meilleure visibilité
        choixutilisateur = "M"

    # (E) Coût pour le voyage

    elif choixutilisateur == "E" or choixutilisateur == "e":
        passagers = int(input("Veuillez entrer le nombre de passagers dans votre véhicule (excluant le conducteur) :"))
        while passagers < 0:
            passagers = int(input("Veuillez entrer un nombre de passagers valide"))
        else:
            passagers=passagers

        consommation = float(input("Veuillez entrer la consommation d’essence de votre véhicule (litres/100km):"))
        distance = float(input("Veuillez entrer la distance pour vous rendre à destination (km):"))
        prix = float(input("Veuillez entrer le prix de l'essence ($/litre):"))
        print("\n Voici quelques informations concernant votre voyage:"
              , "\nLe nombre de passagers est de :", passagers,"passager;"
              , "\nLa consommation d'essence avec les occupants du véhicules mentionnés est de:", round(consommation *(1+0.05*passagers), 2), "litres/100km;"
              , "\nLa distance pour vous rendre à destination est :", distance, "km;"
              , "\nLe prix de l'essence que vous avez indiqué est de :", prix, "$/litre;"
              , "\nLe nombre de litres consommés pour un aller simple est de :", round(consommation/100*(1+0.05*passagers)*distance, 2), "litres;"
              , "\nLe prix du voyage pour un aller simple est de :", round(prix*(consommation/100*(1+0.05*passagers) * distance), 2), "$;"
              , "\nLe prix du voyage aller-retour est donc de :", round(2*prix*(consommation/100*(1+0.05*passagers) *distance), 2), "$.")
        print() #espace pour meilleure visibilité
        choixutilisateur = "m"


    # (M) Réafficher les options menu

    elif choixutilisateur == "M" or choixutilisateur == "m":
        print()#espace

    # (Q) Quitter le programme

    elif choixutilisateur == "Q" or choixutilisateur == "q":
        print("À la prochaine.")

    # Si l'utilisateur fait un choix de lettre qui n'est pas énoncé

    else:
        print("La réponse que vous avez entrée est invalide. Veuillez essayer de nouveau.")
        print() #espace
        choixutilisateur = "M" #réaffiche les options
