import pygame, sys,random #imports pygame and sys :)
from pygame.math import Vector2 #allows us to just type "Vector2" instead of pygame.math.Vector2()

class StartButton:
    def __init__(self,text,width,height,pos,elevation):
        self.pressed = False
        self.elevation = elevation
        self.dyel = elevation
        self.origin_y = pos[1]

        self.top_rect = pygame.Rect(pos,(width,height))
        self.top_color = '#31373e'

        self.bottom_rect = pygame.Rect(pos,(width,elevation))
        self.bottom_color = '#231f20'

        self.text_surf = game_font.render(text,True,'#FFFFFF')
        self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)
        
        # self.click_sound = pygame.mixer.Sound(r'Sounds\mouse-click.mp3')

    def draw(self):
        self.top_rect.y = self.origin_y - self.dyel
        self.text_rect.center = self.top_rect.center

        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dyel

        pygame.draw.rect(screen,self.bottom_color,self.bottom_rect,border_radius=12)
        pygame.draw.rect(screen,self.top_color,self.top_rect,border_radius = 12)
        screen.blit(self.text_surf,self.text_rect)
        self.click()

    def click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            self.top_color = '#7289da'
            if pygame.mouse.get_pressed()[0]:
                self.dyel = 0
                self.pressed = True
            else:
                self.dyel = self.elevation
                if self.pressed == True:
                    self.pressed = False
                    main_play()
        else:
            self.dyel = self.elevation
            self.top_color = '#31373e'

class CredButton:
    def __init__(self,text,width,height,pos,elevation):
        self.pressed = False
        self.elevation = elevation
        self.dyel = elevation
        self.origin_y = pos[1]

        self.top_rect = pygame.Rect(pos,(width,height))
        self.top_color = '#31373e'

        self.bottom_rect = pygame.Rect(pos,(width,elevation))
        self.bottom_color = '#231f20'

        self.text_surf = game_font.render(text,True,'#FFFFFF')
        self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)
        
        # self.click_sound = pygame.mixer.Sound(r'Sounds\mouse-click.mp3')

    def draw(self):
        self.top_rect.y = self.origin_y - self.dyel
        self.text_rect.center = self.top_rect.center

        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dyel

        pygame.draw.rect(screen,self.bottom_color,self.bottom_rect,border_radius=12)
        pygame.draw.rect(screen,self.top_color,self.top_rect,border_radius = 12)
        screen.blit(self.text_surf,self.text_rect)
        self.click()

    def click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            self.top_color = '#7289da'
            if pygame.mouse.get_pressed()[0]:
                self.dyel = 0
                self.pressed = True
            else:
                self.dyel = self.elevation
                if self.pressed == True:
                    self.pressed = False
                    cred_menu()
        else:
            self.dyel = self.elevation
            self.top_color = '#31373e'

class OptButton:
    def __init__(self,text,width,height,pos,elevation):
        self.pressed = False
        self.elevation = elevation
        self.dyel = elevation
        self.origin_y = pos[1]

        self.top_rect = pygame.Rect(pos,(width,height))
        self.top_color = '#31373e'

        self.bottom_rect = pygame.Rect(pos,(width,elevation))
        self.bottom_color = '#231f20'

        self.text_surf = game_font.render(text,True,'#FFFFFF')
        self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)
        
        # self.click_sound = pygame.mixer.Sound(r'Sounds\mouse-click.mp3')

    def draw(self):
        self.top_rect.y = self.origin_y - self.dyel
        self.text_rect.center = self.top_rect.center

        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dyel

        pygame.draw.rect(screen,self.bottom_color,self.bottom_rect,border_radius=12)
        pygame.draw.rect(screen,self.top_color,self.top_rect,border_radius = 12)
        screen.blit(self.text_surf,self.text_rect)
        self.click()

    def click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            self.top_color = '#7289da'
            if pygame.mouse.get_pressed()[0]:
                self.dyel = 0
                self.pressed = True
            else:
                self.dyel = self.elevation
                if self.pressed == True:
                    # self.nothing.play()
                    self.pressed = False
                    opt_menu()
        else:
            self.dyel = self.elevation
            self.top_color = '#31373e'

