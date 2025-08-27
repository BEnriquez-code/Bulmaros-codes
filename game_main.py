import pygame
import random
import math
from pygame import mixer

pygame.init()

# Screen setup
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Astronaut")

# Load assets
icon = pygame.image.load('arcade-game.png')
pygame.display.set_icon(icon)
background = pygame.image.load('pixil-frame-0.png')

#Explosion frames
explosion_frames = [
    pygame.image.load("pixil-layer-2.png"),
    pygame.image.load("pixil-layer-1.png"),
    pygame.image.load("pixil-layer-0.png")
]
explosions = []

# Background Sound
mixer.music.load("background.wav")
mixer.music.play(-1)

# Player
playerImg = pygame.image.load("pixil-frame-0 (2).png")
playerX = 370
playerY = 286
playerX_change = 0

# Ground Enemy
enemyImg = pygame.image.load("ailenpxl-drawing.png")
enemies = []
spawn_timer = 0

# Flying Enemy
fly_enemyImg = pygame.image.load("pixil-frame-0 (flying).png")
fly_enemies = []
fly_spawn_timer = 0
fly_shoot_cooldown = 1000
last_fly_shot_time = 0
flying_kills = 0

# Boss
bossImg = pygame.image.load("ailenpxl-drawing.png")
boss = None
boss_health = 20
boss_bullets = []
boss_shoot_cooldown = 800
boss_spawn_threshold = 10

# Player Bullet
bulletImg = pygame.image.load("bullet.png")
bullet_speed = 4
bullets = []
last_shot_time = 0
shot_cooldown = 750  # miliseconds

# Enemy Bullet
enemy_bullet_img = pygame.image.load("bullet.png")
enemy_bullets = []
enemy_bullet_speed = 2

# Score
score_value = 0
font = pygame.font.Font("freesansbold.ttf", 32)
textX = 10
textY = 10

# Game over text
over_font = pygame.font.Font("freesansbold.ttf", 64)
game_over = False

# Game mode
flying_mode = False

def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def game_over_text():
    over_text = over_font.render("Game Over", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))

def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y):
    screen.blit(enemyImg, (x, y))

def fly_enemy(x, y):
    screen.blit(fly_enemyImg, (x, y))
def draw_boss_health(boss):
    if boss:
        pygame.draw.rect(screen, (255,0,0), (boss["x"], boss["y"] - 20, 100, 10))
        pygame.draw.rect(screen, (0,255,0), (boss["x"], boss["y"] - 20, int(100*(boss["health"]/ boss_health)), 10))

def spawn_enemy():
    side = random.choice(["left", "right"])
    y = playerY
    if side == "left":
        x = -50
        x_change = 0.3
    else:
        x = 850
        x_change = -0.3
    enemies.append({"x": x, "y": y, "x_change": x_change})

def fire_bullet(x, y, target_x, target_y):
    bullet_x = x + playerImg.get_width() // 2 - bulletImg.get_width() // 2
    bullet_y = y + playerImg.get_height() // 2 - bulletImg.get_height() // 2
    dx = target_x - bullet_x
    dy = target_y - bullet_y
    distance = math.hypot(dx, dy)
    if distance == 0:
        distance = 1
    dx /= distance
    dy /= distance
    bullets.append({"x": bullet_x, "y": bullet_y, "dx": dx, "dy": dy})

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.hypot(enemyX - bulletX, enemyY - bulletY)
    return distance < 45

def isPlayerCollision(enemyX, enemyY, playerX, playerY):
    distance = math.hypot(enemyX - playerX, enemyY - playerY)
    return distance < 40

