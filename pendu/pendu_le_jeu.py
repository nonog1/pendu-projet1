from tkinter import *
import random
#Liste des mots possibles dans le jeu du pendu :
liste=["eau","bonjour","astronaute","hauteur","fraction","poumon","vote","nature","bagage","rapide","langue","dragon","jouet","fin","encore","centre","pendu","populaire","semaine","armure","livre","canard"]


#Les différentes polices d'écriture utilisé dans le programme :
fonttitrep= "-size 32 -family {Arial}"
fontmenub= "-size 13 -family {Arial}"
fontsaisie= "-size 16 -family {Arial}"



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
        lettre=False



def comparaisonlettre():                       #compare si la lettre saisie se trouve dans le mot
    global nb_vie
    global nb_trouve
    global lettre_dans_mot
    global lettre_deja_saisie
    global resultatt
    if saisie in lettre_deja_saisie:
        resultatt.set("Vous avez déjà saisi cette lettre")
        lettre_dans_mot=False
    else:
        if saisie in motlist:                   #si la saisie est dans la liste qui contient chaque caractère du mot
            resultatt.set("Vous avez trouvé une lettre")
            nb_trouve=nb_trouve+1               #Le nombre de lettres trouvés augmente
            motlist.remove(saisie)              #On supprime le caractère saisie de la liste pour éviter d'avoir plusieurs fois la même lettre
            lettre_dans_mot=True    
        else:
            resultatt.set("Cette lettre n'est pas présente dans le mot")
            nb_vie=nb_vie-1                     #perdre une vie
            lettre_dans_mot=False


def affichagemot():                         #permet d'afficher le mot lorsqu'une lettre est trouvée
    global lettre_dans_mot
    global tiret
    global affichage_tiret
    global mott
    if lettre_dans_mot==True:
        while saisie in motlist2:
            position_lettre=motlist2.index(saisie)
            motlist2[position_lettre]="_"
            tiret[position_lettre]=saisie
            affichage_tiret=' '.join(tiret)
            mott.set(affichage_tiret)





def hommependu():
    global lependu
    global pendu1img
    global pendu2img
    global pendu3img
    global pendu4img
    global pendu5img
    global pendu6img
    global pendu7img
    global pendu8img
    if nb_vie==7:
        lependu.create_image(0, 0, anchor=NW, image=pendu1img)
        lependu.pack()
    if nb_vie==6:
        lependu.create_image(0, 0, anchor=NW, image=pendu2img)
        lependu.pack()
    if nb_vie==5:
        lependu.create_image(0, 0, anchor=NW, image=pendu3img)
        lependu.pack()
    if nb_vie==4:
        lependu.create_image(0, 0, anchor=NW, image=pendu4img)
        lependu.pack()
    if nb_vie==3:
        lependu.create_image(0, 0, anchor=NW, image=pendu5img)
        lependu.pack()
    if nb_vie==2:
        lependu.create_image(0, 0, anchor=NW, image=pendu6img)
        lependu.pack()
    if nb_vie==1:
        lependu.create_image(0, 0, anchor=NW, image=pendu7img)
        lependu.pack()
    if nb_vie==0:
        lependu.create_image(0, 0, anchor=NW, image=pendu8img)
        lependu.pack()

def toucheentre(event) :        #lorsque la touche entré est pressé
    saisiev()


def saisiev():          #s'execute lorsque l'utilisateur clique sur Valider
    global saisie
    global lettre
    global lettre_deja_saisie
    global resultatt
    global nb_vie
    global tiret
    global lettreds
    global lettre_deja_saisie
    global fini
    if fini==0:
        saisie=entre.get()
        verificationlettre()
        if lettre==True:
            comparaisonlettre()
            lettre_deja_saisie+=[saisie]
            affichagemot()
            hommependu()    
        else:
            resultatt.set("Merci de saisir une lettre")
        if nb_vie==0:
            resultatt.set("Vous avez PERDU !!")
            fini=1
        if not "_" in tiret:
            resultatt.set("Vous avez GAGNE !! BRAVO !")
            fini=1
        lettreds.set(lettre_deja_saisie)    
        entre.delete(0,END)                             #On supprime la lettre saisie de l'entré pour une meilleur utilisation
        


