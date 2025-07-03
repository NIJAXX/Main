import tkinter as tk

# Phrase cryptée et inversée
phrase_codee = ""

# Dictionnaire inverse des substitutions
substitutions_inverse = {
    '#': 'a',
    '7': 'o',
    '+': 'h',
}

def decoder_phrase(code):
    # Étape 1 : Réinverser la phrase
    phrase_reinversee = code[::-1]

    # Étape 2 : Restaurer les caractères originaux
    phrase_decodee = ""
    for c in phrase_reinversee:
        if c.lower() in substitutions_inverse:
            original = substitutions_inverse[c.lower()]
            if c.isupper():
                original = original.upper()
            phrase_decodee += original
        else:
            phrase_decodee += c
    return phrase_decodee

# Interface graphique avec Tkinter
def afficher_interface():
    def action_decoder():
        code = champ_code.get("1.0", tk.END).strip()
        resultat = decoder_phrase(code)
        champ_resultat.delete("1.0", tk.END)
        champ_resultat.insert(tk.END, resultat)

    fenetre = tk.Tk()
    fenetre.title("Décodeur de Phrase Cryptée")

    tk.Label(fenetre, text="Phrase cryptée :").pack()
    champ_code = tk.Text(fenetre, height=6, width=80)
    champ_code.insert(tk.END, phrase_codee)
    champ_code.pack()

    bouton_decoder = tk.Button(fenetre, text="Décoder", command=action_decoder)
    bouton_decoder.pack()

    tk.Label(fenetre, text="Phrase décodée :").pack()
    champ_resultat = tk.Text(fenetre, height=10, width=80)
    champ_resultat.pack()

    fenetre.mainloop()

# Lancement de l'interface
afficher_interface()