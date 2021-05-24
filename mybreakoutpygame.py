import pygame
pygame.init()

# Making new window
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Breakout - PyGame Edition - 2021.05.21")

#defining bricks
rows = 4
columns = 15
bricks_height = 25 
bricks_width = 50
bricks = []

def brickwall ():
    for j in range (rows):
        for k in range (columns):
            x = (bricks_width * k * 1.08)
            y = 100 + (bricks_height * j * 1.16)
            eachbrick = pygame.Rect(x, y, bricks_width, bricks_height)
            bricks.append(eachbrick)

brickwall()

# Defining colors used in the game 

white = (255, 255, 255)
red = (255, 000, 000)
black = (0, 0, 0)
blue = (20, 100, 200)
orange = (200, 150, 70)

score = 0
lives = 2

#Creating Paddle

paddle_x = 325
paddle = pygame.Rect(paddle_x, 550, 150, 30)
paddle_right = False
paddle_left = False

#life variable
alive = True

# ball
ball_x = 400
ball_y = 300
ball = pygame.Rect(ball_x, ball_y, 20, 20)
sideimpulse = True

vel1 = 4
vel2 = 8
vel3 = 10

ball_dx = -vel1
ball_dy = -vel1

# Variable for the following while loop
game_loop = True
fps = pygame.time.Clock()

while game_loop:
    if not bricks:
        brickwall()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False
        
        #  keystroke events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                if not alive:
                    bricks = []
                    alive = True
                    lives = 2
                    score = 0
                    ball_dy = vel1
                    ball_dx = vel1
            if event.key == pygame.K_RIGHT:
                paddle_right = True
            if event.key == pygame.K_LEFT:
                paddle_left = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                paddle_right = False
            if event.key == pygame.K_LEFT:
                paddle_left = False

    if alive:
        ball = pygame.Rect(ball_x, ball_y, 13, 13)
        paddle = pygame.Rect(paddle_x, 550, 150, 30 )

        #ball movement
        ball_x = ball_x + ball_dx
        ball_y = ball_y + ball_dy

        # paddle right movement
        if paddle_right:
            if paddle_x <= 750:
                paddle_x += 10
        else:
            paddle_x += 0

        # paddle 1 left movement
        if paddle_left:
            if paddle_x >= -100:
                paddle_x -= 10
        else:
            paddle_x += 0
        screen.fill(black)
        pygame.draw.line(screen, white, [0, 38],
                        [800, 38], 2)

        #Score and Number of lives at the bottom of screen
        font = pygame.font.Font(None, 34)
        text = font.render("Score: " + str(score), 1, white)
        screen.blit(text, (20,10))
        text = font.render("Lives: " + str(lives), 1, white)
        screen.blit(text, (650, 10))

    else: 
        font = pygame.font.Font(None, 34)
        text = font.render("GAME OVER" , 1, white)
        screen.blit(text, (340,300))
        text = font.render("Score: " + str(score), 1, white)
        screen.blit(text, (350,334))
        text = font.render("Press Backspace to restart", 1, white)
        screen.blit(text, (270,360))

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
        ball_y = 300
        ball_x = 300
        lives -= 1
        ball_dy = vel1
        ball_dx = vel1
        if lives <= 0:
            alive = False

    # ball collision with the paddle's top
    if ball.colliderect(paddle):
        ball_y = 530
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

    for block in bricks:
        if ball.colliderect(block):
            bricks.remove(block)
            ball_dy *= -1
            score += 20

    # Bricks
    for block in bricks:
        # Draw Bricks
        pygame.draw.rect(screen, orange, block)
        


    pygame.draw.rect(screen, blue, paddle)
    pygame.draw.rect(screen, red, ball)

    pygame.display.flip()
    
    fps.tick(60)

pygame.quit()