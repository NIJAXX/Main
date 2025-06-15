"Chronomètre en ligne"

import pygame

# Initialisation de Pygame
pygame.init()

# Définition des couleurs
NOIR = (0, 0, 0)
BLANC = (255, 255, 255)
GRIS = (200, 200, 200)
BLEU = (100, 149, 237)

# Taille de la fenêtre
largeur, hauteur = 400, 300
ecran = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Chronomètre")

# Police
font = pygame.font.SysFont(None, 72)
font_bouton = pygame.font.SysFont(None, 36)

# Horloge
clock = pygame.time.Clock()
start_ticks = pygame.time.get_ticks()
pause = False
pause_ticks = 0

# Boucle principale
en_cours = True

# Définition des boutons
bouton_pause_rect = pygame.Rect(50, 220, 130, 50)
bouton_reset_rect = pygame.Rect(220, 220, 160, 50)


while en_cours:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            en_cours = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if bouton_pause_rect.collidepoint(event.pos):
                if not pause:
                    pause = True
                    pause_ticks = pygame.time.get_ticks()
                else:
                    pause = False
                    start_ticks += pygame.time.get_ticks() - pause_ticks

            elif bouton_reset_rect.collidepoint(event.pos):
                start_ticks = pygame.time.get_ticks()
                pause = False

    # Calcul du temps
    if not pause:
        elapsed_ms = pygame.time.get_ticks() - start_ticks
    else:
        elapsed_ms = pause_ticks - start_ticks

    # Rendu du texte
    elapsed_sec = elapsed_ms // 1000
    minutes = elapsed_sec // 60
    secondes = elapsed_sec % 60
    texte = f"{minutes:02}:{secondes:02}"

    rendu_texte = font.render(texte, True, NOIR)

    # Affichage
    ecran.fill(BLANC)
    
    # Affichage du chronomètre
    ecran.blit(rendu_texte, (largeur // 2 - rendu_texte.get_width() // 2, 50))

    # Affichage des boutons

    pygame.draw.rect(ecran, BLEU, bouton_pause_rect)
    pygame.draw.rect(ecran, GRIS, bouton_reset_rect)

    texte_pause = "Pause" if not pause else "Continuer"
    texte_b1 = font_bouton.render(texte_pause, True, BLANC)
    texte_b2 = font_bouton.render("Réinitialiser", True, NOIR)

    ecran.blit(texte_b1, (bouton_pause_rect.x + 10, bouton_pause_rect.y + 10))
    ecran.blit(texte_b2, (bouton_reset_rect.x + 10, bouton_reset_rect.y + 10))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
