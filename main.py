import pygame
from game import Game

# Initialization of the Game
pygame.init()
width = 1500
height = 900
screen = pygame.display.set_mode((width, height)) # Width and Height

# Window Stuff
pygame.display.set_caption('Jeu')

game = Game(screen, width, height)

loop = True
while loop:
    screen.fill((255,225,226))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            loop=False
    game.update()