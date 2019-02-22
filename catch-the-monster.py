import pygame
import random
import time


#Initializers

SCREEN_TITLE = 'Catch the Monster'
SCREEN_WIDTH = 512
SCREEN_HEIGHT = 480
SCREEN_COLOR = (97, 159, 182)
TEXT_COLOR = (0,0,0)
clock = pygame.time.Clock()
pygame.mixer.init()
win = pygame.mixer.Sound('win.wav')
lose = pygame.mixer.Sound('lose.wav')
music = pygame.mixer.Sound('music.wav')

pygame.font.init()
font = pygame.font.SysFont('comicsans', 35)





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
    

    def run_game_loop(self, level_count): 
        did_win = False
        stop_game = False 
        x_dir = 0
        y_dir = 0 
        monster_x_dir = 3
        monster_y_dir = 3
        monster_moving = 1
        goblin_x_dir = 1.5
        goblin_y_dir = 1.5
        goblin_moving = 1
        change_dir_countdown = 120
        music.play(-1)
        immunity_countdown = 60




        # Initiates player character in game loop
        player_character = PlayerCharacter('hero.png', 240, 226, 32, 32)
        # Initiates monsters in game loop
        monster_0 = Monster('monster.png', random.randint(50, 440), random.randint(50,440), 32, 32)
        goblin_0 = Goblin('goblin.png', random.randint(50, 440), random.randint(50,440), 32, 32) 
        goblin_1 = Goblin('goblin.png', random.randint(50, 440), random.randint(50,440), 32, 32)
        goblin_2 = Goblin('goblin.png', random.randint(50, 440), random.randint(50,440), 32, 32) 
        goblin_3 = Goblin('goblin.png', random.randint(50, 440), random.randint(50,440), 32, 32) 
        goblin_4 = Goblin('goblin.png', random.randint(50, 440), random.randint(50,440), 32, 32)



        # Main game loop 
        while not stop_game:
            immunity_countdown = immunity_countdown - 1     
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
                    elif event.key == pygame.K_UP and event.key == pygame.K_RIGHT:
                        y_dir = 3
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
            # count down that gives random integer, move function takes in random integer
            if change_dir_countdown == 0:
                change_dir_countdown = 120
                monster_moving = random.randint(1,8)
                goblin_moving = random.randint(1,8)
        
            
            # Fills screen with SCREEN_COLOR and draws background image over it
            self.game_screen.fill(SCREEN_COLOR)
            self.game_screen.blit(self.image, (0,0))
            # Keeps track of levels on top left corner on screen
            level= font.render('Level: %d' % level_count, True, TEXT_COLOR )
            self.game_screen.blit(level, (30, 30))

            # updates player position, still have to write function in Character class for movement 
            player_character.move(x_dir, y_dir) #, max_height, max_width)
            # Draws player at position
            if player_character.dead == False:
                player_character.draw(self.game_screen)
            # moves monster, changing direction based on number generator
            monster_0.move(monster_x_dir, monster_y_dir, monster_moving)
            #draws monster at given position
            if monster_0.dead == False:
                monster_0.draw(self.game_screen)
            
            goblin_0.move(goblin_x_dir, goblin_y_dir, goblin_moving)
            goblin_0.draw(self.game_screen)
            goblin_1.move(goblin_x_dir, goblin_y_dir, goblin_moving)
            goblin_1.draw(self.game_screen)
            goblin_2.move(goblin_x_dir, goblin_y_dir, goblin_moving)
            goblin_2.draw(self.game_screen)


            # move and draw more enemies when reach higher levels 

            if level_count == 2 :
                goblin_3.move(goblin_x_dir, goblin_y_dir, goblin_moving)
                goblin_3.draw(self.game_screen)
            if level_count == 3 :
                goblin_3.move(goblin_x_dir, goblin_y_dir, goblin_moving)
                goblin_3.draw(self.game_screen)
                goblin_4.move(goblin_x_dir, goblin_y_dir, goblin_moving)
                goblin_4.draw(self.game_screen)
            

            # Player collides with monster 
            if  immunity_countdown < 0 and player_character.detect_collision(monster_0) :
                # stop_game = True
                monster_0.dead = True 
                music.stop()
                while monster_0.dead == True :
                    win.play()
                    break
                # win.play()
                text = font.render('You win! Press ENTER to play again!', True, TEXT_COLOR )
                self.game_screen.blit(text, (43, 200))
                # pygame.display.update()
                clock.tick(1)
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            print('restart game')
                            new_game.run_game_loop(level_count+1)
                    break
           # Goblin collides with player                                 
            elif goblin_0.detect_collision(player_character) and immunity_countdown < 0 or goblin_1.detect_collision(player_character) and immunity_countdown < 0 or goblin_2.detect_collision(player_character) and immunity_countdown < 0 or goblin_3.detect_collision(player_character) and immunity_countdown < 0 or goblin_4.detect_collision(player_character) and immunity_countdown < 0:
                # stop_game = True
                # did_win = False 
                player_character.dead = True
                music.stop()
                while player_character.dead ==True:
                    lose.play()
                    text = font.render('You lose! Press ENTER to play again!', True, TEXT_COLOR)
                    self.game_screen.blit(text, (43, 200))
                # pygame.display.update()
                    clock.tick(1)
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_RETURN:
                               print('restart game')
                               new_game.run_game_loop(1)
                    break
                # lose.play()
                
                # break

            pygame.display.update()
            clock.tick(60)
        
        if did_win:
            self.run_game_loop(level_count + 1)
        else:
            return






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
    dead = False
    def __init__(self, image_path, x, y, width, height):
        super().__init__(image_path, x, y, width, height)

    def move(self, x_dir, y_dir):
        if y_dir == 3:
            self.y_pos -= abs(y_dir)
        elif y_dir == -3:
            self.y_pos += abs(y_dir)
        if x_dir == 3:
            self.x_pos += abs(x_dir)
        elif x_dir == -3:
            self.x_pos -= abs(x_dir)
        # blocks player movement from going past bushes in  background
        if self.x_pos >= 450:
            self.x_pos = 450
        elif self.x_pos <= 30:
            self.x_pos = 30
        elif self.y_pos <= 30:
            self.y_pos = 30
        elif self.y_pos >= 420:
            self.y_pos = 420

    def detect_collision(self, other_body):
        if self.y_pos > other_body.monster_y_pos + other_body.height:
            return False
        elif self.y_pos + self.height < other_body.monster_y_pos:
            return False
        
        if self.x_pos > other_body.monster_x_pos + other_body.width:
            return False
        elif self.x_pos + self.width < other_body.monster_x_pos:
            return False
        
        return True

        

