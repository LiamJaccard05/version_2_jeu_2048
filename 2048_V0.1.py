"""
Auteur      : Liam Jaccard
Date        : 03.02.2023
Version     : 0.1
Description : Projet 2048
"""
from tkinter import *

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
Label_Top_score = Label(top_score, text="Top Score:",fg="white", bg="#9b9b9b", font=("Arial",10))
Label_score = Label(score, text="Score:", bg="#9b9b9b",fg="white", font=("Arial",10))

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
        Labels[line][col] = Label (carre_de_fond, text ="", width=6, height=3, borderwidth=1, relief="solid", font=("Arial", 15), fg="white")
        # placement du label dans la fenêtre par ses coordonnées en pixels
        Labels[line][col].place(x=13 + 80 * col, y=10 + 80 * line)

#
def display():
    for line in range(len(Chiffres)):
        for col in range(len(Chiffres[line])):
            # construction de chaque label sans le placer
            Labels[line][col].config (text =Chiffres[line][col], bg=carre_couleurs[Chiffres[line][col]])

            if Chiffres [line][col] == 0:
                Labels[line][col].config(text="", bg="#CCCCCC")

            else:
                Labels[line][col].config (text =Chiffres[line][col], bg=carre_couleurs[Chiffres[line][col]])

def nouvelle_partie():
    global Chiffres
    Chiffres = [[0,0,0,0], [0,0,0,0],[0,0,0,0],[0,0,0,0]]
    display()


#button
button_nouvelle_partie = Button(fenetre,command=nouvelle_partie, text="Nouvelle Partie", bg="#9b9b9b", font=("Arial",10), fg="white")
button_nouvelle_partie.place(x=195, y=500)
#lancement de la fenetre en boucle et tableau
display()
fenetre.mainloop()
