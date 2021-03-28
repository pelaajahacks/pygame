import pygame
import random

# initialize
pygame.init()

# create screen
screen = pygame.display.set_mode((1080, 720))

# title and icon
pygame.display.set_caption("Best game evurrr")
icon = pygame.image.load("assets/icon.png")
pygame.display.set_icon(icon)

# player
playerImg = pygame.image.load("assets/player.png")
playerImg = pygame.transform.scale(playerImg, (64, 64))
playerX = 540
playerY = 600
playerX_change = 0

# enemy
enemyImg = pygame.image.load("assets/enemy.png")
enemyImg = pygame.transform.scale(enemyImg, (64, 64))
enemyX = random.randint(50, 1000)
enemyY = 50
enemyX_change = 0.5
enemyY_change = 0


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


# main loop
running = True
while running:
    # basic display things
    screen.fill((200, 255, 255))

    # check events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                playerX_change = -1
            if event.key == pygame.K_d:
                playerX_change = 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                playerX_change = 0

        # exit
        if event.type == pygame.QUIT:
            print(event.type)
            running = False

    # change player coordinate
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 1020:
        playerX = 1020

    enemyX += enemyX_change
    if enemyX <= 0:
        enemyX_change = 0.5
        enemyY_change = -0.3
    elif enemyX >= 1020:
        enemyX_change = -0.5
        enemyY_change = -0.3

    player(playerX, playerY)

    enemy(enemyX, enemyY)

    pygame.display.update()
