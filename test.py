import pygame

pygame.init()

screen_width = 800
screen_height = 750

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Testing')

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

