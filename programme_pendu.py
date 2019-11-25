
import random
liste=["eau","bonjour","astronaute"]

def choisirmot():                           #fonction qui permet de choisir un mot et d'afficher les underscores
    global mot
    global taille
    global motlist
    global motlist2
    mot=""
    mot=random.choice(liste)                #choisie un mot aléatoirement dans la liste
    print(mot)
    taille=len(mot)                         #compte le nombre de lettre dans le mot
    print(taille)
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
    if saisie in motlist:                   #si la saisie est dans la liste qui contient chaque caractère du mot
        print("Vous avez trouvé une lettre !")
        nb_trouve=nb_trouve+1               #Le nombre de lettres trouvés augmente
        motlist.remove(saisie)              #On supprime le caractère saisie de la liste pour éviter d'avoir plusieurs fois la même lettre
        print(motlist)
        lettre_dans_mot=True
        
    else:
        print("cette lettre n'est pas présente dans le mot")
        nb_vie=nb_vie-1                     #perdre une vie
        lettre_dans_mot=False


def affichagemot():
    global lettre_dans_mot
    if lettre_dans_mot==True:
        position_lettre=motlist2.index(saisie)
        print(position_lettre)

    

choisirmot()
nb_trouve=0
nb_vie=7    
lettres_trouve=[]
lettres_fausse=[]
while nb_trouve<taille:    
    saisie=input("saisir une lettre:")
    verificationlettre()
    if lettre==True:
        comparaisonlettre()
        affichagemot()

    
    
    
    
#        ________
#       |        |
#       |        O
#       |       /|\
#       |       /\
#    ___|____