class BackButton:
    def __init__(self,text,width,height,pos,elevation):
        self.pressed = False
        self.elevation = elevation
        self.dyel = elevation
        self.origin_y = pos[1]

        self.top_rect = pygame.Rect(pos,(width,height))
        self.top_color = '#31373e'

        self.bottom_rect = pygame.Rect(pos,(width,elevation))
        self.bottom_color = '#231f20'

        self.text_surf = game_font.render(text,True,'#FFFFFF')
        self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)
        
        # self.click_sound = pygame.mixer.Sound(r'Sounds\mouse-click.mp3')

    def draw(self):
        self.top_rect.y = self.origin_y - self.dyel
        self.text_rect.center = self.top_rect.center

        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dyel

        pygame.draw.rect(screen,self.bottom_color,self.bottom_rect,border_radius=12)
        pygame.draw.rect(screen,self.top_color,self.top_rect,border_radius = 12)
        screen.blit(self.text_surf,self.text_rect)
        self.click()

    def click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            self.top_color = '#7289da'
            if pygame.mouse.get_pressed()[0]:
                self.dyel = 0
                self.pressed = True
            else:
                self.dyel = self.elevation
                if self.pressed == True:
                    # self.nothing.play()
                    self.pressed = False
                    start_menu()
        else:
            self.dyel = self.elevation
            self.top_color = '#31373e'

class ResetButton:
    def __init__(self,text,width,height,pos,elevation):
        self.pressed = False
        self.elevation = elevation
        self.dyel = elevation
        self.origin_y = pos[1]

        self.top_rect = pygame.Rect(pos,(width,height))
        self.top_color = '#31373e'

        self.bottom_rect = pygame.Rect(pos,(width,elevation))
        self.bottom_color = '#231f20'

        self.text_surf = game_font.render(text,True,'#FFFFFF')
        self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)
        self.snake = SNAKE()
        
        # self.click_sound = pygame.mixer.Sound(r'Sounds\mouse-click.mp3')

    def draw(self):
        self.top_rect.y = self.origin_y - self.dyel
        self.text_rect.center = self.top_rect.center

        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dyel

        pygame.draw.rect(screen,self.bottom_color,self.bottom_rect,border_radius=12)
        pygame.draw.rect(screen,self.top_color,self.top_rect,border_radius = 12)
        screen.blit(self.text_surf,self.text_rect)
        self.click()

    def click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            self.top_color = '#7289da'
            if pygame.mouse.get_pressed()[0]:
                self.dyel = 0
                self.pressed = True
            else:
                self.dyel = self.elevation
                if self.pressed == True:
                    # self.nothing.play()
                    self.pressed = False
                    main_play()
                    self.snake.reset()
        else:
            self.dyel = self.elevation
            self.top_color = '#31373e'