def add_explosion(x, y, enemyImg, fly_enemyImg):
    frame = explosion_frames[0]
    rect = frame.get_rect()
    explosions.append({"x":x + enemyImg.get_width()//2 - rect.width//2, "y":y + enemyImg.get_height() //2 - rect.height//2, "frame": 0, "time": pygame.time.get_ticks()})

# Game loop
running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                playerX_change = -1.5
            if event.key == pygame.K_d:
                playerX_change = 1.5

        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_a, pygame.K_d):
                playerX_change = 0

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                current_time = pygame.time.get_ticks()
                if current_time - last_shot_time > shot_cooldown:
                    bullet_Sound = mixer.Sound("laser.wav")
                    bullet_Sound.play()
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    fire_bullet(playerX, playerY, mouse_x, mouse_y)
                    last_shot_time = current_time

    if not game_over:
        playerX += playerX_change
        playerX = max(0, min(playerX, 736))

        # Switch to flying mode after 20 points
        if score_value >= 15:
            if not flying_mode:
                flying_mode = True
                enemies.clear()  # Remove remaining ground enemies
                
        #Spawn boss after flying enemies
        if flying_kills >= boss_spawn_threshold and boss is None:
            boss = {
                "x": 300,
                "y": 50,
                "health": boss_health,
                "last_shot_time": 0,
                "dx": 1.5}
        #Boss behavoir
        if boss:
            screen.blit(bossImg, (boss["x"], boss["y"]))
            draw_boss_health(boss)

            if current_time - boss["last_shot_time"] > boss_shoot_cooldown:
                dx = playerX - boss["x"]
                dy = playerY - boss["y"]
                dist = math.hypot(dx, dy)
                if dist == 0:
                    dist = 1
                dx /= dist
                dy /= dist
                boss_bullets.append({"x": boss["x"], "y": boss["y"], "dx":dx, "dy":dy})
                boss["last_shot_time"] = current_time
                
            #boss movement
            boss["x"] += boss["dx"]
            if boss["x"] > 700:
                boss["x"] = 700
                boss["dx"] = -1.5
            if boss["x"] < 0:
                boss["x"] = 0
                boss["dx"] = 1.5

            for bb in boss_bullets[:]:
                bb["x"] += bb["dx"] *2
                bb["y"] += bb["dy"] *2
                screen.blit(enemy_bullet_img, (bb["x"], bb["y"]))
                # remove if off screen
                if bb["x"] < -50 or bb["x"] > 850 or bb["y"] < -50 or bb["y"] > 650:
                    boss_bullets.remove(bb)

                if bb["y"] >= 335:
                    boss_bullets.remove(bb)
                    continue
                if math.hypot(bb["x"] - playerX, bb["y"] - playerY) < 30:
                    game_over = True
                    boss_bullets.remove(bb)
                
            for bullet in bullets[:]:
                if math.hypot(bullet["x"] - boss["x"], bullet["y"] - boss["y"]) <40:
                    bullets.remove(bullet)
                    boss["health"] -= 1
                    if boss["health"] <= 0:
                        explosion_Sound = mixer.Sound("explosion.wav")
                        explosion_Sound.play()
                        add_explosion(boss["x"], boss["y"], bossImg)
                        boss = None
                        game_over = True

        # Spawn ground enemies if not in flying mode
        if not flying_mode:
            spawn_timer += 1
            if spawn_timer > 120:
                spawn_enemy()
                spawn_timer = 0

        # Spawn flying enemies(only if boss isn't active)
        if flying_mode and boss is None:
            fly_spawn_timer += 1
            if fly_spawn_timer > 300:
                x = random.randint(100, 700)
                fly_enemies.append({"x": x, "y": 50, "last_shot_time":0, "spawn_time": pygame.time.get_ticks()})
                fly_spawn_timer = 0

        # Update ground enemies
        for enemy_data in enemies[:]:
            enemy_data["x"] += enemy_data["x_change"]
            enemy(enemy_data["x"], enemy_data["y"])

            if enemy_data["x"] < -60 or enemy_data["x"] > 860:
                enemies.remove(enemy_data)
                continue

            if isPlayerCollision(enemy_data["x"], enemy_data["y"], playerX, playerY):
                game_over = True

            for bullet in bullets[:]:
                if isCollision(enemy_data["x"], enemy_data["y"], bullet["x"], bullet["y"]):
                    explosion_Sound = mixer.Sound("explosion.wav")
                    explosion_Sound.play()
                    add_explosion(enemy_data["x"], enemy_data["y"], enemyImg, fly_enemyImg)
                    bullets.remove(bullet)
                    enemies.remove(enemy_data)
                    score_value += 1
                    break

        # Update flying enemies and shoot
        current_time = pygame.time.get_ticks()
        for fly in fly_enemies[:]:
            fly_enemy(fly["x"], fly["y"])

            # Shoot at player only after cooldown after spawn
            if current_time - fly["last_shot_time"] > fly_shoot_cooldown and current_time - fly["spawn_time"] > 500:
                fx, fy = fly["x"], fly["y"]
                dx = playerX - fx
                dy = playerY - fy
                dist = math.hypot(dx, dy)
                if dist == 0:
                    dist = 1
                dx /= dist
                dy /= dist
                enemy_bullets.append({"x": fx, "y": fy, "dx": dx, "dy": dy})
                fly["last_shot_time"] = current_time

            # Check collision with bullets
            for bullet in bullets[:]:
                if isCollision(fly["x"], fly["y"], bullet["x"], bullet["y"]):
                    explosion_Sound = mixer.Sound("explosion.wav")
                    explosion_Sound.play()
                    add_explosion(fly["x"], fly["y"], enemyImg, fly_enemyImg)
                    bullets.remove(bullet)
                    fly_enemies.remove(fly)
                    score_value += 2
                    flying_kills += 1
                    break

        # Update player bullets
        for bullet in bullets[:]:
            bullet["x"] += bullet["dx"] * bullet_speed
            bullet["y"] += bullet["dy"] * bullet_speed
            screen.blit(bulletImg, (bullet["x"], bullet["y"]))
            if (bullet["x"] < -50 or bullet["x"] > 850 or
            bullet["y"] < -50 or bullet["y"] > 335):
                bullets.remove(bullet)

        # Update enemy bullets
        for eb in enemy_bullets[:]:
            eb["x"] += eb["dx"] * enemy_bullet_speed
            eb["y"] += eb["dy"] * enemy_bullet_speed
            screen.blit(enemy_bullet_img, (eb["x"], eb["y"]))
            if (bullet["x"] < -50 or bullet["x"] > 850 or
            bullet["y"] < -50 or bullet["y"] > 335):
                bullets.remove(bullet)

            if math.hypot(eb["x"] - playerX, eb["y"] - playerY) < 30:
                game_over = True

            if eb["x"] < -50 or eb["x"] > 850 or eb["y"] < -50 or eb["y"] > 335:
                enemy_bullets.remove(eb)

        # Update and draw explosions
        for explosion in explosions[:]:
            frame = explosion["frame"]
            screen.blit(explosion_frames[frame], (explosion["x"], explosion["y"]))

            #advance frame every 100 miliseconds
            if pygame.time.get_ticks() - explosion["time"] > 100:
                explosion["frame"] += 1
                explosion["time"] = pygame.time.get_ticks()

            #remove when finished
            if explosion["frame"] >= len(explosion_frames):
                explosions.remove(explosion)

        player(playerX, playerY)
        show_score(textX, textY)
    else:
        game_over_text()
        pygame.display.update()
        pygame.time.wait(2000)
        running = False

    pygame.display.update()

pygame.quit()
