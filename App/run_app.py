import tkinter as tk
from tkinter import font
from assets import conjuguer
from time import sleep

app = tk.Tk()
Ubuntu = font.Font(font="Ubuntu")

class data():
    temps = None
    radical = None
    groupe = None
    compose = None
    avancer = 0
    control_avancer = 1

def suite():
    if data.avancer == 0 and data.control_avancer == 1:
        data.avancer = 1
        data.temps = enter0.get()
        data.control_avancer = 0
        label1.config(text="Ecrit le radical:")
    elif data.avancer == 1 and data.control_avancer == 1:
        data.avancer = 2
        data.radical = enter0.get()
        data.control_avancer = 0
        label1.config(text="Ecrit le groupe:")
    elif data.avancer == 2 and data.control_avancer == 1:
        data.avancer = 3
        data.groupe = enter0.get()
        data.control_avancer = 0
        label1.config(text="Ecrit Oui s'il c'est un temps composé sinon valide:")
    elif data.avancer == 3 and data.control_avancer == 1:
        data.avancer = 4
        if enter0.get() == "Oui":
            data.compose = "1"
        else:
            data.compose = "0"
        data.control_avancer = 0
        label0.config(text=f"Temps: {data.temps}, radical: {data.radical}, groupe: {data.groupe}, compose: {data.compose}")
        label1.config(text="Clique sur démarer pour commencer la conjugaison:")
        enter0.destroy()
        button0.config(text="Démarer")
    elif data.avancer == 4 and data.control_avancer == 1:
        print("Start to Conjug !!")
        data.control_avancer = 0
        button0.destroy()
        label1.config(text="Tâche en cour....")
        conjug = conjuguer.conjuguer(temps=data.temps, radical=data.radical, groupe=data.groupe, compose=data.compose)
        # affiche conjug (extraire with "je" puis "tu" ...
        label1.config(text="C'est fini voici la conjugaison (6s left before auto closing the application):")
        label2 = tk.Label(app, text=conjug, fg="white", bg="black", font=Ubuntu)
        label2.pack(pady=10)
        app.geometry("700x500")
        sleep(6)
        app.destroy()

    data.control_avancer = 1
    if data.avancer <= 3:
        enter0.delete(0, 'end')

def appli():
    app.title("Auto_Conjug")
    app.geometry("500x500")
    app.config(bg="black")

    global label0
    label0 = tk.Label(app, text="Welcome !!", fg="white", bg="black", font=Ubuntu)
    label0.pack(pady=10)
    global label1
    label1 = tk.Label(app, text="Ecrit le temps ici:", fg="white", bg="black", font=Ubuntu)
    label1.pack(pady=10)
    global enter0
    enter0 = tk.Entry(app, bg="black", fg="white")
    enter0.pack(pady=10)
    global button0
    button0 = tk.Button(app, text="Valider", command=suite)
    button0.pack(pady=10)

    app.mainloop()

if __name__ == "__main__":
    appli()