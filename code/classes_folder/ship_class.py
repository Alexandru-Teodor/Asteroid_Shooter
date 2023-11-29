import pygame, sys
from global_variables import *
from .laser_class import Laser
from classes_folder.game_over import GameOver


class Ship(pygame.sprite.Sprite):
    def __init__(self, groups):
        # 1. init the parent class
        super().__init__(groups)
        # 2. surface -> image
        self.image = pygame.image.load("graphics/ship.png").convert_alpha()
        # 3. rect
        self.rect = self.image.get_rect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
        # 4. add a mask - need to be called "mask"
        self.mask = pygame.mask.from_surface(self.image)

        self.shoot_time = 0

    def input_position(self):
        pos = pygame.mouse.get_pos()
        self.rect.center = pos

    def can_shoot(self):
        DURATION = 500
        crt_time = pygame.time.get_ticks()
        if crt_time - self.shoot_time >= DURATION:
            self.shoot_time = crt_time
            return True
        return False

    def shoot_laser(self):
        if pygame.mouse.get_pressed()[0] and self.can_shoot():
            Laser(self.rect.midtop, laser_group)
            laser_sound.play()
            pygame.mixer.Sound.set_volume(laser_sound, 0.5)

    def meteor_collision(self, game_over: GameOver):
        # it returns a list with the objects in collision
        if pygame.sprite.spritecollide(
            self, meteor_group, False, pygame.sprite.collide_mask): 
            game_over.end_game = True

    def update(self, game_over: GameOver):
        self.input_position()
        self.shoot_laser()
        self.meteor_collision(game_over)
