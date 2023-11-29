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

# end the game

# Implement:
# 1. The score
# 2. private variables
# 3. Invisible mouse
# 4. Game over screen 
#           -> pause the game and show the message "Game Over"
#           -> crt_ score and best score
#           -> with restart button if possible

# Differences:
# 1. project organized in more modules (files) and packages(folders) 
#       -are they called modules and packages?
# 2. sounds as global variables
#       - I had to write pygame.mixer.init(), but I've read that initing pygame more than once should not be a problem
# 3. reduced volume to the sounds - they were too loud
# 4. invisible mouse during the game
# 5. a score - incremented every time a meteor is hit
# 6. increase difficulty (+100 speed) every 10 meteors hit
