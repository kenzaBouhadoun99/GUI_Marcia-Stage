import io
import os
import subprocess
import matplotlib.pyplot as plt
import pandas as pd
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from matplotlib.rcsetup import validate_color_for_prop_cycle, validate_color_or_auto
from sympy import im
from Interface import * 
from PIL import ImageTk, Image
from pyparsing import col
from pandastable import Table
from mask import Mask
from os.path import basename
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk






                                            ###########'''IMAGES'''###########
def calculateur(option):
    pop.destroy()
    if option == 'calc':
        pass
    elif option == "ajout":
        print("ajout")
    else:
        global pop2
        pop2 = Toplevel(fenetre)
        pop2.title("Tools")
        pop2.geometry("350x200")
        # Ici, vous devez ouvrir les diagrammes biplots et ternaires
    pass



def open_settings():
    global pop
    pop = Toplevel(fenetre)
    pop.title("Tools")
    pop.geometry("350x200")
    pop.config(bg="#909497")
    pop_label =Label(pop,text="VEUILLEZ CHOISIR VOTRE OPTION:")
    pop_label.pack(pady=10)
    my_frame=Frame(pop ,bg="#909497")
    my_frame.pack(pady=5)
    #les boutons de popup
    calc = Button(my_frame, text="Ouvrir un calculateur d'images", command=lambda: calculateur("calc"))
    calc.grid(row=0 ,column=0)
    ajout= Button(my_frame,text="Ouvrir un diagramme biplot et ternaire",command=lambda: calculateur("ajout"))
    ajout.grid(row=1 ,column=0)
    ouvrir_popup= Button(my_frame,text="Ajouter un élément ou une l’image d’une région spectrale",command=lambda: calculateur("ouvrir_popup"))
    ouvrir_popup.grid(row=2 ,column=0)

# Avant d'utiliser la fonction save_image, initialisez l'attribut 'images' pour le cadre 5
cadre5.images = []



def save_image():
    # Demander à l'utilisateur de spécifier le nom du fichier avec l'extension
    filename = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG", "*.png"), ("JPEG", "*.jpeg"), ("TIF", "*.tif")])
    
    if filename:
        # Extraire le nom de fichier et le dossier de destination
        destination_dir, image_name = os.path.split(filename)
        
        # Vérifier si le dossier de destination existe
        if not os.path.isdir(destination_dir):
            os.makedirs(destination_dir)  # Créer le dossier de destination s'il n'existe pas
        
        # Parcourir les images dans le cadre5
        for image_label in cadre5.winfo_children():
            # Vérifier si l'élément est un canvas
            if isinstance(image_label, tk.Canvas) and image_label.winfo_class() == "Canvas":
                # Récupérer l'image du canvas
                image = image_label.postscript(colormode="color")
                if image:
                    # Convertir l'image en format PIL Image
                    pil_image = Image.open(io.BytesIO(image.encode("utf-8")))
                    
                    # Enregistrer l'image dans le dossier de destination
                    image_path = os.path.join(destination_dir, image_name)
                    pil_image.save(image_path)
        # Afficher un message de confirmation
        messagebox.showinfo("Information", "L'image est enregistrée avec succès")
    else:
        # Afficher un message d'erreur si aucun nom de fichier n'a été spécifié
        messagebox.showerror("Erreur", "Aucun nom de fichier spécifié ")

def save_classification():
    # Demander à l'utilisateur de spécifier le nom du fichier avec l'extension
    filename = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG", "*.png"), ("JPEG", "*.jpeg"), ("TIF", "*.tif")])
    if filename:
        # Extraire le nom de fichier et le dossier de destination
        destination_dir, image_name = os.path.split(filename)
        # Vérifier si le dossier de destination existe
        if not os.path.isdir(destination_dir):
            os.makedirs(destination_dir)  # Créer le dossier de destination s'il n'existe pas
        # Parcourir les images dans le cadre5
        for image_label in cadre8.winfo_children():
            # Vérifier si l'élément est un canvas
            if isinstance(image_label, tk.Canvas) and image_label.winfo_class() == "Canvas":
                # Récupérer l'image du canvas
                image = image_label.postscript(colormode="color")
                if image:
                    # Convertir l'image en format PIL Image
                    pil_image = Image.open(io.BytesIO(image.encode("utf-8")))  
                    # Enregistrer l'image dans le dossier de destination
                    image_path = os.path.join(destination_dir, image_name)
                    pil_image.save(image_path)
                   

        # Afficher un message de confirmation
        messagebox.showinfo("Information", "L'image est enregistrée avec succès")
    else:
        # Afficher un message d'erreur si aucun nom de fichier n'a été spécifié
        messagebox.showerror("Erreur", "Aucun nom de fichier spécifié ")



