# By Connor Counts

"""
Game structure:
GOALS; RULES; FEEDBACK; FREEDOM

My goal is:
For this final project, I want to make a mario like game where the user has to jump on the platforms to reach a goal.
I am using the color changing platforms for this game too, and I want to make it so if the user falls off of a platform on to the ground, the game restarts. 
I also want to make a counter for checking that the player hits each platform on the way up to the top. 
I am still working on what layout I want for my games platforms. 

sources:
https://api.arcade.academy/en/stable/examples/platform_tutorial/index.html 
https://api.arcade.academy/en/stable/examples/platform_tutorial/step_02.html 
http://programarcadegames.com/index.php?chapter=example_code_platformer 
http://programarcadegames.com/python_examples/show_file.php?file=platform_jumper.py 
https://www.youtube.com/watch?v=Ongc4EVqRjo&list=PLjcN1EyupaQnHM1I9SmiXfbT6aG4ezUvu&ab_channel=CodingWithRuss 
"""

# import libraries
import pygame as pg
import os
# allowing the  Setting and Sprites files to be used
from settings import *
from sprites import *
# from pg.sprite import Sprite
from random import randint


# set up assets folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")

# create game class in order to pass properties to the sprite file
class Game: 
    def __init__(self):
        # init game window etc.
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("Final game")
        self.clock = pg.time.Clock()
        self.running = True
        print(self.screen)
    
    # starting a new game
    def new(self):

        # setting up classes to self.__ to be used easier in the code
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.enemies = pg.sprite.Group()
        self.player = Player(self)

            #self.plat1 = Platform(WIDTH, 50, 0, HEIGHT-50, (50,50,50), "normal")
            #self.all_sprites.add(self.plat1)
            #self.platforms.add(self.plat1)

        #adding the platforms to the game 
        self.all_sprites.add(self.player)
        for plat in PLATFORM_LIST:
            p = Platform(*plat)
            self.all_sprites.add(p)
            self.platforms.add(p)
        
        self.run()

    # while the game is going on events, update, and draw are running too
    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()


    # When the user quits the game, the game will sop running and when the user clicks the space bar, the player will jump
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.player.jump()


    def update(self):
        self.all_sprites.update()

        # if the player is falling
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)

            # checking to see if the player has collided with a platform
            # if the player hits a platform, the color of the platform will change to red
            if hits:
                self.player.standing = True
                if hits[0].variant == "normal":
                    self.player.pos.y = hits[0].rect.top
                    self.player.vel.y = 0
                    print ("landed!!!!")
                    #do a variable for RED 
                    hits[0].image.fill(RED)

                elif hits[0].variant == "plat_1":
                    self.player.pos.y = hits[0].rect.top
                    self.player.vel.y = 0
                    hits[0].image.fill(BLACK)
                elif hits[0].variant == "plat_2":
                    self.player.pos.y = hits[0].rect.top
                    self.player.vel.y = 0
                    hits[0].image.fill(RED)
                elif hits[0].variant == "plat_3":
                    self.player.pos.y = hits[0].rect.top
                    self.player.vel.y = 0
                    hits[0].image.fill(BLUE)
                elif hits[0].variant == "plat_4":
                    self.player.pos.y = hits[0].rect.top
                    self.player.vel.y = 0
                    hits[0].image.fill(WHITE)
                elif hits[0].variant == "plat_5":
                    self.player.pos.y = hits[0].rect.top
                    self.player.vel.y = 0
                    hits[0].image.fill(BLACK)
                elif hits[0].variant == "plat_6":
                    self.player.pos.y = hits[0].rect.top
                    self.player.vel.y = 0
                    hits[0].image.fill(RED)
                elif hits[0].variant == "plat_7":
                    self.player.pos.y = hits[0].rect.top
                    self.player.vel.y = 0
                    hits[0].image.fill(BLUE)
                elif hits[0].variant == "plat_8":
                    self.player.pos.y = hits[0].rect.top
                    self.player.vel.y = 0
                    hits[0].image.fill(WHITE)
                elif hits[0].variant == "plat_9":
                    self.player.pos.y = hits[0].rect.top
                    self.player.vel.y = 0
                    hits[0].image.fill(BLACK)
                elif hits[0].variant == "plat_10":
                    self.player.pos.y = hits[0].rect.top
                    self.player.vel.y = 0
                    hits[0].image.fill(RED)
                elif hits[0].variant == "plat_11":
                    self.player.pos.y = hits[0].rect.top
                    self.player.vel.y = 0
                    hits[0].image.fill(BLUE)
                    #draw_text("Level Complete", 22, WHITE, WIDTH/500, HEIGHT/700)
                    #draw_text("Level Complete",font, (0,0,0), 220, 150)
            else:
                # if the player is not on a platform, the platform will go back to white
                self.player.standing = False
                    #self.platforms[0].image.fill(WHITE)
                for platform in self.platforms:
                    platform.image.fill(WHITE)

        

    # Making the screen blue
    def draw (self):
        self.screen.fill(BLUE)
        self.all_sprites.draw(self.screen)
        pg.display.flip()

    # Making paramaters for allowing text to be drawn on the screen
    def draw_text(self, text, size, color, x, y):
        font_name = pg.font.match_font('arial')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        self.screen.blit(text_surface, text_rect)   

    def get_mouse_now(self):
        x,y = pg.mouse.get_pos()
        return (x,y)
 
# instantiate the game class
g = Game()

# kick off the game loop
while g.running:
    g.new()

pg.quit()