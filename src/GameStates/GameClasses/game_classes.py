import pygame
import json

import color as clr

with open("config_gc.json") as config_json:
    configs = json.load(config_json)

for config in configs:
    WALL_BLOCK_WIDTH = configs["WALL_BLOCK_WIDTH"]
    WALL_BLOCK_LENGTH = configs["WALL_BLOCK_LENGTH"]

    PLAYER_WIDTH = configs["PLAYER_WIDTH"]
    PLAYER_LENGTH = configs["PLAYER_LENGTH"]
    PLAYER_MOVEMENT_SPEED = configs["PLAYER_MOVEMENT_SPEED"]

class WallBlock(pygame.sprite.Sprite):
    def __init__(self, x_map_index, y_map_index, wall_block_width = WALL_BLOCK_WIDTH,
        wall_block_length = WALL_BLOCK_LENGTH, color = clr.WHITE):
        super().__init__()

        self.width = wall_block_width
        self.length = wall_block_length

        self.image = pygame.Surface([self.width, self.length])
        self.image.fill(color)
        self.rect = self.image.get_rect()

        self.rect.x = x_map_index * self.width
        self.rect.y = y_map_index * self.length

class Player(pygame.sprite.Sprite):
    def __init__(self, spawn_x, spawn_y, player_width = PLAYER_WIDTH, 
        player_length = PLAYER_LENGTH, player_movement = PLAYER_MOVEMENT_SPEED color):
        super().__init__()

        self.player_width = player_width
        self.player_length = player_length

        self.image = self.Surface([self.player_width, self.player_length])
        self.image.fill(color)
        self.rect = self.image.get_rect()

        self.rect.x = spawn_x
        self.rect.y = spawn_y

        self.movement_speed = player_movement

    def movement(self, direction):
        if direction == "left":
            self.rect.x -= direction
        elif direction == "right":
            self.rect.x += direction
        elif direction == "up":
            self.rect.y -= direction
        elif direction == "down":
            self.rect.y += direction

    # This is checking if the player has gone off the top or bottom walls.
    # Kinda backwards that the x-axis checks the rect.y. Oh well.
    def x_axis_boundary_check(self):
        # TODO: Change this so that it stops the user before they go off screen to
        # avoid them slingshotting back into the screen.
        if self.rect.y < 0:
            self.rect.y = 0
        # TODO: Change this so that the 600 is replaced by a variable or argument of some sort
        # so that you don't have to come back and change this every time you change
        # the screen resolution.
        elif (self.rect.y + self.player_width) > 600: # 600 is the screen's width.
            self.rect.y = 600 - self.player_width

    # This is checking if the player has gone off the left or right walls.
    # Once again, this is kinda backwards that the y-axis checks the rect.x. Oh well.
    def y_axis_boundary_check(self):
        # TODO: Change this so that it stops the user before they go off screen to
        # avoid them slingshotting back into the screen.
        if self.rect.x < 0:
            self.rect.x = 0
        # TODO: Change this so that the 600 is replaced by a variable or argument of some sort
        # so that you don't have to come back and change this every time you change
        # the screen resolution.
        elif (self.rect.x + self.player_length) > 600: # 600 is the screen's width.
            self.rect.x = 600 - self.player_length

    def update(self):
        self.x_axis_boundary_check()
        self.y_axis_boundary_check()
        