class SNAKE:
    def __init__(self):
        self.body = [Vector2(5,10),Vector2(4,0),Vector2(3,10)]
        self.direction = Vector2(0,0)
        self.new_block = False

        self.head_up = pygame.image.load('Graphics/head_up.png').convert_alpha()
        self.head_down = pygame.image.load('Graphics/head_down.png').convert_alpha()
        self.head_right = pygame.image.load('Graphics/head_right.png').convert_alpha()
        self.head_left = pygame.image.load('Graphics/head_left.png').convert_alpha()
        
        self.tail_up = pygame.image.load('Graphics/tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load('Graphics/tail_down.png').convert_alpha()
        self.tail_right = pygame.image.load('Graphics/tail_right.png').convert_alpha()
        self.tail_left = pygame.image.load('Graphics/tail_left.png').convert_alpha()

        self.body_vertical = pygame.image.load('Graphics/body_vertical.png').convert_alpha()
        self.body_horizontal = pygame.image.load('Graphics/body_horizontal.png').convert_alpha()

        self.body_tr = pygame.image.load('Graphics/body_tr.png').convert_alpha()
        self.body_tl = pygame.image.load('Graphics/body_tl.png').convert_alpha()
        self.body_br = pygame.image.load('Graphics/body_br.png').convert_alpha()
        self.body_bl = pygame.image.load('Graphics/body_bl.png').convert_alpha()
        self.crunch_sound = pygame.mixer.Sound(r'Sounds\sound_crunch.wav')



    def draw_snake(self):

        for index,block in enumerate(self.body):
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos,y_pos,cell_size,cell_size)

            if index == 0:
                head_dir = self.body[1] - self.body[0]
                if head_dir == Vector2(1,0): 
                    self.head = self.head_left
                    screen.blit(self.head,block_rect)
                elif head_dir == Vector2(-1,0): 
                    self.head = self.head_right
                    screen.blit(self.head,block_rect)
                elif head_dir == Vector2(0,1): 
                    self.head = self.head_up
                    screen.blit(self.head,block_rect)
                elif head_dir == Vector2(0,-1): 
                    self.head = self.head_down
                    screen.blit(self.head,block_rect)
            elif index == len(self.body) - 1:
                tail_relation = self.body[-2] - self.body[-1]
                if tail_relation == Vector2(1,0):
                    self.tail = self.tail_left
                    screen.blit(self.tail,block_rect)
                elif tail_relation == Vector2(-1,0):
                    self.tail = self.tail_right
                    screen.blit(self.tail,block_rect)
                elif tail_relation == Vector2(0,1):
                    self.tail = self.tail_up
                    screen.blit(self.tail,block_rect)
                elif tail_relation == Vector2(0,-1):
                    self.tail = self.tail_down
                    screen.blit(self.tail,block_rect)
            else:
                previous_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block
                if previous_block.x == next_block.x:
                    screen.blit(self.body_vertical,block_rect)
                elif previous_block.y == next_block.y:
                    screen.blit(self.body_horizontal,block_rect)
                else:
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                        screen.blit(self.body_tl,block_rect)
                    elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                        screen.blit(self.body_bl,block_rect)
                    elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                        screen.blit(self.body_tr,block_rect)
                    elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                        screen.blit(self.body_br,block_rect)


    def move_snake(self):
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0,body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0,body_copy[0] + self.direction)
            self.body = body_copy[:]

    def add_block(self):
        self.new_block = True

    def play_crunch(self):
        self.crunch_sound.play()

    def reset(self):
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.direction = Vector2(0,0)
    # def escreset(self):
    #     self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
    #     self.direction = Vector2(0,0)
        

class FRUIT:
    def __init__(self):
        self.randomize()
        self.x = random.randint(0,cell_number - 1)
        self.y = random.randint(0,cell_number - 1)
        self.pos = Vector2(self.x, self.y)

    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size),int(self.pos.y * cell_size),cell_size,cell_size)
        screen.blit(apple,fruit_rect)
        # pygame.draw.rect(screen,(126,166,114),fruit_rect)

    def randomize(self):
        self.x = random.randint(0,cell_number - 1)
        self.y = random.randint(0,cell_number - 1)
        self.pos = Vector2(self.x, self.y)

class SCORE:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()
        score_text = str(len(self.snake.body) - 3)
        score_surface = game_font.render(score_text,True,(56,74,12))
        score_x = int(cell_size * cell_number - 60)
        score_y = int(cell_size * cell_number - 40)
        score_rect = score_surface.get_rect(center = (score_x,score_y))
        apple_rect = apple.get_rect(midright = (score_rect.left,score_rect.centery))
        self.bg_rect = pygame.Rect(apple_rect.left,apple_rect.top,apple_rect.width + score_rect.width + 6,apple_rect.height)

        pygame.draw.rect(screen,(167,209,61),self.bg_rect)
        screen.blit(score_surface,score_rect)
        screen.blit(apple,apple_rect)
        pygame.draw.rect(screen,(56,74,12),self.bg_rect,2)

class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()
        self.score = SCORE()

    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_death()

    def draw_elements(self):
        self.draw_grass()
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.draw_score()

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_block()
            self.snake.play_crunch()
        for block in self.snake.body[1:]:
            if block == self.fruit.pos:
                self.fruit.randomize()
        for block in self.score.bg_rect:
            if block == self.fruit.pos:
                self.fruit.randomize()

    def check_death(self):
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()

        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        self.snake.reset()

    def draw_grass(self):
        grass_color = (167,209,61)
        for row in range(cell_number):
            if row % 2 == 0:
                for col in range(cell_number):
                    if col % 2 == 0:
                        grass_rect = pygame.Rect(col * cell_size,row * cell_size,cell_size,cell_size)
                        pygame.draw.rect(screen,grass_color,grass_rect)
            else:
                for col in range(cell_number):
                    if col % 2 != 0:
                        grass_rect = pygame.Rect(col * cell_size,row * cell_size,cell_size,cell_size)
                        pygame.draw.rect(screen,grass_color,grass_rect)

    def draw_score(self):
        score_text = str(len(self.snake.body) - 3)
        score_surface = game_font.render(score_text,True,(56,74,12))
        score_x = int(cell_size * cell_number - 60)
        score_y = int(cell_size * cell_number - 40)
        score_rect = score_surface.get_rect(center = (score_x,score_y))
        apple_rect = apple.get_rect(midright = (score_rect.left,score_rect.centery))
        bg_rect = pygame.Rect(apple_rect.left,apple_rect.top,apple_rect.width + score_rect.width + 6,apple_rect.height)

        pygame.draw.rect(screen,(167,209,61),bg_rect)
        screen.blit(score_surface,score_rect)
        screen.blit(apple,apple_rect)
        pygame.draw.rect(screen,(56,74,12),bg_rect,2)

