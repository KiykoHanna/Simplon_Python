import os
import time

import random
from matplotlib import pyplot as plt
import numpy as np
from IPython.display import clear_output

def func_add(a, b):
    return a + b

# function pour dessiner le pendu
def afficher_pendu(nb_tentat):
    """
    Affiche le pendu en fonction du nombre d'erreurs.
    """

    plt.figure()  # Crée une nouvelle figure

    # Dessine la potence
    plt.plot([0, 1], [0, 0], 'k')  # Base
    
    if nb_tentat < 8:
        plt.plot([0.5, 0.5], [0, 1], 'k')  # Poteau vertical
        plt.plot([0.5, 1], [1, 1], 'k')  # Barre horizontale
        plt.plot([1, 1], [0.9, 0.8], 'k')  # Corde


    # Dessine le corps du pendu en fonction du nombre d'erreurs
    if nb_tentat < 7:# Tête
        head = plt.Circle((1, 0.75), 0.05, fill=False, color='k', linewidth=2)
        plt.gca().add_patch(head)
    if nb_tentat < 6:# Corps
        corp = plt.Circle((1, 0.55), 0.1, fill=False, color='k', linewidth=2)
        plt.gca().add_patch(corp)
    if nb_tentat < 5:# Bras gauche
        plt.plot([0.9, 0.83], [0.65, 0.6], 'k')
    if nb_tentat < 4:# Bras droit
        plt.plot([1.1, 1.17], [0.65, 0.60], 'k')
    if nb_tentat < 3:# Jambe gauche
        plt.plot([0.9, 0.83], [0.45, 0.3], 'k')
    if nb_tentat < 2:# Jambe droite
        plt.plot([1.1, 1.17], [0.45, 0.3], 'k')
    if nb_tentat < 1:# Croix
        plt.plot([0.65, 1.35], [0.2, 0.9], 'k')
        plt.plot([0.65, 1.35], [0.9, 0.2], 'k')
    
    # Paramètres d'affichage
    plt.axis('off')  # Cache les axes
    plt.xlim(-0.2, 1.4)  # Ajuste les limites de l'axe x
    plt.ylim(-0.2, 1.2)  # Ajuste les limites de l'axe y
    plt.show()  # Affiche le pendu

def input_lettre():
    while True:
        try:
            lettre = str(input("Devinez une lettre"))[0]
            print(f"Vorte lettre: {lettre}")
            return lettre  
        except ValueError:
            print("Error. Reessayez")

if __name__ == "__main__":
    print(mot_masq, "\n", f"Vous avez {N_tent} tentatives restantes ")
    afficher_pendu(N_tent)

    list_de_mot = ["python", "ordinateur", "voiture", "maison", "pendu"]
    N_tent = 8

    mot = random.choice(list_de_mot)
    mot_masq = "_" * len(mot)
    while N_tent and (mot_masq != mot):
        lettre = input_lettre()
    
    
        if lettre.lower() in mot.lower():
            mot_masq =  "".join([
                mot[i] if mot[i].lower() == lettre else mot_masq[i]
                for i in range(len(mot))
                ])
            clear_output(wait=True)
            print(mot_masq, "\n", f"Vous avez {N_tent} tentatives restantes ")
            afficher_pendu(N_tent)
        
        else:
            N_tent -= 1
            clear_output(wait=True)
            print(mot_masq, "\n", f"Vous avez {N_tent} tentatives restantes ")
            afficher_pendu(N_tent)

