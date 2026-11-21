import os, sys, random
import pygame
from game import Game

# Always run relative to this file so assets load no matter where it's launched from
os.chdir(os.path.dirname(os.path.abspath(__file__)))

pygame.init()

SCREEN_WIDTH = 750
SCREEN_HEIGHT = 700
OFFSET = 50

# Palette
BG_TOP = (10, 8, 30)
BG_BOTTOM = (38, 12, 62)
ACCENT = (64, 224, 255)      # cyan
ACCENT_2 = (255, 70, 200)    # magenta
TEXT = (235, 240, 255)

font = pygame.font.Font("Font/monogram.ttf", 40)
big_font = pygame.font.Font("Font/monogram.ttf", 72)
small_font = pygame.font.Font("Font/monogram.ttf", 28)

screen = pygame.display.set_mode((SCREEN_WIDTH + OFFSET, SCREEN_HEIGHT + 2 * OFFSET))
pygame.display.set_caption("NEBULA DEFENDERS")

clock = pygame.time.Clock()
game = Game(SCREEN_WIDTH, SCREEN_HEIGHT, OFFSET)

# --- Background: vertical gradient + three layers of drifting stars ---
W, H = screen.get_size()
background = pygame.Surface((W, H))
for y in range(H):
    t = y / H
    color = tuple(int(BG_TOP[i] + (BG_BOTTOM[i] - BG_TOP[i]) * t) for i in range(3))
    pygame.draw.line(background, color, (0, y), (W, y))

stars = []
for layer, (count, speed, size, shade) in enumerate(
        [(40, 0.2, 1, 90), (25, 0.5, 2, 150), (12, 1.0, 2, 230)]):
    for _ in range(count):
        stars.append([random.uniform(0, W), random.uniform(0, H), speed, size, shade])

def draw_stars():
    for s in stars:
        s[1] += s[2]
        if s[1] > H:
            s[0], s[1] = random.uniform(0, W), 0
        c = s[4]
        pygame.draw.rect(screen, (c, c, min(255, c + 20)), (s[0], s[1], s[3], s[3]))

SHOOT_LASER = pygame.USEREVENT
pygame.time.set_timer(SHOOT_LASER, 300)

MYSTERYSHIP = pygame.USEREVENT + 1
pygame.time.set_timer(MYSTERYSHIP, random.randint(4000, 8000))

def centered(surface, y):
    screen.blit(surface, surface.get_rect(center=(W // 2, y)))

while True:
    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SHOOT_LASER and game.run:
            game.alien_shoot_laser()
        if event.type == MYSTERYSHIP and game.run:
            game.create_mystery_ship()
            pygame.time.set_timer(MYSTERYSHIP, random.randint(4000, 8000))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and not game.run:
        game.reset()

    # Update
    if game.run:
        game.spaceship_group.update()
        game.move_aliens()
        game.alien_lasers_group.update()
        game.mystery_ship_group.update()
        game.check_for_collisions()

    # Draw
    screen.blit(background, (0, 0))
    draw_stars()

    # Frame
    pygame.draw.rect(screen, ACCENT, (10, 10, 780, 780), 2, 0, 60, 60, 60, 60)
    pygame.draw.line(screen, ACCENT_2, (25, 730), (775, 730), 3)

    status = "WAVE 01" if game.run else "GAME OVER"
    screen.blit(font.render(status, False, ACCENT_2), (570, 740))

    x = 50
    for _ in range(game.lives):
        screen.blit(game.spaceship_group.sprite.image, (x, 742))
        x += 70

    screen.blit(font.render("SCORE", False, ACCENT), (50, 15))
    screen.blit(font.render(str(game.score).zfill(5), False, TEXT), (50, 40))
    screen.blit(font.render("BEST", False, ACCENT), (600, 15))
    screen.blit(font.render(str(game.highscore).zfill(5), False, TEXT), (600, 40))

    game.spaceship_group.draw(screen)
    game.spaceship_group.sprite.lasers_group.draw(screen)
    for obstacle in game.obstacles:
        obstacle.blocks_group.draw(screen)
    game.aliens_group.draw(screen)
    game.alien_lasers_group.draw(screen)
    game.mystery_ship_group.draw(screen)

    if not game.run:
        centered(big_font.render("GAME OVER", False, ACCENT_2), 330)
        centered(small_font.render("PRESS SPACE TO PLAY AGAIN", False, TEXT), 390)

    pygame.display.update()
    clock.tick(60)