pygame.mixer.pre_init(44100,-16,2,512)
pygame.init() #starts pygame as a whole
cell_size = 40
cell_number = 15
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
mainClock = pygame.time.Clock() #helps me influence the time in pygame
startClock = pygame.time.Clock()
credClock = pygame.time.Clock()
escClock = pygame.time.Clock()
apple = pygame.image.load(r'Graphics\apple.png').convert_alpha()
game_font = pygame.font.Font(r'Fonts\PoetsenOne-Regular.ttf',25)
back_arrow = pygame.image.load(r'Graphics\OIP.jfif')
esc_font = pygame.font.Font(r'Fonts\PoetsenOne-Regular.ttf',15)

buttonstart = StartButton('Start Game',200,40,(200,200),6)
buttonop = OptButton('Options', 200, 40, (200,250),6)
buttoncred = CredButton('Credits',200,40,(200,300),6)
buttonback = BackButton('Return to Menu',200,40,(20,550),6)
buttonbackesc = BackButton('Return to Menu',200,40,(195,300),6)
buttonreset = ResetButton('Reset',200,40,(195,350),6)


SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150)

main_game = MAIN()

def start_menu():
    while True:

        screen.fill((175,215,70))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit
                sys.exit()

        buttonstart.draw()
        buttonop.draw()
        buttoncred.draw()

        pygame.display.update()
        startClock.tick(60)
        
def cred_menu():
    while True:
        screen.fill((175,215,70))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit
                sys.exit()
        text = game_font.render('Made by spaghetti =)',True,'#FFFFFF')
        screen.blit(text, (300,400))

        buttonback.draw()

        pygame.display.update()
        credClock.tick(60)

def opt_menu():
    while True:
        screen.fill((175,215,70))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit
                sys.exit()
        text = game_font.render('Trolled e.e',True,'#FFFFFF')
        screen.blit(text, (177,200))

        buttonback.draw()

        pygame.display.update()
        credClock.tick(60)

def esc_menu():
    while True:
        screen.fill((175,215,70))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main_play()
        
        buttonbackesc.draw()
        buttonreset.draw()
        
        pygame.display.update()
        escClock.tick(60)
        



def main_play():
    while True:
        tutorial = True
        for event in pygame.event.get(): #checking for every possible event
            if event.type == pygame.QUIT: #checks if you press the X
                pygame.quit #quits the game
                sys.exit() #ends any code that is being run
            if event.type == SCREEN_UPDATE:
                main_game.update()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    tutorial = False
                    if main_game.snake.direction.y != 1:
                        main_game.snake.direction = Vector2(0,-1)
                if event.key == pygame.K_DOWN:
                    tutorial = False
                    if main_game.snake.direction.y != -1:
                        main_game.snake.direction = Vector2(0,1)
                if event.key == pygame.K_LEFT:
                    tutorial = False
                    if main_game.snake.direction.x != 1:
                        main_game.snake.direction = Vector2(-1,0)
                if event.key == pygame.K_RIGHT:
                    tutorial = False
                    if main_game.snake.direction.x != -1:
                        main_game.snake.direction = Vector2(1,0)
                if event.key == pygame.K_ESCAPE:
                    esc_menu()

        screen.fill((175,215,70))
        main_game.draw_elements()
        pygame.display.update() #displays all of the new info on the display surface
        mainClock.tick(60) #runs at 60 FPS

esc_menu()
