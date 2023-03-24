"""
Auteur      : Liam Jaccard
Date        : 03.02.2023
Version     : 0.2
Description : Projet 2048
"""
from tkinter import *
import random
#tableau des valeur du jeu
Chiffres = [[2, 4, 8, 16],
           [32, 64, 128, 256],
           [512, 1024, 2048, 4096],
           [8192, 0, 0, 0]]

#tableau des labels du jeu
Labels = [[None, None, None, None],
          [None, None, None, None],
          [None, None, None, None],
          [None, None, None, None]]

#code couleur des carré
carre_couleurs = { 0: "#CCCCCC",
                    2: "#ffea00",
                    4: "#ffdd00",
                    8: "#ffd000",
                    16: "#ffc300",
                    32: "#ffb700",
                    64: "#ffaa00",
                    128: "#ffa200",
                    256: "#ff9500",
                    512: "#ff8800",
                    1024: "#ff7b00",
                    2048: "#B45F06",
                    4096: "#783F04",
                    8192: "#6F523B",}

# VARIABLES
width = 500
height = 600
Score = 0
Top = 0
# CREER UNE FENETRE
fenetre = Tk()


# CARACTERISTIQUES DE LA FENÊTRE
screenwidth = fenetre.winfo_screenwidth()
screenheight = fenetre.winfo_screenheight()
x = (screenwidth / 2) - (width / 2)
y = (screenheight / 2) - (height / 2)
fenetre.geometry("%dx%d+%d+%d" % (width, height, x, y))
fenetre.resizable(False, False)
fenetre.config(bg="#B6D7A8")
fenetre.title("Projet 2048")
#frame
carre_de_fond = Frame(fenetre, height="340", width="340", background="#9b9b9b",borderwidth=1, relief="solid")
top_score = Frame(fenetre, height="60" , width="80" , background="#9b9b9b",borderwidth=1, relief="solid")
score = Frame(fenetre, height="60" , width="80" , background="#9b9b9b",borderwidth=1, relief="solid")

#carré du score
label_2048 = Label(fenetre, text="2048", bg="#B6D7A8", font=("Arial",50))
Label_score = Label(score, text="Score:", bg="#9b9b9b",fg="white", font=("Arial",10))
Label_Top_score = Label(top_score, text="Top Score:",fg="white", bg="#9b9b9b", font=("Arial",10))

#packs
label_2048.place(x=170, y=20)
carre_de_fond.place(x=75, y=110)
top_score.place(x=30, y=40)
Label_Top_score.place(x=5, y=2)
score.place(x=375, y=38)
Label_score.place(x=17, y=2)



#création des labels du heu 2048 avec les differents tableau et les couleurs
for line in range(len(Chiffres)):
    for col in range(len(Chiffres[line])):
        # construction de chaque label sans le placer
        Labels[line][col] = Label (carre_de_fond, text ="", width=6, height=3, borderwidth=1, relief="solid", font=("Arial", 15), fg="black")
        # placement du label dans la fenêtre par ses coordonnées en pixels
        Labels[line][col].place(x=13 + 80 * col, y=10 + 80 * line)

#afficher le jeu
def display():
    for line in range(len(Chiffres)):
        for col in range(len(Chiffres[line])):
            # construction de chaque label sans le placer
            Labels[line][col].config (text =Chiffres[line][col], bg=carre_couleurs[Chiffres[line][col]])

            if Chiffres [line][col] == 0:
                Labels[line][col].config(text="", bg="#CCCCCC")

            else:
                Labels[line][col].config (text =Chiffres[line][col], bg=carre_couleurs[Chiffres[line][col]])
#fonction pour créer une nouvelle partie aidé par amine
def nouveau():
    global Chiffres
    global Score
    Score = 0
    Label_score.configure(text=f"{Score}")

    possibles  = [0,1,2,3]
    Chiffres =[[0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]]


    spawn_hole(2)
    display()



# reçoit 4 nombres, tasse vers le a,  et en renvoie 5
def tasse_4(a,b,c,d):
    global Score
    global Top
    nmove=0 #sert à savoir si on a réussi à bouger
    # ici le code va manipuler a,b,c et d

