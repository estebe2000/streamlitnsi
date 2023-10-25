import pyxel
import random

# Initialisation des variables
x, y = 50, 50
SIZE = 16  # Taille de sprite dans Pyxel
SPEED = 2
WIDTH, HEIGHT = 160, 120
win_count, lose_count = 0, 0
message_time = 0
game_state = "playing"
win = False

def update():
    global x, y, game_state, win_count, lose_count, message_time, win

    # Quitter le jeu
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()

    # Mouvement
    x += (pyxel.btn(pyxel.KEY_RIGHT) - pyxel.btn(pyxel.KEY_LEFT)) * SPEED
    y += (pyxel.btn(pyxel.KEY_DOWN) - pyxel.btn(pyxel.KEY_UP)) * SPEED

    x = max(0, min(WIDTH - SIZE, x))
    y = max(0, min(HEIGHT - SIZE, y))

    # Tirage au sort
    if pyxel.btnp(pyxel.KEY_SPACE):
        result = random.choice(['pile', 'face'])
        handle_random_choice(result)

def handle_random_choice(result):
    global win_count, lose_count, message_time, win

    if (result == 'pile' and x < WIDTH // 2) or (result == 'face' and x > WIDTH // 2):
        win = True
        win_count += 1
    else:
        win = False
        lose_count += 1

    message_time = pyxel.frame_count

def draw():
    pyxel.cls(0)

    # Dessiner les pièces (cercles)
    pyxel.circ(WIDTH // 4, HEIGHT // 2, 20, 8)
    pyxel.circ(3 * WIDTH // 4, HEIGHT // 2, 20, 8)

    # Ajouter "P" et "F" dans les cercles
    pyxel.text(WIDTH // 4 - 3, HEIGHT // 2 - 3, "P", 7)
    pyxel.text(3 * WIDTH // 4 - 3, HEIGHT // 2 - 3, "F", 7)

    # Dessiner le joueur (carré)
    pyxel.rect(x, y, SIZE, SIZE, 12)

    # Afficher le nombre de victoires et de défaites
    pyxel.text(5, 5, f"Victoires : {win_count}", 7)
    pyxel.text(5, 15, f"Defaites : {lose_count}", 7)

    # Afficher un message pour la victoire ou la défaite
    if pyxel.frame_count - message_time < 60:  # 60 frames == 1 seconde dans Pyxel
        msg = "Victoire !" if win else "Defaite !"
        pyxel.text(WIDTH//2 - 20, HEIGHT//2, msg, 8 if win else 6)

# Initialisation de Pyxel
pyxel.init(WIDTH, HEIGHT)
pyxel.run(update, draw)
