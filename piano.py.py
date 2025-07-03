import tkinter as tk         # Pour créer la fenêtre et les boutons
from pygame import mixer     # Pour jouer des sons
import os                    # Pour trouver les fichiers sons

mixer.init()  # On démarre le lecteur de sons

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

notes = {
    "do": os.path.join(BASE_DIR, "sons", "do.wav"),
    "re": os.path.join(BASE_DIR, "sons", "re.wav"),
    "mi": os.path.join(BASE_DIR, "sons", "mi.wav"),
    "fa": os.path.join(BASE_DIR, "sons", "fa.wav"),
    "sol": os.path.join(BASE_DIR, "sons", "sol.wav"),
    "la": os.path.join(BASE_DIR, "sons", "la.wav"),
    "si": os.path.join(BASE_DIR, "sons", "si.wav")
}

touche_clavier = {
    "a": "do",
    "z": "re",
    "e": "mi",
    "r": "fa",
    "t": "sol",
    "y": "la",
    "u": "si"
}

# Couleurs spéciales par note
couleurs = {
    "do": "#FF6F61",    # rouge corail
    "re": "#6B5B95",    # violet
    "mi": "#88B04B",    # vert clair
    "fa": "#F7CAC9",    # rose pâle
    "sol": "#92A8D1",   # bleu clair
    "la": "#FAD02E",    # jaune
    "si": "#D65076"     # rose foncé
}

root = tk.Tk()
root.title("Piano Interactif 🎹")
root.geometry("600x300")  # Taille de la fenêtre

frame = tk.Frame(root)
frame.pack(pady=30)       # On met un peu d'espace autour

boutons = {}

def jouer_note(note):
    son = notes.get(note)
    if son and os.path.exists(son):
        mixer.Sound(son).play()
        # Changer la couleur du bouton
        bouton = boutons.get(note)
        if bouton:
            bouton.config(bg=couleurs[note])
            root.after(150, lambda: bouton.config(bg="white"))

for note in notes:
    btn = tk.Button(frame, text=note.upper(), width=8, height=10,
                    bg="white", command=lambda n=note: jouer_note(n))
    btn.pack(side="left", padx=5)
    boutons[note] = btn

def on_key_press(event):
    touche = event.char.lower()
    note = touche_clavier.get(touche)
    if note:
        jouer_note(note)

root.bind("<Key>", on_key_press)

root.mainloop()


































































