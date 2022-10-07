#----Importing Modules and packages----#
import pygame
import random
import math

#----Window Setup and Pygame Setup----#
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("images/icon.png")
pygame.display.set_icon(icon)
background = pygame.image.load("images/background.png")

#----Player Setup----#
playerImg = pygame.image.load("images/player.png")
playerX = 370  # width x
playerY = 480  # height y
playerX_change = 0


def player(x, y):
    screen.blit(playerImg, (x, y))  # blit means draw


#----Enemy Setup----#
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load("images/enemy.png"))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(1.9)
    enemyY_change.append(0)


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


#----Bullet Setup----#
bulletImg = pygame.image.load("images/bullet.png")
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 40
bullet_state = "ready"

#--score Setup--#
score = 0

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))

#----Collision Setup----#
def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) +
                         (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


#----Game Loop----#
run = True
while run:
    screen.fill((0, 0, 0))  # rgb
    screen.blit(background, (0, 0))  # Drawing background
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #----Keystrokes Setup----#
        # KEYDOWN Event k
        # K stands for key
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -2.2
            if event.key == pygame.K_RIGHT:
                playerX_change = 2.2

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
        #--KEYUP Event k--#
        # K stands for key
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    #---Player Logic---#
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    player(playerX, playerY)

    #---Enemy Logic---#
    for i in range(num_of_enemies):
        enemyX[i] += enemyX_change[i]
    if enemyX[i] <= 0:
        enemyX_change[i] = 1.9
        enemyY[i] += enemyY_change[i]
    elif enemyX[i] >= 736:
        enemyX_change[i] = -1.9
        enemyY[i] += enemyY_change[i]

 #----Collision Logic Detection----#
    collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
    if collision:
        bulletY = 480
        bullet_state = "ready"
        score += 1
        print(score)
        enemyX[i] = random.randint(0, 736)
        enemyY[i] = random.randint(50, 150)
    
    enemy(enemyX[i], enemyY[i], i)

 #----Bullet Logic----#
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(playerX, bulletY)
        bulletY -= bulletY_change



    #----This update the game update()----#
 
    pygame.display.update()


# pygame.init()

# # Create the Screen
# screen = pygame.display.set_mode((800, 600))

# # background Image
# background = pygame.image.load("background.jpg")


# # Title and icon
# pygame.display.set_caption("Test Game")
# icon = pygame.image.load("space.png")  # 34px image
# pygame.display.set_icon(icon)

# # Player
# playerImg = pygame.image.load("player.png")  # 64px image
# playerX = 370
# playerY = 480
# playerX_change = 0

# # Enemy
# enemyImg = []
# enemyX = []
# enemyY = []
# enemyX_change = []
# enemyY_change = []
# num_of_enemies = 6

# for i in range(num_of_enemies):
#     enemyImg.append(pygame.image.load("enemy.png"))  # 64px image
#     enemyX.append(random.randint(0, 800))
#     enemyY.append(random.randint(50, 150))
#     enemyX_change.append(4)
#     enemyY_change.append(40)


# # Bullet
# # Ready - You can't see the bullet on the screen
# # Fire - the bullet is moving

# bulletImg = pygame.image.load("bullet.png")  # 64px image
# bulletX = 0
# bulletY = 480
# bulletX_change = 0
# bulletY_change = 10
# bullet_state = "ready"

# score = 0


# def player(x, y):
#     screen.blit(playerImg, (x, y))


# def enemy(x, y, i):
#     screen.blit(enemyImg[i], (x, y))


# def fire_bullet(x, y):
#     global bullet_state
#     bullet_state = "fire"
#     screen.blit(bulletImg, (x, y))


# def isCollision(x, y, bulletX, buttetY):
#     distance = math.sqrt((math.pow(enemyX - bulletX, 2)) +
#                          (math.pow(enemyY - bulletY, 2)))
#     if distance < 27:
#         return True
#     else:
#         return False


# # Game Loop
# run = True

# while run:

#     screen.fill((255, 214, 255))

#     # background Image
#     screen.blit(background, (0, 0))

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False

#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_LEFT:
#                 playerX_change = -1.9

#             if event.key == pygame.K_RIGHT:
#                 playerX_change = 1.9

#             if event.key == pygame.K_UP:
#                 if bullet_state is "ready":
#                     bulletX = playerX
#                     fire_bullet(playerX, bulletY)

#         if event.type == pygame.KEYUP:
#             if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
#                 playerX_change = 0

#     # checking for boundings
#     playerX += playerX_change

#     if playerX <= 0:
#         playerX = 0
#     elif playerX >= 736:
#         playerX = 736

#     # enemy movement
#     for i in range(num_of_enemies):
#         enemyX[i] += enemyX_change[i]
#         if enemyX[i] <= 0:
#             enemyX_change[i] = 4
#             enemyY[i] += enemyX_change[i]
#         elif enemyX[i] >= 736:
#             enemyX_change[i] = -2
#             enemyY[i] += enemyX_change[i]

#         # Collision
#         collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
#         if collision:
#             bulletY = 480
#             bullet_state = "ready"
#             score += 1
#             print(score)
#             enemyX[i] = random.randint(0, 735)
#             enemyY[i] = random.randint(50, 150)

#         enemy(enemyY[i], enemyY[i], i)

#     # Bullet movement
#     if bulletY <= 0:
#         bulletY = 480
#         bullet_state = "ready"
#     if bullet_state is "fire":
#         fire_bullet(bulletX, bulletY)
#         bulletY -= bulletY_change

#     enemy(enemyX, enemyY)
#     player(playerX, playerY)

#     pygame.display.update()
