import pygame
from global_variables import WINDOW_HEIGHT
from random import randint, uniform
# from classes_folder.score_class import Score


class Meteor(pygame.sprite.Sprite):
    def __init__(self, position, score, groups) -> None:
        #basic setup
        super().__init__(groups)
        #randomizing the meteor size
        self.scaled_surface = self.scale_meteor()
        self.image = self.scaled_surface
        self.rect = self.image.get_rect(center = position)
        self.mask = pygame.mask.from_surface(self.image)

        # float based position
        self.pos = pygame.math.Vector2(self.rect.topleft)
        self.direction = pygame.math.Vector2(uniform(-0.5, 0.5), 1)

        # update this to a higher speed every 10 points
        self.difficulty = score.current_score // 10 * 100
        self.speed = randint(300 + self.difficulty, 500 + self.difficulty)

        # rotation logic
        self.rotation = 0
        self.rotation_speed = randint(20, 50)

    def rotate(self, dt: float):
        self.rotation += self.rotation_speed * dt
        rotated_surf = pygame.transform.rotozoom(self.scaled_surface, self.rotation, 1)
        self.image = rotated_surf
        self.rect = self.image.get_rect(center = self.rect.center)
        self.mask = pygame.mask.from_surface(self.image)

    def scale_meteor(self):
        meteor_surf = pygame.image.load("graphics/meteor.png").convert_alpha()
        meteor_size = pygame.math.Vector2(meteor_surf.get_size()) * uniform(0.5, 1.5)
        return pygame.transform.scale(meteor_surf, meteor_size)

    def update(self, delta_time: float):
        self.pos += self.direction * self.speed * delta_time
        self.rect.topleft = (round(self.pos.x), round(self.pos.y))
        self.rotate(delta_time)
        if self.rect.top > WINDOW_HEIGHT:
            # meteor_group.remove(self)
            self.kill()
