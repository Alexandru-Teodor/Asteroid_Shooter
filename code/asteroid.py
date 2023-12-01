import pygame, sys
from random import randint

from global_variables import *
from classes_folder.ship import Ship
from classes_folder.meteor import Meteor
from classes_folder.time import Time
from classes_folder.score import Score
from classes_folder.game_over import GameOver


# basic setup
pygame.init()
#game window is imported from global_variables
pygame.display.set_caption("Space Shooter")
clock = pygame.time.Clock()

#background
background_surf = pygame.image.load("graphics/background.png").convert()

#sprite creation
ship = Ship(spaceship_group)

# timer object
time_text = Time()

# score object
score_text  = Score()

# meteor timer
meteor_timer = pygame.event.custom_type()
pygame.time.set_timer(meteor_timer, 400)

# play background music
background_music.play(loops=-1)
pygame.mixer.Sound.set_volume(background_music, 0.3)

# mouse not visible during the game
pygame.mouse.set_visible(False)

# end game
game_over = GameOver()

# game loop
while True:
    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()
        
        if event.type == meteor_timer:
            meteor_x_pos = randint(-100, WINDOW_WIDTH + 100)
            meteor_y_pos = randint(-150, -50)
            Meteor((meteor_x_pos, meteor_y_pos), score_text, meteor_group)
    
    if not game_over.end_game:
        #delta time
        dt = clock.tick() / 1000
        
        #background
        display_surface.blit(background_surf, (0, 0))

        #update
        spaceship_group.update(game_over)
        laser_group.update(dt, score_text)
        meteor_group.update(dt)

        # display timer
        time_text.display()

        # display score
        score_text.display()

        #graphics
        spaceship_group.draw(display_surface)
        laser_group.draw(display_surface)
        meteor_group.draw(display_surface)
        
        #draw the frame
        pygame.display.update()
    else:
        pygame.mouse.set_visible(True)
        game_over.crt_score = score_text.current_score
        game_over.update(score_text)
        if game_over.last_update:
            pygame.display.update()
            game_over.last_update = False
