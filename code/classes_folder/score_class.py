import pygame
from global_variables import WINDOW_WIDTH, WINDOW_HEIGHT, display_surface
from .time_class import Time

class Score(Time):
    def __init__(self) -> None:
        super().__init__()
        self.current_score = 0
        self.best_score = self.get_best_score()

    def get_best_score(self) -> list:
        with open("utils/best_score.txt") as score_file:
            best_score = score_file.readline()
        if best_score:
            return int(best_score)
        return 0
    
    def update_scores(self):
        if self.current_score > self.best_score:
            with open("utils/best_score.txt", "w") as score_file:
                score_file.write(f"{self.current_score}")

    def display(self):
        self.best_score = self.get_best_score()
        self.update_scores()
        text_surf = self.font.render(f"{self.current_score}", True, "white")
        text_rect = text_surf.get_rect(
            bottomright = (WINDOW_WIDTH - 80, WINDOW_HEIGHT - 50))
        display_surface.blit(text_surf, text_rect)
        pygame.draw.rect(display_surface, "white", text_rect.inflate(30, 30),
                         width = 5, border_radius= 5)
