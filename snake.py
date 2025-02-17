import pygame
import time
import random
pygame.init()

speed = 15

window_x = 1440
window_y = 960

black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

game_window = pygame.display.set_mode(window_x, window_y)
fps = 24

snake_position = [0, 0]
snake_body = [  
    [1, 0]
    [2, 0]
    [3, 0]
    [4, 0] 
]

fruit_position = [random.randrange(1, window_x),
                  random.randrange(1, window_y)]
fruit_spawn = True