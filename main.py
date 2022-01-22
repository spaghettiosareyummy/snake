import pygame, sys,random #imports pygame and sys :)
from pygame.math import Vector2 #allows us to just type "Vector2" instead of pygame.math.Vector2()

class FRUIT:
    def __init__(self):
        self.x = random.randint(0,cell_number - 1)
        self.y = random.randint(0,cell_number - 1)
        self.pos = Vector2(self.x, self.y)

    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size),int(self.pos.y * cell_size),cell_size,cell_size)
        pygame.draw.rect(screen,(126,166,114),fruit_rect)

pygame.init() #starts pygame as a whole
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
clock = pygame.time.Clock() #helps us influence the time in pygame

fruit = FRUIT()

while True:
    for event in pygame.event.get(): #checking for every possible event
        if event.type == pygame.QUIT: #checks if you press the X
            pygame.quit #quits the game
            sys.exit() #ends any code that is being run
    screen.fill((175,215,70))
    fruit.draw_fruit()
    pygame.display.update() #displays all of the new info on the display surface
    clock.tick(60) #runs at 60 FPS