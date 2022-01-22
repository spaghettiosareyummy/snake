import pygame, sys #imports pygame and sys :)

class FRUIT:
    def __init__(self):
        self.x = 5
        self.y = 4
        # Create an x and y pos
        # Draw a square in that pos

pygame.init() #starts pygame as a whole
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size)) #Creates a game display with a width of 400 and a height of 500
clock = pygame.time.Clock() #helps us influence the time in pygame

while True:
    for event in pygame.event.get(): #checking for every possible event
        if event.type == pygame.QUIT: #checks if you press the X
            pygame.quit #quits the game
            sys.exit() #ends any code that is being run
    screen.fill((175,215,70))
    pygame.display.update() #displays all of the new info on the display surface
    clock.tick(60) #runs at 60 FPS