import os
import pandas as pd

def create_default_excel_file(dossier):
    # Vérifier si le dossier existe
    if not os.path.exists(dossier):
        messagebox.showerror("Erreur", "Le dossier spécifié n'existe pas.")
        return None

    # Chemin complet du fichier "default.xlsx"
    fichier_excel = os.path.join(dossier, "default.xlsx")

    if os.path.exists(fichier_excel):
        try:
            # Charger le DataFrame à partir du fichier Excel existant
            df = pd.read_excel(fichier_excel)
        except Exception as e:
            messagebox.showerror("Erreur", f"Une erreur s'est produite lors de la lecture du fichier : {str(e)}")
            return None
    else:
        # Créer le DataFrame initial avec une seule colonne "Element"
        df = pd.DataFrame(columns=["Element"])

    # Ajouter une nouvelle ligne avec la valeur "couleur" dans la première colonne
    df.loc[df.shape[0], "Element"] = "couleur"

    # Mettre à jour le DataFrame avec les nouvelles données
    filenames_list = df["Element"].tolist()
    for filename in filenames:
        if filename not in filenames_list:
            df = pd.concat([df, pd.DataFrame({"Element": [filename]})], ignore_index=True)  # Ajouter une nouvelle ligne avec le nom de fichier
    try:
        # Écrire le DataFrame dans le fichier Excel
        df.to_excel(fichier_excel, index=False)
        #messagebox.showinfo("Succès", "Le fichier default.xlsx a été mis à jour avec succès.")
        return fichier_excel
    except Exception as e:
        messagebox.showerror("Erreur", f"Une erreur s'est produite lors de la mise à jour du fichier : {str(e)}")
        return None












dossier = ""
extension ='.tif'

# Fonction pour choisir un dossier
def choisir_dossier():
    global dossier
    messagebox.showinfo("Message", "Bonjour ! Veuillez d'abord choisir le dossier de travail.")
    chemin_complet = filedialog.askdirectory()
    dossier = os.path.basename(chemin_complet) + "/"
    create_default_excel_file(dossier) 
    print("le nom du fichier xlsx",create_default_excel_file(dossier))
     


# Appel de la fonction pour choisir un dossier
choisir_dossier()

# Affichage du nom du dossier choisi
print("Dossier choisi :", dossier)


def createObject(dir, ext, fileExcel):
    cm = Mask(dir, ext, fileExcel)
    
    return cm

fichierExcel  = create_default_excel_file(dossier)

# Créer l'instance de Mask en utilisant la fonction createObject()
cm = createObject(dossier, extension, fichierExcel)



# Créer le DataFrame initial avec les colonnes "Element"
df = pd.DataFrame(columns=["Element"])
start_index = 0  # Déclaration de la variable start_index en tant que variable globale
import pandas as pd

df = pd.DataFrame(columns=["Element"])
start_index = 0  # Déclaration de la variable start_index en tant que variable globale