class Monster(GameObject): 
    dead = False 

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
        elif move_count == 5:
            self.monster_x_pos += x_dir
            self.monster_y_pos += y_dir
        elif move_count == 6:
            self.monster_x_pos += x_dir
            self.monster_y_pos -= y_dir
        elif move_count == 7:
            self.monster_x_pos -= x_dir
            self.monster_y_pos += y_dir
        elif move_count == 8:
            self.monster_x_pos -= x_dir
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

class Goblin(Monster):
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
        elif move_count == 5:
            self.monster_x_pos += x_dir
            self.monster_y_pos += y_dir
        elif move_count == 6:
            self.monster_x_pos += x_dir
            self.monster_y_pos -= y_dir
        elif move_count == 7:
            self.monster_x_pos -= x_dir
            self.monster_y_pos += y_dir
        elif move_count == 8:
            self.monster_x_pos -= x_dir
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

    def detect_collision(self, other_body):
        if self.monster_y_pos > other_body.y_pos + other_body.height:
            return False
        elif self.monster_y_pos + self.height < other_body.y_pos:
            return False
        
        if self.monster_x_pos > other_body.x_pos + other_body.width:
            return False
        elif self.monster_x_pos + self.width < other_body.x_pos:
            return False

        return True
    def draw(self, background):
        background.blit(self.image, (self.monster_x_pos, self.monster_y_pos))


pygame.init()

new_game = Game('background.png', SCREEN_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT)
new_game.run_game_loop(1)

pygame.quit()
quit()
