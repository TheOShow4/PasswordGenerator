# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 20:47:58 2025

@author: theodoregrosliere
"""
from random import *

string = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 
 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 
 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 
 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 
 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '!', '"', '#', 
 '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', 
 ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', 
 '|', '}', '~')

stop = True

mdp = {}

while stop == True:
    robustesse = 0
    mdptemp = []
    mdptemp2 = []
    valeur = None
    print("""\n
          1. Afficher les mots de passe.
          2. Créer un mot de passe.
          3. Créer plusieurs mots de passe.
          4. Supprimer un mot de passe.
          5. Modifier un mot de passe.
          6. Vérifier la robustesse d'un mot de passe.
          7. Sauvegarder les mots de passe dans un fichier (.txt).
          8. Afficher les critères de robustesse.
          9. Quitter.
          """)
    demande = int(input("Que voulez-vous faire : "))
    
    if demande == 1: 
        if len(mdp) != 0:
            print(f'Voici vos mots de passe : {mdp}')
        else: 
            print(f"\nVous n'avez aucun mot de passe actuellement.")
    
    elif demande == 2:
        print('\nDonnez les caractéristiques du mot de passe voulu.')
        valeur = input("\nQuel nom voulez-vous donner : ")
        longueur = int(input("Quelle longueur voulez-vous : "))
        
        for i in range(longueur):
            mdptemp.append(choice(string))
        mdp[valeur] = "".join(mdptemp)
        
    elif demande == 3:
        print('\nDonnez les caractéristiques des mots de passe voulus.')
        nombre = int(input("\nCombien de mots de passe voulez-vous créer : "))
        
        for i in range(nombre):
            mdptemp2 = []
            valeur = input("\nQuel nom voulez-vous donner : ")
            longueur = int(input("Quelle longueur voulez-vous : "))
            
            for i in range(longueur):
                mdptemp2.append(choice(string))
                
            mdp[valeur] = "".join(mdptemp2)
            print(f'\nVous avez généré un mot de passe. ')
            
    elif demande == 4:
        valeur = input('Quel mot de passe voulez-vous supprimer : ')
        if valeur in mdp:
            mdp.pop(valeur)
        else:
            print("Vous n'avez pas entré un nom valide.")
        
    elif demande == 5:
        valeur = input("Quel mot de passe voulez-vous modifier : ")
        if valeur in mdp:
            longueur = int(input("Quelle nouvelle longueur voulez-vous : "))
            mdptemp = []
            for i in range(longueur):
                mdptemp.append(choice(string))
            mdp[valeur] = "".join(mdptemp)
            print(f"\nLe mot de passe a été modifié.")
        else:
            print("Le mot de passe que vous voulez modifier n'existe pas.")
        
    elif demande == 6:
        demande2 = int(input("""
            1. Vérifier un mot de passe généré ici.
            2. Vérifier un mot de passe personnel.
                             """))
        if demande2 == 1:
            valeur = input("De quel mot de passe voulez-vous vérifier la robustesse : ")
            if valeur in mdp:
                if len(mdp[valeur]) >= 12:
                    robustesse += 1
                if any(char.isdigit() for char in mdp[valeur]):
                    robustesse += 1
                if any(char.isupper() for char in mdp[valeur]):
                    robustesse += 1
                if any(char.islower() for char in mdp[valeur]):
                    robustesse += 1
                if robustesse == 4:
                    print("\nLe mot de passe est robuste.")
                else:
                    print("\nLe mot de passe est faible.")
            else: print(f"{valeur}, n'est pas dans la liste de mot de passe.")
        elif demande2 == 2:
            valeur = input("Entrez votre mot de passe à vérifier : ")
            if len(valeur) >= 12:
                robustesse += 1
            if any(char.isdigit() for char in valeur):
                robustesse += 1
            if any(char.isupper() for char in valeur):
                robustesse += 1
            if any(char.islower() for char in valeur):
                robustesse += 1
            if robustesse == 4:
                print("\nLe mot de passe est robuste.")
            else:
                print("\nLe mot de passe est faible.")
        
    elif demande == 7:
        with open('mdp.txt', 'w', encoding='utf-8') as f:
            f.write(str(mdp))
        print("Les mots de passe ont été sauvegardés dans 'mdp.txt'.")
        
    elif demande == 8:
        print("""
        Critères de robustesse du mot de passe :
        1. La longueur doit être supérieure ou égale à 12 caractères.
        2. Le mot de passe doit contenir au moins un chiffre.
        3. Le mot de passe doit contenir au moins une lettre majuscule.
        4. Le mot de passe doit contenir au moins une lettre minuscule.
        """)
        
    elif demande == 9:
        stop = False
    
    else:
        print('Veuillez entrer un choix valide.')
