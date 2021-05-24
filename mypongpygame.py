import pygame
from pygame.locals import *

pygame.init()

screen_width = 800
screen_heigh = 600

screen = pygame.display.set_mode ((screen_width, screen_heigh))
pygame.display.set_caption('Breakout SI')

#colors
bg = (000, 000, 000)
blockH = (253, 108, 158)
blockM = (235, 99, 107)
blockL = (204, 169, 221)

#define variables
columns = 10
rows = 3

#brick wall class
class wall():
    def __init__(self):
        self.width = screen_width // columns
        self.height = 60
    
    def create_wall(self):
        self.blocks= []
        #define an empty list for an individual block
        block_individual = []
        for row in range(rows):
            #reset the block row list:
            block_row = []
            #iterate through each colum in that row
            for col in range(columns):
                #generate x and y positions for each block and create a rectangle from that
                block_x = col + self.width
                block_y = row + self.height
                rect = pygame.Rect(block_x, block_y, self.width, self.height)
                #assign block strength based on row
                if row < 2:
                    strength = 3
                elif row < 4:
                    strength = 2
                elif row < 6:
                    strength = 1
                #create a list at this point to store the rect and colour data
                block_individual = [rect, strength]
                #append that individual block to the block row
                block_row.append(block_individual)
            #append the row to the full list of blocks
            self.blocks.append(block_row)

    def draw_wall(self):
        for row in self.blocks:
            for block in row:
                #assing a colour based on strength
                if block[1] == 3:
                    block_col = blockL
                elif block[1] == 2:
                    block_col = blockM
                elif block[1] == 1:
                    block_col = blockH
                pygame.draw.rect(screen, block_col, block[0])
                pygame.draw.rect(screen, bg, (block[0]))

#create a wall
wall = wall()
wall.create_wall()

fps = pygame.time.Clock()

run = True
while run:

    screen.fill(bg)

    #draw wall
    wall.draw_wall()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    fps.tick(60)
    

pygame.quit()