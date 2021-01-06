def z_casino():
    from random import randrange
    pot = 1000
    continuer = "Y"
    print("vous vous installez à la table avec un pot de 1000")

    while pot > 0:
        # Choix du numéro sur lequel miser, vérification de ce numéro et re-saisie si erreur
        numero = int(input("Sur quel numéro souhaitez vous miser (entre 0 et 49) : "))
        if numero not in range(50):
            numero = int(input("Merci de saisir un numéro entre 0 et 49 : "))

        # Détermination couleur
        if numero % 2 == 0:
            couleur = "noir"
        else:
            couleur = "rouge"

        # Choix de la mise, vérification du montant et re-saisie si erreur
        mise = int(input("Montant de votre mise : "))
        if mise > pot:
            print("vous disposez actuellement de {}".format(pot))
            mise = input("Veuillez saisir une mise inférieur ou égale à ce montant :")

        # Tirage au sort
        num_tirage = randrange(50)
        print(num_tirage)

        if num_tirage % 2 == 0:
            coul_tirage = "noir"
        else:
            coul_tirage = "rouge"

        # Gain ou perte
        if num_tirage == numero:
            pot += mise * 2
        elif coul_tirage == couleur:
            pot += mise / 2
        else:
            pot -= mise

        print("votre pot est désormais de :{}".format(pot))
        continuer = input("Voulez-vous continuer de jouer (Y or N) ?")
        continuer = str.upper(continuer)
        if continuer == "N":
            print("Merci d'avoir jouer à Z_casino, vous repartez avec la somme de {} à bientôt".format(pot))

    # fin de partie, rejouer ou non

    print("La partie est terminée vous n'avez plus d'argent")
    nouvelle_partie = input("Voulez-vous refaire une partie (Y or N) ?")
    nouvelle_partie = str.upper(nouvelle_partie)
    if nouvelle_partie == "Y":
        z_casino()
    elif nouvelle_partie == "N":
        print("Merci d'avoir jouer à Z_casino, à bientôt")
    else:
        print("je n'ai pas compris que voulez-vous faire ?")
        nouvelle_partie = input("Voulez-vous refaire une partie (Y or N) ?")

z_casino()