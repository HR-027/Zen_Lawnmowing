import pygame
import sys
import os
from Zen_Settings import *


class Player(pygame.sprite.Sprite):
    # Creates a player class
    def __init__(self, game, x_pos, y_pos):
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        # Sets the player to the picture of a mower
        self.image = pygame.image.load(Red_Mower).convert_alpha()
        # A copy of the player sprite for rotating player
        self.img_copy = pygame.image.load(Red_Mower).convert_alpha()
        # Rectangle that is the same size as the image
        self.rect = self.image.get_rect()
        # Current position of the player
        self.x = x_pos
        self.y = y_pos
        self.pos = [[x_pos, y_pos]]

    def move(self, dx=0, dy=0):
        # If the position is not blocked then it moves the player
        if not self.blocked(dx, dy):
            self.x += dx
            self.y += dy
            self.pos.append([self.x, self.y])
            print(self.pos)

    def blocked(self, dx=0, dy=0):
        # For each block, if the block co-ord is equal to the player co-ord it returns True, else it return False
        for block in self.game.blocks:
            if block.x == self.x + dx and block.y == self.y + dy:
                return True
        return False

    def cut_grass(self):
        pass

    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE


class Block(pygame.sprite.Sprite):
    def __init__(self, game, x_pos, y_pos):
        self.groups = game.all_sprites, game.blocks
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(ORANGE)
        self.rect = self.image.get_rect()
        self.x = x_pos
        self.y = y_pos
        self.rect.x = x_pos * TILESIZE
        self.rect.y = y_pos * TILESIZE

class Path(pygame.sprite.Sprite):
    def __init__(self, game, x_pos, y_pos):
        self.groups = game.paths, game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.x = x_pos
        self.y = y_pos
        self.rect.x = x_pos * TILESIZE
        self.rect.y = y_pos * TILESIZE

class Mob(pygame.sprite.Sprite):
    def __init__(self, game, x_pos, y_pos):
        self.groups = game.all_sprites, game.mobs
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = pygame.image.load(Mole).convert_alpha()
        self.rect = self.image.get_rect()
        self.x = x_pos
        self.y = y_pos
        self.rect.x = x_pos * TILESIZE
        self.rect.y = y_pos * TILESIZE

