
import random
liste=["eau","bonjour","astronaute"]
def choisirmot():                    #fonction qui permet de choisir un mot et d'afficher les underscores
    mot=""
    mot=random.choice(liste)         #choisie un mot aléatoirement dans la liste
    print(mot)
    taille=len(mot)                  #compte le nombre de lettre dans le mot
    print(taille)
    i=0
    while i<taille:                  #boucle qui affiche les underscores
        print("_ ", end="")          #le (, end="") permet de les écrires à la suite, ne pas revenir à la ligne
        i=i+1


caractereMaj=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
caractereMin=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]  
def verificationlettre():
    verif=saisi in caractereMaj
    if verif==True:
       saisi=(saisi.lower())
       print(saisi)
    else:
        print(saisi)
    verif2= saisi in caractereMin
    if verif2==True:
        print(saisi)
    else:
        print("vous n'avez pas saisi une lettre, merci de recommencer")
    
    

    
choisirmot()
saisi=input("saisir une lettre:")
verificationlettre()
