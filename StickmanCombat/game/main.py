import pygame
import requests

# ---------------- INIT ----------------
pygame.init()
WIDTH, HEIGHT = 1000, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("1v1 Sword Combat")
clock = pygame.time.Clock()

# ---------------- GET DATA FROM BACKEND ----------------
weapons = requests.get("http://127.0.0.1:8000/weapons").json()
weapon = weapons[0]   # Sword
DAMAGE = weapon[1]
RANGE = weapon[3]

# ---------------- COLORS ----------------
BG = (15, 15, 15)
PLAYER_COLOR = (255, 220, 0)
ENEMY_COLOR = (230, 230, 230)
SWORD_COLOR = (200, 200, 200)
HIT_FLASH = (70, 70, 70)

# ---------------- PLAYER ----------------
player = {
    "x": 200,
    "y": 320,
    "health": 100,
    "attacking": False,
    "attack_timer": 0
}

# ---------------- ENEMY ----------------
enemy = {
    "x": 750,
    "y": 320,
    "health": 100,
    "cooldown": 0
}

# ---------------- DRAW FUNCTION ----------------
def draw_fighter(x, y, color, attack=False, facing=1):
    # head
    pygame.draw.circle(screen, color, (x, y - 35), 14)
    # body
    pygame.draw.line(screen, color, (x, y - 15), (x, y + 50), 5)
    # legs
    pygame.draw.line(screen, color, (x, y + 50), (x - 15, y + 90), 5)
    pygame.draw.line(screen, color, (x, y + 50), (x + 15, y + 90), 5)

    # arm + sword
    if attack:
        pygame.draw.line(screen, color, (x, y), (x + facing * 70, y), 6)
        pygame.draw.line(
            screen, SWORD_COLOR,
            (x + facing * 70, y),
            (x + facing * 100, y - 10),
            4
        )
    else:
        pygame.draw.line(screen, color, (x, y), (x + facing * 30, y + 10), 5)

# ---------------- HIT EFFECT ----------------
def hit_effect():
    screen.fill(HIT_FLASH)
    pygame.display.update()
    pygame.time.delay(25)

# ---------------- GAME LOOP ----------------
running = True
while running:
    clock.tick(60)
    screen.fill(BG)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # -------- PLAYER MOVE --------
    if keys[pygame.K_LEFT]:
        player["x"] -= 5
    if keys[pygame.K_RIGHT]:
        player["x"] += 5

    # -------- PLAYER ATTACK --------
    if keys[pygame.K_SPACE] and not player["attacking"]:
        player["attacking"] = True
        player["attack_timer"] = 10

        if abs(player["x"] - enemy["x"]) < RANGE:
            enemy["health"] -= DAMAGE
            enemy["x"] += 20
            hit_effect()

    # attack timer
    if player["attacking"]:
        player["attack_timer"] -= 1
        if player["attack_timer"] <= 0:
            player["attacking"] = False

    # -------- ENEMY AI --------
    if enemy["cooldown"] > 0:
        enemy["cooldown"] -= 1
    else:
        if abs(enemy["x"] - player["x"]) > 70:
            enemy["x"] -= 2 if enemy["x"] > player["x"] else -2
        else:
            player["health"] -= 5
            enemy["cooldown"] = 40
            hit_effect()

    # -------- DRAW --------
    draw_fighter(player["x"], player["y"], PLAYER_COLOR, player["attacking"], 1)
    draw_fighter(enemy["x"], enemy["y"], ENEMY_COLOR, enemy["cooldown"] > 30, -1)

    # -------- UI --------
    pygame.draw.rect(screen, (200, 0, 0), (40, 30, player["health"] * 2, 10))
    pygame.draw.rect(screen, (200, 0, 0), (WIDTH - 260, 30, enemy["health"] * 2, 10))

    pygame.display.update()

pygame.quit()
