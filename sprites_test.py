# importing the libraries to use
import pygame as pg
# Allowing this sprite file to go into the main file and allowing the Settings file to work in with this file 
from pygame.sprite import Sprite
from setting_test import *
from random import randint 

vec = pg.math.Vector2

# player class
class Player(Sprite):
    def __init__(self, game):
        Sprite.__init__(self)
        # Setting the properties for the player
        self.game = game
        self.image = pg.Surface((50,50))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.cofric = 0.1
        self.canjump = False
        self.standing = False
        self.jumping = False

    # defining what keys are good to use for controlling the user 
    def input(self):
        keystate = pg.key.get_pressed()
        if keystate[pg.K_a]:
            self.acc.x = -PLAYER_ACC
        if keystate[pg.K_d]:
            self.acc.x = PLAYER_ACC
       
    # defining how the player can jump 
    def jump(self):
        self.jumping = True
        self.rect.x += 1
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.x -= 1
        #if hits:
        self.vel.y = -PLAYER_JUMP
        self.jumping = False

    # adding gravity to the user
    def update(self):
        self.acc = vec(0, PLAYER_GRAV)
        self.acc.x = self.vel.x * PLAYER_FRICTION
        self.input()
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.rect.bottomleft = self.pos

        print(self.pos)
        
        # if isinstance(self, MovingPlatform):
        #     self.rect.x += block.change_x
        


# creating a platform class
class Platform(Sprite):
    def __init__(self, x, y, width, height, color, variant):
        Sprite.__init__(self)
        self.width = width
        self.height = height
        self.image = pg.Surface((self.width,self.height))
        self.color = color
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.variant = variant
        
#class MovingPlatform(Sprite):
    def __init__(self, x, y, width, height, color, variant):
        Sprite.__init__(self)
        self.width = width
        self.height = height
        self.image = pg.Surface((self.width,self.height))
        self.color = color
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.variant = variant
    change_x = 0
    change_y = 0 

    boundary_top = 0
    boundary_bottom = 0
    boundary_left = 0
    boundary_right = 0
    
    #player = none

    def update(self):

        #moving left or right
        self.rect.x += self.change_x 

        hit = pg.sprite.collide_rect(self, self.player)
        if hit: 
            if self.change_x < 0:
                self.player.rect.right = self.rect.left
            else:
                self.player.rect.left = self.rect.right
        
        # moving up or down
        self.rect.y += self.change_y

        hits = pg.sprite.collide_rect(self, self.player)
        if hit: 
            if self.change_y < 0:
                self.player.rect.bottom = self.rect.top
            else:
                self.player.rect.top = self.rect.bottom
        
        if self.rect.bottom > self.boundary_bottom or self.rect.top < self.boundary_top:
            self.change_y *= -1
 
        cur_pos = self.rect.x - self.level.world_shift
        if cur_pos < self.boundary_left or cur_pos > self.boundary_right:
            self.change_x *= -1