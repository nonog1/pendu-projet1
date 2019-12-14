# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 10:32:43 2019

@author: Elève
"""

import random
liste=["eau","bonjour","astronaute","hauteur","fraction","poumon","vote","nature","bagage","rapide","langue","dragon","jouet","fin","encore","centre","pendu","populaire","semaine","armure","livre","canard"]

def choisirmot():                           #fonction qui permet de choisir un mot et d'afficher les underscores
    global mot
    global taille
    global motlist
    global motlist2
    mot=""
    mot=random.choice(liste)                #choisie un mot aléatoirement dans la liste
    taille=len(mot)                         #compte le nombre de lettre dans le mot
    motlist=list(mot)                       #créé une liste avec chaque caractères du mot
    motlist2=list(mot)
    i=0
    while i<taille:                         #boucle qui affiche les underscores
        print("_ ", end="")                 #le (, end="") permet de les écrires à la suite, ne pas revenir à la ligne
        i=i+1


caractereMaj=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
caractereMin=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"] 
 
def verificationlettre():                   #vérifie si la saisie est une minuscule
    global lettre                           #permet d'utiliser la variable lettre hors de cette fonction
    global saisie    
    verif=saisie in caractereMaj            #si saisie est dans la liste caractereMaj
    if verif==True:
        saisie=(saisie.lower())             #convertir majuscule en minuscule
    verif2= saisie in caractereMin
    if verif2==True:                        #confirme que la convertion à eu lieu et que la saisie est bien une lettre et non un caractère
        lettre=True
    else:
        print("vous n'avez pas saisi une lettre, merci de recommencer")
        lettre=False



def comparaisonlettre():                    #compare si la lettre saisie se trouve dans le mot
    global nb_vie
    global nb_trouve
    global lettre_dans_mot
    global lettre_deja_saisie
    if saisie in lettre_deja_saisie:
        print("vous avez déjà saisie cette lettre")
        lettre_dans_mot=False
    else:
        if saisie in motlist:                   #si la saisie est dans la liste qui contient chaque caractère du mot
            print("Vous avez trouvé une lettre !")
            nb_trouve=nb_trouve+1               #Le nombre de lettres trouvés augmente
            motlist.remove(saisie)              #On supprime le caractère saisie de la liste pour éviter d'avoir plusieurs fois la même lettre
            lettre_dans_mot=True    
        else:
            print("cette lettre n'est pas présente dans le mot")
            nb_vie=nb_vie-1                     #perdre une vie
            lettre_dans_mot=False


def affichagemot():                         #permet d'afficher le mot lorsq'une lettre est trouvée
    global lettre_dans_mot
    global tiret
    global affichage_tiret
    if lettre_dans_mot==True:
        while saisie in motlist2:
            position_lettre=motlist2.index(saisie)
            motlist2[position_lettre]="_"
            tiret[position_lettre]=saisie
            affichage_tiret=' '.join(tiret)
            print(affichage_tiret)
    else:
        try:
            print(affichage_tiret)
        except:
            i=0
            while i<taille:
                print("_ ", end="")                 
                i=i+1

def hommependu():
    global nb_vie
    if nb_vie==6:
        print("_______")
    if nb_vie==5:
        print("   |    ")
        print("   |    ")
        print("   |    ")
        print("   |    ")
        print("___|____")
    if nb_vie==4:
        print("    ________")
        print("   |    ")
        print("   |    ")
        print("   |    ")
        print("   |    ")
        print("___|____")
    if nb_vie==3:
        print("    ________  ")
        print("   |        | ")
        print("   |          ")
        print("   |          ")
        print("   |          ")
        print("___|____      ")  
    if nb_vie==2:
        print("    ________  ")
        print("   |        | ")
        print("   |        O ")
        print("   |          ")
        print("   |          ")
        print("___|____      ")  
    if nb_vie==1:
        print("    ________  ")
        print("   |        | ")
        print("   |        O ")
        print("   |       /|\ ")
        print("   |          ")
        print("___|____      ")  
    if nb_vie==0:
        print("    ________  ")
        print("   |        | ")
        print("   |        O ")
        print("   |       /|\ ")
        print("   |       /\ ")
        print("___|____      ")  
        nb_vie=-1


try :
    del affichage_tiret
except:
    print("")
choisirmot()
lettre_dans_mot=False
lettre_deja_saisie=[]
nb_trouve=0
nb_vie=7    
lettres_trouve=[]
lettres_fausse=[]
tiret=["_"]*taille
while nb_trouve<taille:    
    saisie=input("saisir une lettre:")
    verificationlettre()
    if lettre==True:
        comparaisonlettre()
        lettre_deja_saisie+=[saisie]
        if lettre_dans_mot==True:
            hommependu()
            print("")
            affichagemot()
        else:
            hommependu()
            print("")
            affichagemot()
    else:
        hommependu()
        print("")
        affichagemot()
    if nb_vie==-1:
        print("Vous avez perdu, désolé")
        break
    if "_" in tiret:
        print("")
    else:
        print("Bravo, vous avez gagné")
        break
    
    
    
#        ________
#       |        |
#       |        O
#       |       /|\
#       |       /\
#    ___|____