def nouvellegame():
    global lettre_dans_mot
    global lettre_deja_saisie
    global nb_trouve
    global nb_vie
    global lettres_trouve
    global lettre_fausse
    global fini
    fini=0
    lettre_dans_mot=False
    lettre_deja_saisie=[]
    nb_trouve=0
    nb_vie=8    
    lettres_trouve=[]
    lettres_fausse=[]


#Fenetre de jeu principale : (s'affiche quand le bouton "jouer" est cliqué, car ce bouton appel la fonction "jouer")
def jouer():
    global entre
    global taille
    global affichage
    global resultatt
    global mott
    global tiret
    global lependu
    global pendu1img
    global lettre_deja_saisie
    global lettreds
    choisirmot()
    nouvellegame()
    tiret=["_"]*taille
    fen=Toplevel(fenmenu)
    fen.geometry("1000x1000")
    fen.title("Pendu - Partie En Cours")
    titrejeu= Label(fen, text="- Partie en cours -", font=fonttitrep)
    titrejeu.pack()
    espace4= Canvas(fen, width=20, height=10)
    espace4.pack()
    textentre= Label(fen, text="saisir une lettre :", font=fontsaisie)
    textentre.pack()
    espace5= Canvas(fen, width=20, height=10)
    espace5.pack()
    entre= Entry(fen, font=fontsaisie, width=5)
    entre.pack()
    espace6= Canvas(fen, width=20, height=10)
    espace6.pack()
    valider= Button(fen, text="Valider", activebackground="#047f1c", width=5, height=1, bg="#1cb339", font=fontmenub, command=saisiev) 
    valider.pack()
    resultatt = StringVar()                           
    resultatsaisie= Label(fen, textvariable=resultatt, font=fontsaisie)    
    resultatt.set("- Aucune lettre saisie -")               
    resultatsaisie.pack()
    mott = StringVar()
    lemot= Label(fen, textvariable=mott, font=fontsaisie)
    mott.set(tiret)
    lemot.pack()
    lependu= Canvas(fen, width=365, height=365)
    espace7= Canvas(fen, width=20, height=10)
    espace7.pack()
    bquitterjeu= Button(fen, text="Quitter la partie", activebackground="#ac0101", width=15, height=1, bg="#f60000", font=fontmenub, command=fen.destroy)
    bquitterjeu.pack()
    espace7= Canvas(fen, width=20, height=10)
    espace7.pack()
    fen.bind("<Return>", toucheentre)           #lorsque la touche entré est pressé
    dejasaisi= Label(fen, text="Les lettres déjà saisies : ")
    dejasaisi.pack()
    lettreds= StringVar()
    afflettreds= Label(fen, textvariable=lettreds)
    afflettreds.pack()






#Fenetre du menu de lancement :
fenmenu= Tk()
fenmenu.title("Menu principal - Pendu")
fenmenu.geometry("500x500")
textbienvenue= Label(fenmenu, text="- Le Jeu Du Pendu -")
textbienvenue.configure(font=fonttitrep)
textbienvenue.pack()
espace1= Canvas(fenmenu, width=20, height=20)
espace1.pack()
boutonjouer= Button(fenmenu, text="JOUER !", activebackground="#0a7200", width=15, height=3, bg="#0fa700", font=fontmenub, command=jouer)
boutonjouer.pack()
espace2= Canvas(fenmenu, width=20, height=10)
espace2.pack()
boutonquitter= Button(fenmenu, text="QUITTER :(", activebackground="#ac0101", width=15, height=3, bg="#f60000", font=fontmenub, command=fenmenu.destroy)
boutonquitter.pack()
espace3= Canvas(fenmenu, width=20, height=10)
espace3.pack()
pendu1img = PhotoImage(file="lependu/pendu1.png")                ####
pendu2img = PhotoImage(file="lependu/pendu2.png")
pendu3img = PhotoImage(file="lependu/pendu3.png")
pendu4img = PhotoImage(file="lependu/pendu4.png")
pendu5img = PhotoImage(file="lependu/pendu5.png")
pendu6img = PhotoImage(file="lependu/pendu6.png")
pendu7img = PhotoImage(file="lependu/pendu7.png")
pendu8img = PhotoImage(file="lependu/pendu8.png")
pendumenu = PhotoImage(file="pendu_menu_img.png")                   ###
imagemenu= Canvas(fenmenu, width=200, height=200)
imagemenu.create_image(0, 0, anchor=NW, image=pendumenu)
imagemenu.pack()
fenmenu.mainloop()



