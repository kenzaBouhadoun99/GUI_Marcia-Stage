import pandas as pd
from tkinter import *
from matplotlib.rcsetup import validate_color_for_prop_cycle, validate_color_or_auto
from PIL import ImageTk, Image
import tkinter as tk
from pyparsing import col



fenetre = Tk() 
fenetre.title("MARCIA")
fenetre.geometry("1200x700")

''' Le menu '''
mon_menu = Menu(fenetre)
#creation des onglets
mon_menu.add_cascade(label="File")
mon_menu.add_cascade(label="About")
fenetre.config(menu=mon_menu)


# Créer les 8 cadres qui représentent les colonnes
#volet 1 en haut
cadre1 = Frame(fenetre, borderwidth=2, relief="solid", width=400, height=400)
#volet 2 en haut
cadre2 = Frame(fenetre, borderwidth=2, relief="solid", width=400, height=400)
#volet 3 en haut
cadre3 = Frame(fenetre, borderwidth=2, relief="solid", width=400, height=400) 
#volet 1 au milieu
cadre4 = Frame(fenetre, borderwidth=2, relief="solid", width=100, height=50)
#volet 1 en bas
cadre5 = Frame(fenetre, borderwidth=2, relief="solid", width=400, height=349)
#volet 2 au milieu
cadre6 = Frame(fenetre, borderwidth=2, relief="solid", width=100, height=50)
#volet 2 en bas
cadre7 = Frame(fenetre, borderwidth=2, relief="solid", width=400, height=349)
#volet 3 en bas
cadre8 = Frame(fenetre, borderwidth=2, relief="solid", width=400, height=400)


# Répartir les colonnes en utilisant la méthode grid
cadre1.grid(row=0, column=0, sticky="nsew")
cadre2.grid(row=0, column=1, sticky="nsew")
cadre3.grid(row=0, column=2, sticky="nsew")
cadre4.grid(row=1, column=0, sticky="nsew")
cadre5.grid(row=2, column=0, sticky="nsew")
cadre6.grid(row=1, column=1, sticky="nsew")
cadre7.grid(row=2, column=1, sticky="nsew")
cadre8.grid(row=1, rowspan=2, column=2, sticky="nsew")




# Charger l'image
image = Image.open("images/save.png")

# Redimensionner l'image si nécessaire
image = image.resize((200, 200))  # Spécifiez la taille souhaitée

# Convertir l'image en format compatible avec Tkinter
image_tk = ImageTk.PhotoImage(image)



# Charger l'icône "settings.png" 
icon_settings = Image.open("images/settings.png")
icon_settings = ImageTk.PhotoImage(icon_settings)  


# charger l'icône "save.png" en tant qu'objet PhotoImage
icon_save = PhotoImage(file="images/save.png")
icon_save = icon_save.zoom(1)


# charger l'icône "folder.png" en tant qu'objet PhotoImage et la réduire de moitié
icon_open = PhotoImage(file="images/file.png")
icon_open = icon_open.zoom(1)


# charger l'icône "folder.png" en tant qu'objet PhotoImage et la réduire de moitié
icon_open2 = PhotoImage(file="images/file.png")
icon_open2 = icon_open2.zoom(1)


# charger l'icône "plus.png" en tant qu'objet PhotoImage et la réduire de moitié
icon_plus = PhotoImage(file="images/plus.png")
icon_plus = icon_plus.zoom(1)


# charger l'icône "moin.png" en tant qu'objet PhotoImage et la réduire de moitié
icon_moins = PhotoImage(file="images/moins.png")
icon_moins= icon_moins.zoom(1)


# charger l'icône "settings.png" en tant qu'objet PhotoImage et la réduire de moitié
icon_settings2 = Image.open("images/settings.png")
icon_settings2 = ImageTk.PhotoImage(icon_settings2)


# charger l'icône "settings.png" en tant qu'objet PhotoImage et la réduire de moitié 
icon_update = Image.open("images/MiseAJ.png")
icon_update = ImageTk.PhotoImage(icon_update)


# Redimensionner les colonnes pour qu'elles s'adaptent à la taille de la fenêtre
fenetre.grid_columnconfigure(0, weight=1)
fenetre.grid_columnconfigure(1, weight=1)
fenetre.grid_columnconfigure(2, weight=1)

#Partie  scrolle pour le cadre 6 
mycanvas = Canvas(cadre6)
mycanvas.pack(side=TOP, fill="both", expand=True)
xscrollbar = Scrollbar(cadre6, orient="horizontal", command=mycanvas.xview)
xscrollbar.pack(side=BOTTOM, fill='x')
mycanvas.configure(xscrollcommand=xscrollbar.set)
def adjust_scrollregion(event):
    mycanvas.configure(scrollregion=mycanvas.bbox("all"))

mycanvas.bind('<Configure>', adjust_scrollregion)
myframe = Frame(mycanvas)
mycanvas.create_window((0, 0), window=myframe, anchor="nw")
# Configurer la zone de défilement initiale
mycanvas.configure(scrollregion=mycanvas.bbox("all"))


mycanvas2 = Canvas(cadre7)
mycanvas2.pack(side="top", fill="both", expand=True)
xscrollbar2 = Scrollbar(cadre7, orient="horizontal", command=mycanvas2.xview)
xscrollbar2.pack(side="bottom", fill="x")
myframe2 = Frame(mycanvas2)
mycanvas2.create_window((0, 0), window=myframe2, anchor="nw")
# Configurer la barre de défilement pour le canevas interne
mycanvas2.configure(xscrollcommand=xscrollbar2.set)
# Fonction pour configurer la taille du canevas interne en fonction du contenu
def configurer_canevas_interne(event):
    mycanvas2.configure(scrollregion=mycanvas2.bbox("all"))
# Associer la fonction de configuration du canevas interne avec le redimensionnement du cadre ou du tableau
myframe2.bind("<Configure>", configurer_canevas_interne)



# Largeur maximale de l'affichage horizontal
max_width = 300
filenames = [] # une liste vide pour stocker les noms de fichiers
filebuttons = []

current_image_label = None

