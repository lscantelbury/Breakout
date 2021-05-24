import pygame
pygame.init()

# Making new window 
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Breakout - PyGame Edition - 2021.05.21")

# Defining colors used in the game 

white = (255, 255, 255)
red = (255, 100, 0)
orange = (255, 100, 0)
yellow = (255,255,0)
black = (0, 0, 0)

score = 0
lives = 2

# Brick's first roll
'''c1 = pygame.image.load("assets/brick1.png")
c2 = pygame.image.load("assets/brick1.png")
c3 = pygame.image.load("assets/brick1.png")
c4 = pygame.image.load("assets/brick1.png")
c5 = pygame.image.load("assets/brick1.2.png")
c6 = pygame.image.load("assets/brick1.2.png")
c7 = pygame.image.load("assets/brick1.png")
c8 = pygame.image.load("assets/brick1.png")
c9 = pygame.image.load("assets/brick1.png")
c10 = pygame.image.load("assets/brick1.png")
# Brick's second roll
b1 = pygame.image.load("assets/brick2.png")
b2 = pygame.image.load("assets/brick2.png")
b3 = pygame.image.load("assets/brick2.png")
b4 = pygame.image.load("assets/brick2.png")
b5 = pygame.image.load("assets/brick2.2.png")
b6 = pygame.image.load("assets/brick2.2.png")
b7 = pygame.image.load("assets/brick2.png")
b8 = pygame.image.load("assets/brick2.png")
b9 = pygame.image.load("assets/brick2.png")
b10 = pygame.image.load("assets/brick2.png")'''
# Brick's third roll
a1 = pygame.image.load("assets/brick3.png")
a2 = pygame.image.load("assets/brick3.png")
a3 = pygame.image.load("assets/brick3.png")
a4 = pygame.image.load("assets/brick3.png")
a5 = pygame.image.load("assets/brick3.2.png")
a6 = pygame.image.load("assets/brick3.2.png")
a7 = pygame.image.load("assets/brick3.png")
a8 = pygame.image.load("assets/brick3.png")
a9 = pygame.image.load("assets/brick3.png")
a10 = pygame.image.load("assets/brick3.png")

#Creating Paddle
paddle = pygame.image.load("assets/paddle.png")
paddle_x = 325
paddle_right = False
paddle_left = False

# ball
ball = pygame.image.load("assets/ball.png")
ball_x = 640
ball_y = 360
sideimpulse = True

vel1 = 6
vel2 = 8
vel3 = 10

ball_dx = -vel1
ball_dy = -vel1

# Variable for the following while loop
game_loop = True
fps = pygame.time.Clock()

while game_loop:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False
        
        #  keystroke events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                paddle_right = True
            if event.key == pygame.K_LEFT:
                paddle_left = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                paddle_right = False
            if event.key == pygame.K_LEFT:
                paddle_left = False
        

    screen.fill(black)
    pygame.draw.line(screen, white, [0, 38],
                    [800, 38], 2)

    #Score and Number of lives at the bottom of screen
    font = pygame.font.Font(None, 34)
    text = font.render("Score: " + str(score), 1, white)
    screen.blit(text, (20,10))
    text = font.render("Lives: " + str(lives), 1, white)
    screen.blit(text, (650, 10))

    # ball movement
    ball_x = ball_x + ball_dx
    ball_y = ball_y + ball_dy

    # paddle right movement
    if paddle_right:
        if paddle_x <= 650:
            paddle_x += 10
    else:
        paddle_x += 0

    # paddle 1 left movement
    if paddle_left:
        if paddle_x >= 0:
            paddle_x -= 10
    else:
        paddle_x += 0

    # ball collision with upper wall
    if ball_y <= 40:
        ball_dy *= -1

    # ball collision with left wall
    if ball_x <= 0:
        ball_dx *= -1
    
    # ball collision with right wall
    if ball_x >= 790:
        ball_dx *= -1

     # ball collision with floor
    if ball_y > 590:
        ball_dy *= -1 
        lives -= 1
        if lives == 0:
            #Display Game Over Message for 3 seconds
            font = pygame.font.Font(None, 74)
            text = font.render("GAME OVER", 1, white)
            screen.blit(text, (250,300))
            pygame.display.flip()
            pygame.time.wait(3000)

    # ball collision with the paddle's top
    if ball_y + 10 >= 550 and ball_y + 10 <= 560:
        if ball_x + 10 >= paddle_x:
            if ball_x - 10 < paddle_x + 150:
                if ball_x - 10 >= paddle_x + 100:
                    ball_dx = vel3
                    ball_dy *= -1
                if ball_x - 10 > paddle_x + 50:
                    if ball_x <= paddle_x + 75:
                        ball_dy = -vel3
                        if ball_dx > 0:
                            ball_dx = vel1
                        else:
                            ball_dx = -vel1
                if ball_x - 10 > paddle_x:
                    if ball_x <= paddle_x + 50:
                        ball_dx = -vel3
                        ball_dy = -vel1

    # ball collision with the paddle's side
    if ball_y + 10 > 555:
        if sideimpulse == True:
            if ball_x + 10 >= paddle_x - 10:
                if ball_x - 10 < paddle_x + 160:
                    ball_dx *= -1
                    sideimpulse = False

    screen.blit(paddle, (paddle_x, 560))
    screen.blit(a1, (4, 100))
    screen.blit(a2, (60, 100))
    screen.blit(a3, (112, 100))
    screen.blit(a4, (168, 100))
    screen.blit(a5, (224, 100))
    screen.blit(a6, (284, 100))
    screen.blit(a7, (344, 100))
    screen.blit(a8, (400, 100))
    screen.blit(a9, (456, 100))
    screen.blit(a10, (512, 100))
    screen.blit(ball, (ball_x, ball_y))
    pygame.display.flip()
    
    fps.tick(60)

pygame.quit()