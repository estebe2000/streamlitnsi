import pyxel


# taille de la fenetre 128x128 pixels
# ne pas modifier
pyxel.init(128, 128, title="Nuit du c0de")

# position initiale du vaisseau
# (origine des positions : coin haut gauche)
vaisseau_x = 60
vaisseau_y = 60
vitesse = 1

# couleur du vaisseau
vaisseau_couleur = 1

def vaisseau_deplacement(x, y):
    """déplacement avec les touches de directions"""

    if pyxel.btn(pyxel.KEY_RIGHT):
        if (x < 120):
            x = x + vitesse
    if pyxel.btn(pyxel.KEY_LEFT):
        if (x > 0):
            x = x - vitesse
    if pyxel.btn(pyxel.KEY_DOWN):
        if (y < 120):
            y = y + vitesse
    if pyxel.btn(pyxel.KEY_UP):
        if (y > 0):
            y = y - vitesse
    return x, y

def update():
    """mise à jour des variables (30 fois par seconde)"""
    global vaisseau_x, vaisseau_y, vaisseau_couleur

    # mise à jour de la position du vaisseau
    vaisseau_x, vaisseau_y = vaisseau_deplacement(vaisseau_x, vaisseau_y)

    # vérifier si la touche d'espace est enfoncée
    if pyxel.btnp(pyxel.KEY_SPACE):
        # changer la couleur du carré
        if vaisseau_couleur == 1:
            vaisseau_couleur = 2
        else:
            vaisseau_couleur = 1

def draw():
    """création des objets (30 fois par seconde)"""
    pyxel.cls(0)  # vide la fenetre

    # vaisseau (carre 8x8)
    pyxel.rect(vaisseau_x, vaisseau_y, 8, 8, vaisseau_couleur)

pyxel.run(update, draw)
