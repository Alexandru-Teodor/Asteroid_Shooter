import pygame
from global_variables import WINDOW_WIDTH, WINDOW_HEIGHT, display_surface
from classes_folder.score import Score

class GameOver:
    def __init__(self) -> None:
        self.message_font = pygame.font.Font("graphics/subatomic.ttf", 50)
        self.score_font = pygame.font.Font("graphics/subatomic.ttf", 30)
        self.end_game = False
        self.last_update = True

        self.message_text = "Game over"
        self.message_surf = self.message_font.render(self.message_text, True, "red")
        self.message_pos = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 - WINDOW_HEIGHT / 8)
        self.message_rect = self.message_surf.get_rect(center = self.message_pos)

    def display_message(self):
        display_surface.blit(self.message_surf, self.message_rect)

    def crt_score_pos(self) -> tuple:
        x = self.message_rect.left
        y = self.message_rect.bottom + 30
        return (x, y)
    
    def best_score_pos(self) -> tuple:
        x = self.message_rect.left + 30
        y = self.message_rect.bottom + 70
        return (x, y)

    def display_crt_score(self, score: Score):
        crt_score = score.current_score
        crt_score_text = f"Current score: {crt_score}"
        crt_score_surf = self.score_font.render(crt_score_text, True, "green3")
        crt_score_rect = self.message_surf.get_rect(topleft = self.crt_score_pos())
        display_surface.blit(crt_score_surf,crt_score_rect)

    def display_best_score(self, score: Score):
        best_score = score.best_score
        best_score_text = f"Best score: {best_score}"
        best_score_surf = self.score_font.render(best_score_text, True, "green3")
        best_score_rect = self.message_surf.get_rect(topleft = self.best_score_pos())
        display_surface.blit(best_score_surf, best_score_rect)

    def update(self, score: Score):
        self.display_message()
        self.display_crt_score(score)
        self.display_best_score(score)