#pour bouger les blocs
    if c == 0 and d>0:
         c,d = d,0
         nmove+=1

    if b == 0 and c>0 :
        b,c,d = c,d,0
        nmove+=1
    if a == 0 and b>0 :
        a,b,c,d = b,c,d,0
        nmove+=1
#tasser les blocs
    if a == b and a>0:
        a,b,c,d = a+b,c,d,0
        Score = Score + a
        nmove+=1
    if b == c and b>0:
        b,c,d = b+c,d,0
        Score = Score + b
        nmove+=1
    if c == d and c>0:
        c,d = c+d,0
        Score = Score + c
        nmove += 1

    #mise à jour des scores
    Label_score.configure(text=f"{Score}")
    if Score > Top:
        Top = Score
        Label_Top_score.configure(text=f"{Top}")

    # ici on retourne les cinq valeurs en un tableau
    temp=[a,b,c,d,nmove] #tableau temporaire de fin
    return temp


#bouge a gauche aidé par kushtrim
def move_left(event):
    totn = 0
    for ligne in range(4):
        [Chiffres[ligne][0],Chiffres[ligne][1],Chiffres[ligne][2],Chiffres[ligne][3], n]=tasse_4(Chiffres[ligne][0],Chiffres[ligne][1],Chiffres[ligne][2],Chiffres[ligne][3])
    totn+=n
    if totn > 0:
        spawn_hole(1)
        print(n)
    display()
#bouge a droite
def move_right(event):
    totn = 0
    for ligne in range(4):
        [Chiffres[ligne][3],Chiffres[ligne][2],Chiffres[ligne][1],Chiffres[ligne][0], n]=tasse_4(Chiffres[ligne][3],Chiffres[ligne][2],Chiffres[ligne][1],Chiffres[ligne][0])
        totn+=n
    if totn > 0:
        spawn_hole(1)
        print(n)
    display()
#bouge en haut
def move_top(event):
    totn = 0
    for ligne in range(4):
        [Chiffres[0][ligne],Chiffres[1][ligne],Chiffres[2][ligne],Chiffres[3][ligne], n]=tasse_4(Chiffres[0][ligne],Chiffres[1][ligne],Chiffres[2][ligne],Chiffres[3][ligne])
        totn += n
    if totn > 0:
        spawn_hole(1)
        print(n)
    display()
#bouge en bas
def move_down(event):
    totn = 0
    for ligne in range(4):
        [Chiffres[3][ligne],Chiffres[2][ligne],Chiffres[1][ligne],Chiffres[0][ligne], n]=tasse_4(Chiffres[3][ligne],Chiffres[2][ligne],Chiffres[1][ligne],Chiffres[0][ligne])
        totn += n
    if totn > 0:
        spawn_hole(1)
        print(n)
    display()



#bind touche
fenetre.bind("<Left>",move_left)
fenetre.bind("a",move_left)
fenetre.bind("A",move_left)
fenetre.bind("<Right>",move_right)
fenetre.bind("d",move_right)
fenetre.bind("D",move_right)
fenetre.bind("<Up>",move_top)
fenetre.bind("w",move_top)
fenetre.bind("W",move_top)
fenetre.bind("<Down>",move_down)
fenetre.bind("s",move_down)
fenetre.bind("S",move_down)


def spawn_hole(number_of_tile):
#fonction pour que la tuile apparait a chaque mouvement
# si on tombe sur une tuile déjà prise, on relance la fonction
    global  Chiffres   # case vide
    for i in range(number_of_tile):
        vide = []
        for line in range(len(Chiffres)):
            for col in range(len(Chiffres[line])):
                if Chiffres [line][col] == 0:
                    vide.append([line,col])
        if len(vide) > 0:
            n = random.randint(0,len(vide)-1)
            #tire un 2° nb aléatoire entre 0 et 10
            a = random.randint(0,10)
            #si le nb est <7, on met un 2
            if a<7:
                Chiffres[vide[n][0]][vide[n][1]] = 2
            #sinon on met un 4
            else:
                Chiffres[vide[n][0]][vide[n][1]] = 4
        display()




display()
#button
button_nouvelle_partie = Button(fenetre,command=nouveau, text="Nouvelle Partie", bg="#9b9b9b", font=("Arial",10), fg="white")
button_nouvelle_partie.place(x=195, y=500)
#lancement de la fenetre en boucle et tableau
display()
fenetre.mainloop()
