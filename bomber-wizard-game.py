import pygame 

WHITE_COLOR = (255,255,255)
SCREEN_TITLE = 'Bomber Wizard'
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800 

clock = pygame.time.Clock
pygame.font.init()
font = pygame.font.SysFont ('comicsans', 50)


class Game:

    TICK_RATE = 60
    # Initializes game class title, width height
    def __init__(self, image_path, title, width, height):
        self.title= title
        self.width= width
        self.height= height

        # Creates a window of a certain size and fills in with white color
        self.game_screen = pygame.display.set_mode((width, height))
        self.game_screen.fill(WHITE_COLOR)
        pygame.display.set_caption(title)
        # Loads an image to fill in color, will be tiles 
        background_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(background_image, (width, height))







class GameObject:

    def __init__(self, image_path,  x, y, width,  height):

        object_image= pygame.image.load(image_path)
        self.image = pygame.transform.scale(object_image, (width,height))

        self.x_pos = x
        self.y_pos = y 
        self.width = width
        self.height= height

    #Draw the object by blitting in onto the background (the game screen
    # in this case)
    def draw(self, background):
        background.blit(self.image, (self.x_pos, self.y_pos))

class PlayerCharacter(GameObject):
    pass

class Block(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([20, 20])
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()

        self.rect.center = pos
