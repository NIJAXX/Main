import turtle

#dessiner les drapeaux en vertical
def dessiner_drapeau_vertical(t, x, y, couleurs, largeur=90, hauteur=150):
    """Dessine un drapeau à bandes verticales (ex: France, Italie)"""
    t.penup()
    t.goto(x, y)
    t.pendown()
    
    largeur_bande = largeur // len(couleurs)
    for couleur in couleurs:
        t.fillcolor(couleur)
        t.begin_fill()
        for _ in range(2):
            t.forward(largeur_bande)
            t.right(90)
            t.forward(hauteur)
            t.right(90)
        t.end_fill()
        t.forward(largeur_bande)

#dessiner les drapeaux en horizontal
def dessiner_drapeau_horizontal(t, x, y, couleurs, largeur=120, hauteur=90):
    """Dessine un drapeau à bandes horizontales (ex: Allemagne, Russie)"""
    bande_hauteur = hauteur // len(couleurs)
    t.penup()
    t.goto(x, y)
    t.setheading(0)
    t.pendown()

    for couleur in couleurs:
        t.fillcolor(couleur)
        t.begin_fill()
        for _ in range(2):
            t.forward(largeur)
            t.right(90)
            t.forward(bande_hauteur)
            t.right(90)
        t.end_fill()
        t.right(90)
        t.forward(bande_hauteur)
        t.left(90)

# Configuration de la fenêtre
turtle.bgcolor("white")
t = turtle.Turtle()
t.speed(5)

# 🇫🇷 France (bandes verticales bleu-blanc-rouge)
dessiner_drapeau_vertical(t, -300, 150, ["blue", "white", "red"])
t.penup()
t.goto(-270, -20)
t.write("France", align="center", font=("Arial", 12, "bold"))

# 🇩🇪 Allemagne (bandes horizontales noir-rouge-jaune)
dessiner_drapeau_horizontal(t, -150, 150, ["black", "red", "yellow"])
t.penup()
t.goto(-90, -20)
t.write("Allemagne", align="center", font=("Arial", 12, "bold"))

# 🇮🇹 Italie (bandes verticales vert-blanc-rouge)
dessiner_drapeau_vertical(t, 50, 150, ["green", "white", "red"])
t.penup()
t.goto(80, -20)
t.write("Italie", align="center", font=("Arial", 12, "bold"))

# 🇷🇺 Russie (bandes horizontales blanc-bleu-rouge)
dessiner_drapeau_horizontal(t, 200, 150, ["white", "blue", "red"])
t.penup()
t.goto(260, -20)
t.write("Russie", align="center", font=("Arial", 12, "bold"))

t.hideturtle()
turtle.done()