import pygame
from global_variables import meteor_group, explosion_sound
from classes_folder.score_class import Score


class Laser(pygame.sprite.Sprite):
    def __init__(self, position, groups) -> None:
        super().__init__(groups)
        self.image = pygame.image.load("graphics/laser.png").convert_alpha()
        self.rect = self.image.get_rect(midbottom = position)
        self.mask = pygame.mask.from_surface(self.image)

        # float based position
        self.pos = pygame.math.Vector2(self.rect.topleft)
        self.direction = pygame.math.Vector2(0, -1)
        self.speed = 500
    
    def meteor_collision(self, score: Score):
        if pygame.sprite.spritecollide(
            self, meteor_group, True, pygame.sprite.collide_mask):
            # pygame.sprite.Sprite.remove(self, laser_group)
            self.kill()
            score.current_score += 1
            explosion_sound.play()
            pygame.mixer.Sound.set_volume(explosion_sound, 0.8)

    def update(self, delta_time: float, score: Score):
        self.pos += self.direction * self.speed * delta_time
        self.rect.topleft = (round(self.pos.x), round(self.pos.y))
        self.meteor_collision(score)

        if self.rect.bottom < 0:
            # laser_group.remove(self)
            self.kill()
