import pygame
from global_variables import WINDOW_HEIGHT, display_surface


class Time:
    def __init__(self) -> None:
        self.font = pygame.font.Font("graphics/subatomic.ttf", 30)

    def display(self):
        time_text = f"{pygame.time.get_ticks() // 1000:02}"
        text_surf = self.font.render(time_text, True, "white")
        text_rect = text_surf.get_rect(bottomleft = (80, WINDOW_HEIGHT - 50))
        display_surface.blit(text_surf, text_rect)
        pygame.draw.rect(display_surface, "white", text_rect.inflate(30, 30),
                          width = 5, border_radius = 5)
    