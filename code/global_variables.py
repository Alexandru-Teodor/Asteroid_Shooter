import pygame

#game window size
WINDOW_WIDTH, WINDOW_HEIGHT = 1130, 635

# game window
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

#sprite groups
spaceship_group = pygame.sprite.GroupSingle()
laser_group = pygame.sprite.Group()
meteor_group = pygame.sprite.Group()

# sound
pygame.mixer.init()
background_music = pygame.mixer.Sound("sounds/music.wav")
laser_sound = pygame.mixer.Sound("sounds/laser.ogg")
explosion_sound = pygame.mixer.Sound("sounds/explosion.wav")
