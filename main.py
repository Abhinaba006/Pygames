import pygame
import random

pygame.init()  # init game

# create  screen
screen = pygame.display.set_mode((800, 600))
running = True

# title and logo
pygame.display.set_caption('Space')
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)

# background
background = pygame.image.load('14998.jpg')

# player
playerImg = pygame.image.load('player.png')
playerX = 370
playerX_change = 0
playerY = 500

# bullet
# ready means i cant see the bullete
# fire - motion
bulletimg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"

# enemy

enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
nOfen=10
enemyimg = pygame.image.load('coronavirus.png')
for _ in range(nOfen):
    enemyX.append(random.randint(0, 750))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(3)
    enemyY_change.append(0)

#score
score_value = 0
font = pygame.font.SysFont('freesansbold.ttf', 70)
textX = 10
testY = 10

def show_score(x, y):
    score = font.render("Score: "+str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def player(x, y):
    # blit draw on screen
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyimg, (x, y))


def bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletimg, (x + 16, y + 10))


def collison(enemyX, enemyY, bulletX, bulletY):
    dis = (((enemyX - bulletX) ** 2) + ((enemyY - bulletY) ** 2)) ** .5
    if dis < 27:
        return True
    return False

Gfont = pygame.font.SysFont('freesansbold.ttf', 100)
def gameOver():
    score = Gfont.render("GAME OVER!!Score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (50, 250))


# game loop
while running:
    screen.fill((0, 150, 0))
    # back
    screen.blit(background, (0, 0))
    # playerX += .1
    # this make sure that i get all the events in the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if key is pressed check it is right or left
        if event.type == pygame.KEYDOWN:  # chk any key is pressed
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletX = playerX
                    bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP:  # chk any key is released
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                playerX_change = 0

    # any thing on the screen run will b in this loop
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    if playerX >= 735:
        playerX = 735

    for i in range(nOfen):

        if enemyY[i]>450:
            for j in range(nOfen):
                enemyY[j] = 2000
            gameOver()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 5
            enemyY[i] += 15
        if enemyX[i] >= 735:
            enemyX_change[i] = -5
            enemyY[i] += 15

        # col
        col = collison(enemyX[i], enemyY[i], bulletX, bulletY)
        if col:
            bullet_state = "ready"
            score_value += 1
            bulletY = 480
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 400)
        enemy(enemyX[i], enemyY[i])

    # bullete movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state == "fire":
        bullet(bulletX, bulletY)
        bulletY -= 10




    player(playerX, playerY)
    show_score(0, 0)
    # any change needs to be updated in this loop
    pygame.display.update()
