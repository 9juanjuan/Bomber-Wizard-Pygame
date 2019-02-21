import pygame
import random
import time

SCREEN_TITLE = 'Catch the Monster'
SCREEN_WIDTH = 512
SCREEN_HEIGHT = 480
SCREEN_COLOR = (97, 159, 182)
clock = pygame.time.Clock()




class Game: 
    def __init__ (self, image_path, title, width, height):
        self.title = title
        self.width = width
        self.height = height
        # Creates a window of specified size 
        self.game_screen = pygame.display.set_mode((width, height))
        # Fills the screen with a blue color 
        self.game_screen.fill (SCREEN_COLOR)
        pygame.display.set_caption(title)

        # load and set the background image 
        background_image =  pygame.image.load('background.png')
        self.image = pygame.transform.scale(background_image, (width, height))



    clock = pygame.time.Clock()
    

    def run_game_loop(self): 
        stop_game = False 
        x_dir = 0
        y_dir = 0 
        monster_x_dir = 3
        monster_y_dir = 3
        monster_moving = 1
        change_dir_countdown = 120
        # Initiates player character in game loop
        player_character = PlayerCharacter('hero.png', 240, 226, 32, 32)
        # Initiates monster in game loop
        monster_0 = Monster('monster.png', 100, 100, 32, 32)

        # Main game loop 
        while not stop_game:

            change_dir_countdown = change_dir_countdown - 1
            for event in pygame.event.get():

                # Event handling
                if event.type == pygame.QUIT:
                    stop_game = True
                # event handler for keypress 
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        y_dir = 3
                    elif event.key == pygame.K_DOWN:
                        y_dir = -3
                    elif event.key == pygame.K_LEFT:
                        x_dir = -3
                    elif event.key == pygame.K_RIGHT:
                        x_dir = 3
                # event handler for key release. Makes Y dir and X dir = 0
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        y_dir = 0
                    elif event.key == pygame.K_DOWN:
                        y_dir = 0
                    elif event.key == pygame.K_LEFT: 
                        x_dir = 0
                    elif event.key == pygame.K_RIGHT:
                        x_dir = 0
            if change_dir_countdown == 0:
                change_dir_countdown = 120
                monster_moving = random.randint(1,4)
        
            
            # Fills screen with SCREEN_COLOR and draws background image over it
            self.game_screen.fill(SCREEN_COLOR)
            self.game_screen.blit(self.image, (0,0))

            # updates player position, still have to write function in Character class for movement 
            player_character.move(x_dir, y_dir) #, max_height, max_width)
            # Draws player at position
            player_character.draw(self.game_screen)

            monster_0.move(monster_x_dir, monster_y_dir, monster_moving)
            monster_0.draw(self.game_screen)

            # move and draw more enemies when reach higher levels 

            # end game if collision detected

            pygame.display.update()
            clock.tick(60)


        # Game logic
        

     

        # Draw background
        # Draw hero
   
        # Game display
        # screen.blit(background_image, (0,0))
        # screen.blit(hero_image,(240,226))
        # screen.blit(monster_image, (monster_x_pos,monster_y_pos))





class GameObject:
    def __init__(self, image_path, x, y, width, height):
        object_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(object_image, (width, height))

        self.x_pos = x
        self.y_pos = y

        self.width = width
        self.height = height

    def draw(self, background):
        background.blit(self.image, (self.x_pos, self.y_pos))

class PlayerCharacter (GameObject): 
    # x_dir = 2
    # y_dir = 2

    def __init__(self, image_path, x, y, width, height):
        super().__init__(image_path, x, y, width, height)

    def move(self, x_dir, y_dir):
        if y_dir == 3:
            self.y_pos -= abs(y_dir)
        elif y_dir == -3:
            self.y_pos += abs(y_dir)
        elif x_dir == 3:
            self.x_pos += abs(x_dir)
        elif x_dir == -3:
            self.x_pos -= abs(x_dir)
    def contain(self, x, y, x_dir, y_dir):
        if x >= 500:
        elif x <= 30:
        elif y <= 30:
        elif y >= 460: 

        

class Monster(GameObject): 
    
    def __init__ (self, image_path, x, y, width, height):
        super().__init__(image_path, x, y, width, height)

        self.monster_x_pos = x
        self.monster_y_pos = y

    def move (self, x_dir, y_dir, move_count):
        if move_count == 1:
            self.monster_x_pos += x_dir
        elif move_count == 2:
            self.monster_x_pos -= x_dir
        elif move_count == 3:
            self.monster_y_pos += y_dir
        elif move_count == 4:
            self.monster_y_pos -= y_dir

        # resets position if monster goes off screen
        if self.monster_x_pos > SCREEN_WIDTH:
            self.monster_x_pos = 0
        elif self.monster_x_pos < -16:
            self.monster_x_pos = SCREEN_WIDTH
        elif self.monster_y_pos > SCREEN_HEIGHT:
            self.monster_y_pos = -16
        elif self.monster_y_pos< -16:
            self.monster_y_pos = SCREEN_HEIGHT
    def draw(self, background):
        background.blit(self.image, (self.monster_x_pos, self.monster_y_pos))



pygame.init()

new_game = Game('background.png', SCREEN_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT)
new_game.run_game_loop()

pygame.quit()
# quit()