def open_file():
    global filenames, df, cadre7

    # Initialiser l'ensemble des noms de fichiers uniques
    unique_filenames = set(filenames)

    # Initialiser la liste de chemins de fichiers
    filepaths = []

    # Demander à l'utilisateur de sélectionner un fichier avec une extension .png, .jpg, .jpeg, bmp ou .tif
    filepaths = filedialog.askopenfilenames(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.tif;*.bmp;*.txt;*.raw")])

    # Si l'utilisateur a sélectionné un fichier
    if filepaths:
        try:
            for filepath in filepaths:
                # Récupérer l'extension du fichier sélectionné
                ext = os.path.splitext(filepath)[1]

                # Vérifier que tous les fichiers dans la liste ont la même extension que le premier fichier
                if any(unique_filenames) and not all(file.endswith(ext) for file in unique_filenames):
                    messagebox.showerror("Error", f"Le fichier n'a pas la bonne extension")
                    return

                # Vérifier que le premier fichier sélectionné est sous extension .tif, .jpg ou .jpeg, .png, .txt
                if len(unique_filenames) == 0:
                    if ext not in [".tif", ".jpg", ".jpeg", ".png", ".bmp", ".txt", ".raw"]:
                        messagebox.showerror("Error", "Le premier fichier doit être sous extension .png, .tif, .jpg, bmp,txt,raw ou .jpeg")
                        return

                # Vérifier si le fichier est déjà ouvert dans l'interface
                if os.path.basename(filepath) in unique_filenames:
                    messagebox.showinfo("Information", "Le fichier est déjà ouvert dans l'interface")
                    return

                # Ajouter le nom de fichier à l'ensemble des noms de fichiers uniques
                filename = os.path.basename(filepath)   
                unique_filenames.add(filename)

            # Mettre à jour les noms de fichiers dans le DataFrame
            filenames = list(unique_filenames)  # Convertir l'ensemble en liste pour maintenir l'ordre
            df = pd.DataFrame({"Element": filenames})

            # Modifier la colonne "Element" pour afficher les noms sans l'extension
            df["Element"] = df["Element"].apply(lambda x: os.path.splitext(x)[0])

            # Ajouter une ligne avec la valeur "couleur" juste en dessous de la colonne "Element"
            new_row = pd.DataFrame({"Element": ["couleur"]})
            df = pd.concat([df, new_row], ignore_index=True)

            # Mettre à jour la liste des fichiers affichée dans le Listbox avec la fonction update_filelist()
            update_filelist()
            # Mettre à jour le tableau avec les nouvelles données
            cadre7.update()

            # Sauvegarder le DataFrame mis à jour dans le fichier Excel
            fichier_excel = os.path.join(dossier, "default.xlsx")
            df.to_excel(fichier_excel, index=False)

            messagebox.showinfo("Succès", "Le fichier default.xlsx a été mis à jour avec succès")
        except FileNotFoundError:
            messagebox.showerror("Error", "L'image sélectionnée n'existe pas")




              


    
    

# Définir la variable comme un dictionnaire vide
popup_hist_dict = {}

def update_image(event):
    global current_image_label, filenames, popup_hist_dict  
    # Obtenir l'indice du bouton sélectionné
    index = event.widget.index(ANCHOR)
    # Obtenir le bouton sélectionné
    selected_button = filebuttons[index]
    # Obtenir le nom du fichier bdu bouton sélectionné
    filename = selected_button["text"]
    # Extraire le nom de fichier sans l'extension
    file_name_without_extension = os.path.splitext(filename)[0]
    # Créer une nouvelle popup d'histogramme et afficher la carte élémentaire dans le cadre5
    cm.get_hist(file_name_without_extension, cadre5)
    # Mettre à jour le dictionnaire pour indiquer que la popup est créée pour ce fichier
    popup_hist_dict[file_name_without_extension] = True
    


def update_filelist():
    global filebuttons, start_index
    # Supprimez les boutons de sélection existants s'il y en a
    for button in filebuttons:
        button.pack_forget()
    filebuttons.clear()
    # Le nombre de colonnes pour afficher les noms des images
    num_columns = 2
    # La position actuelle dans la grille
    row = 0
    column = 0
    # Créer les boutons de sélection pour chaque fichier à partir de l'index de départ
    for i in range(start_index, len(filenames)):
        filename = filenames[i]
        if os.path.exists(os.path.join('images', filename)):
            button = Radiobutton(cadre4, text=filename, font=("Arial", 12), variable=selected_file, value=filename, command=lambda fname=filename: on_file_selection(fname))
            button.grid(row=row, column=column, sticky="w", padx=10, pady=5)
            button.deselect()  # Désélectionner le bouton radio
            filebuttons.append(button)
            # Passer à la colonne suivante
            column += 1
            # Si on a atteint la fin d'une colonne, passer à la ligne suivante
            if column >= num_columns:
                row += 1
                column = 0
                # Si on a atteint le nombre maximum de boutons, arrêter la création
                if row >= 100:
                    break
            
            # Passer à la colonne suivante
            if column >= num_columns:
                row += 1
                column=0



def on_file_selection(*args):
    filename = selected_file.get()
    print("Fichier sélectionné :", filename)
    # Mettez à jour l'image dans le cadre5 en utilisant le nom de fichier sélectionné
    file_name_without_extension = os.path.splitext(filename)[0]
    cm.load_table()  # Charger les éléments à partir du fichier Excel
    cm.datacube_creation()
    cm.get_hist(file_name_without_extension, cadre5)


# Initialiser la liste des fichiers
filenames = []
# Créer une variable pour le fichier sélectionné
selected_file = StringVar()
# Créer une liste pour stocker les boutons de sélection
filebuttons = []
# Créer les boutons et les afficher
update_filelist()

# Lier la variable selected_file à la fonction on_file_selection
selected_file.trace("w", on_file_selection)



                                        ###########'''MASQUES'''###########


'''Ouvrir'''
excel_table = None
filename=""
excel_filename_label = tk.Label(cadre7, text="")
excel_filename_label.pack()
excel_table = None
excel_file_path = ""

def open_fileMask():
    global excel_file, excel_file_path

    # Vider le contenu de cadre7 s'il y a des widgets
    for widget in cadre7.winfo_children():
        widget.destroy()

    # Ouvrir la boîte de dialogue pour sélectionner un fichier Excel
    filename = filedialog.askopenfilename(filetypes=[("Fichiers Excel", "*.xlsx")])
    excel_file_path = filename
    print("Le nom du fichier est", basename(filename))
    if filename:
        # Si un fichier est sélectionné, afficher son contenu dans le cadre7
        excel_file = pd.read_excel(filename)

        # Créer un cadre pour contenir le tableau
        frame = tk.Frame(cadre7)
        frame.grid(row=0, column=0, sticky='nsew')

        # Créer un Canvas pour afficher le tableau avec une barre de défilement verticale et horizontale
        canvas = tk.Canvas(frame)
        canvas.grid(row=0, column=0, sticky='nsew')

        # Créer une frame intérieure pour contenir le tableau
        inner_frame = tk.Frame(canvas)
        inner_frame.grid(row=0, column=0, sticky='nsew')
        inner_frame.grid_propagate(False)
        inner_frame.configure(width=cadre7.winfo_reqwidth(), height=cadre7.winfo_reqheight())

        # Ajouter le tableau à la frame intérieure
        pt = Table(inner_frame, dataframe=excel_file)
        pt.show()

        # Configurer le défilement du Canvas
        canvas.configure(scrollregion=canvas.bbox('all'))

        # Configurer les options de redimensionnement pour le cadre7
        cadre7.grid_rowconfigure(0, weight=1)
        cadre7.grid_columnconfigure(0, weight=1)
        # Créer un bouton "Enregistrer"
        save_button = tk.Button(cadre7, text="  Save  ", command=update_table)
        save_button.grid(row=1, column=0, sticky='s', columnspan=2)


def update_table():
    global excel_file, excel_file_path

    if excel_file is not None and excel_file_path is not None:
        # Enregistrer les modifications dans le fichier Excel d'origine
        excel_file.to_excel(excel_file_path, index=False)
        print("Modifications enregistrées dans le fichier :", excel_file_path)
    elif excel_file is not None:
        # Demander à l'utilisateur de spécifier un nom de fichier pour enregistrer le tableau
        filename = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Fichiers Excel", "*.xlsx")])
        if filename:
            excel_file_path = filename
            # Enregistrer le tableau dans le fichier spécifié
            excel_file.to_excel(excel_file_path, index=False)
            print("Tableau enregistré dans le fichier :", excel_file_path)
        else:
            print("Aucun fichier sélectionné")
    else:
        print("Aucun tableau ouvert")




'''Plus'''
# initialisation des masques à 1
option_count = 0
col_count  = 0
checkbutton_list = []
var_list = []
option_count=0

#df = pd.DataFrame(" nom ", index=range(10), columns=['Element'])            
col_count = 0  # On commence à compter à partir de la deuxième colonne

#Fonction qui supprime les checkbutton qui sont dans le cadre6
def add_checkbutton():
    global option_count, var_list, checkbutton_list,  frame7, col_count

    option_count += 1
    var = IntVar()  # création d'une variable de contrôle pour chaque Checkbutton
    var_list.append(var)
    checkbutton = Checkbutton(myframe, text=f"Masque {option_count}", variable=var)
    checkbutton.grid(row=(option_count-1)//6, column=(option_count-1)%6, padx=2, pady=2)
    checkbutton_list.append(checkbutton)  # ajout du Checkbutton et de sa variable de contrôle à la liste
    add_column()
    checkbutton_list.append(checkbutton)
    
    # Configuration de la propriété grid_propagate à False
    cadre7.grid_propagate(False)

    # Configuration des colonnes du cadre7
    for i in range(10):
        cadre7.grid_columnconfigure(i, weight=11)
    mycanvas.configure(scrollregion=mycanvas.bbox("all"))


def remove_checkbutton():
    global var_list, checkbutton_list, cadre7, df
    selected = False
    for child in myframe.winfo_children():
        if isinstance(child, Checkbutton) and var_list[checkbutton_list.index(child)].get() == 1:
            selected = True
            child.destroy()
            # Supprimer la colonne correspondante dans la DataFrame
            col_index = checkbutton_list.index(child) + 1
            column_name = df.columns[col_index]
            df = df.drop(column_name, axis=1)
            df.columns = df.columns[:col_index].tolist() + df.columns[col_index+1:].tolist()
            checkbutton_list.pop(checkbutton_list.index(child))
    if not selected:
        messagebox.showerror("ATTENTION: ERREUR", "Aucun masque sélectionné")
    # Mettre à jour l'affichage du tableau
    update_table_display()




def update_table_display(): 
    global cadre7, df
    # Effacer le contenu du cadre7
    for widget in cadre7.winfo_children():
        widget.destroy()  
    # Sélectionner les lignes à partir de l'indice 1
    df_display = df.iloc[1:, :]
    # Afficher le tableau dans le cadre7 avec les dimensions du cadre7
    frame = tk.Frame(cadre7)
    frame.grid(row=0, column=0, sticky='nsew')
    pt = Table(frame, dataframe=df_display)
    pt.show()
    # Ajouter un widget de remplissage pour pousser le tableau vers le haut
    fill_label = tk.Label(cadre7)
    fill_label.grid(row=1, column=0, sticky='ns')
    # Configurer les options de redimensionnement pour le cadre7

    cadre7.grid_rowconfigure(0, weight=1)
    cadre7.grid_columnconfigure(0, weight=1)




def add_column():
    global df
    col_counter = len(df.columns) + 1
    column_name = f"Masque {col_counter - 1}" 
    
    # Vérifier si la colonne existe déjà
    if column_name in df.columns:
        messagebox.showerror("Erreur", f"La colonne {column_name} existe déjà.")
        return
    new_column = [''] * len(df)
    df.insert(col_counter - 1, column_name, new_column)
    # Ajouter le nom de la colonne dans la première ligne de la DataFrame
    df.iloc[0, col_counter - 1] = column_name
    df.iloc[0, 0] = "Element"
    
    # Effacer le contenu du cadre7
    for widget in cadre7.winfo_children():
        widget.destroy()
    
        # Sélectionner les lignes à partir de l'indice 1
    df_display = df.iloc[1:, :]
    
    # Afficher le tableau dans le cadre7 avec les dimensions du cadre7
    frame = tk.Frame(cadre7)
    frame.grid(row=0, column=0, sticky='nsew')
    
    # Créer le widget Table
    pt = Table(frame, dataframe=df_display, showtoolbar=False, showstatusbar=False)
    pt.show()
    
    # Ajouter un widget de remplissage pour pousser le tableau vers le haut
    fill_label = tk.Label(cadre7)
    fill_label.grid(row=1, column=0, sticky='ns')
    
    # Configurer les options de redimensionnement pour le cadre7
    cadre7.grid_rowconfigure(0, weight=1)
    cadre7.grid_columnconfigure(0, weight=1)
 




def save_file():
    global df
    filename = filedialog.asksaveasfilename(defaultextension=".xlsx")
    if filename:
        df_copy = df.copy()  # Créer une copie du Dataframe
        df_copy.iloc[0, :] = ""  # Supprimer la première occurrence de la ligne "Element"
        df_copy = df_copy[df_copy.astype(bool).any(axis=1)]  # Supprimer les lignes contenant uniquement des valeurs vides
        df = df[df.astype(bool).any(axis=1)]  # Supprimer la ligne vide du DataFrame original également
        df_copy.to_excel(filename, index=False)
        messagebox.showinfo("Sauvegarde réussie", "Les données ont été sauvegardées avec succès.")
    





                            ###########'''CLASSIFICATION'''###########

def open_settings():
    global pop 
    pop = Toplevel(fenetre)
    pop.title("Tools")
    pop.geometry("350x200")
    pop.config(bg="#909497")
    pop_label =Label(pop,text="VEUILLEZ CHOISIR VOTRE OPTION:")
    pop_label.pack(pady=10)
    my_frame=Frame(pop ,bg="#909497")
    my_frame.pack(pady=5) 
    calc= Button(my_frame,text="Ouvrir un calculateur d'images",command=lambda: calculateur("calc"))
    calc.grid(row=0 ,column=0)
    ajout= Button(my_frame,text="Ouvrir un diagramme biplot et ternaire",command=lambda: calculateur("ajout"))
    ajout.grid(row=1 ,column=0)
    ouvrir_popup= Button(my_frame,text="Ajouter un élément ou une l’image d’une région spectrale",command=lambda: calculateur("ouvrir_popup"))
    ouvrir_popup.grid(row=2 ,column=0)



def classification():
    global cadre8

    # Effacer le contenu existant du cadre8
    for widget in cadre8.winfo_children():
        widget.destroy()
    try:
        cm.datacube_creation()
        cm.load_table()
        cm.mineralcube_creation()
        cm.Minerals
        cm.plot_mineral_mask(cadre8)
        # Assurez-vous que le cadre8 ne change pas de dimension
        cadre8.grid_propagate(False)
    except AttributeError as e:
        messagebox.showerror("Erreur", "Une erreur s'est produite : " + str(e))

# Créer et configurer le bouton classification en dehors de la fonction
classification_button = tk.Button(cadre8, text="Show classification", command=classification)
classification_button.config(width=30, height=3)
classification_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


                                ###########'''APPEL DES FONCTIONS POUR L'INTERFACE'''###########

# créer le bouton avec l'icône et sans texte
bouton_parametres = Button(cadre1, image=icon_settings, command=open_settings)
bouton_parametres.pack(side="left", padx=15, pady=15)

my_label = Label(cadre1,text="")

# Ajouter les labels aux cadres correspondants
label2 = Label(cadre1, text="Images")
label2.pack(side="left", padx=65, pady=15)


# créer le bouton avec l'icône et sans texte
bouton_enregistrer = Button(cadre1, image=icon_save, command=save_image)
bouton_enregistrer.pack(side="right", padx=15, pady=15)

# créer le bouton avec l'icône et sans texte
bouton_update = Button(cadre3, image=icon_update, command=classification)
bouton_update.pack(side="left", padx=2, pady=15)


# créer le bouton avec l'icône et sans texte
bouton_ouvrir = Button(cadre1, image=icon_open, command=open_file)
bouton_ouvrir.pack(side="right", padx=15, pady=15)

# charger l'icône 
icon_open4 = PhotoImage(file="images/save.png")
icon_open4 = icon_open4.zoom(1)
# créer le bouton avec l'icône et sans texte
bouton_enregistrer2 = Button(cadre2, image=icon_save, command=save_file)
bouton_enregistrer2.pack(side="right", padx=15, pady=15)


# créer le bouton avec l'icône et sans texte
bouton_ouvrir2 = Button(cadre2, image=icon_open2, command=open_fileMask)
bouton_ouvrir2.pack(side="right", padx=15, pady=15)

bouton_plus = Button(cadre2, image=icon_plus, command=add_checkbutton)
bouton_plus.pack(side="left", padx=2, pady=15)

# créer le bouton avec l'icône et sans texte
bouton_moins = Button(cadre2, image=icon_moins, command=remove_checkbutton)
bouton_moins.pack(side="left", padx=2, pady=15)



'''Titre Masks'''
# Ajouter les labels aux cadres correspondants
label2 = Label(cadre2, text="Masks")
label2.pack(side="left", padx=65, pady=15)

# charger l'icône "folder.png" en tant qu'objet PhotoImage et la réduire de moitié
icon_open6 = PhotoImage(file="images/save.png")
icon_open6 = icon_open6.zoom(1)
# créer le bouton avec l'icône et sans texte
bouton_enregistrer6 = Button(cadre3, image=icon_save, command=save_classification)
bouton_enregistrer6.pack(side="right", padx=15, pady=15)

# créer le bouton avec l'icône et sans texte
bouton_parametres2 = Button(cadre3, image=icon_settings2, command=open_settings)
bouton_parametres2.pack(side="left", padx=15, pady=15)

# Ajouter les labels aux cadres correspondants
label2 = Label(cadre3, text="Classification")
label2.pack(side="left", padx=25, pady=15)  

try:
        # Créer et afficher votre interface ici
    fenetre.mainloop()
except KeyboardInterrupt:
        # Actions à effectuer avant de quitter
    print("Fermeture de l'interface...") 