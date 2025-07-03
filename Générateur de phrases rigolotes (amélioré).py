"Générateur de phrases rigolotes"

import pygame
import random

pygame.init()


# Couleurs
NOIR = (0, 0, 0)
BLANC = (255, 255, 255)
GRIS = (200, 200, 200)
BLEU = (100, 149, 237)
BLEU_CLAIR = (135, 179, 255)

#Couleurs phrases
ROUGE = (255, 0, 0)
VERT = (0, 255, 0)
JAUNE = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

#Liste des coueleurs pour les phrases
couleurs_phrases = [ROUGE, VERT, JAUNE, CYAN, MAGENTA]

# Polices
font = pygame.font.SysFont(None, 25)
font_bouton = pygame.font.SysFont(None, 36)

#Curseur initial
cursor_hand = pygame.SYSTEM_CURSOR_HAND
cursor_arrow = pygame.SYSTEM_CURSOR_ARROW

# Dimensions de la fenêtre
largeur, hauteur = 700, 450
ecran = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Phrases rigolotes")

# Rectangles pour le bouton et l'affichage de la phrase
bouton_rect = pygame.Rect(275, 300, 150, 50)
phrase_rect = pygame.Rect(50, 200, 600, 50)

# Liste de phrases rigolotes
liste_phrases = [
    "J’ai un emploi stable : je dors au boulot !",
    "Un jour sans rire est un jour perdu.",
    "Si dormir était un sport olympique, j’aurais l’or.",
    "La vie est courte… sauf les lundis.",
    "J’ai une idée de génie… mais elle fait la sieste.",
    "Je suis organisé : mon bazar est classé par couches.",
    "Mon téléphone a plus de mémoire que moi.",
    "Si j’étais payé à glander, je serais millionnaire.",
    "J’ai une idée de génie… mais elle fait la sieste.",

]

# Phrase actuelle affichée
phrase_actuelle = ""
couleur_phrase_actuelle = NOIR

# Boucle principale
en_cours = True
while en_cours:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            en_cours = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if bouton_rect.collidepoint(event.pos):
                phrase_actuelle = random.choice(liste_phrases)
                couleur_phrase_actuelle = random.choice(couleurs_phrases)

    # Position actuelle de la souris
    souris_pos = pygame.mouse.get_pos()
    if bouton_rect.collidepoint(souris_pos):
        couleur_bouton = BLEU_CLAIR
        couleur_tbouton = NOIR
    else:
        couleur_bouton = BLEU
        couleur_tbouton = BLANC

    #Changement du curseur
    if bouton_rect.collidepoint(souris_pos):
        pygame.mouse.set_cursor(cursor_hand)
    else:
        pygame.mouse.set_cursor(cursor_arrow)

    # Affichage
    ecran.fill(BLANC)

    
    # Titre
    titre = font_bouton.render("Générateur de phrases rigolotes", True, NOIR)
    ecran.blit(titre, (largeur // 2 - titre.get_width() // 2, 50))

    # Bouton
    pygame.draw.rect(ecran, couleur_bouton, bouton_rect)
    texte_b1 = font_bouton.render("Click ici!", True, couleur_tbouton)
    ecran.blit(texte_b1, (bouton_rect.x + 20, bouton_rect.y + 10))

    # Zone de la phrase
    pygame.draw.rect(ecran, GRIS, phrase_rect)
    if phrase_actuelle:
        texte_phrase = font.render(phrase_actuelle, True, couleur_phrase_actuelle)
        ecran.blit(texte_phrase, (phrase_rect.x + 10, phrase_rect.y + 10))

    pygame.display.flip()

pygame.quit()