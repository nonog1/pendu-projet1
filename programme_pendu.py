
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


#def veriflettre():
    #saisie=input("saisir une lettre: ")
    #saisie=(saisie.lower())
    #print(saisie)
    
saisi=input("saisir une lettre:")
caractereMaj=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
verif=saisi in caractereMaj
if verif==True:
    print(saisi.lower())
else:
    print(saisi)
    
    
    
    
    
choisirmot()
#veriflettre()
