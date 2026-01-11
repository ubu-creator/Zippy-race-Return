import pygame
import random
import sys

# Game Settings
WIDTH, HEIGHT = 400, 700
FPS = 60

# Colors - TowMes Professional Edition
ROAD_COLOR = (45, 45, 45)
GRASS_COLOR = (20, 120, 20)
PLAYER_COLOR = (255, 215, 0) # Gold
ENEMY_COLOR = (200, 0, 0)    # Red
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

class ZippyRace:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Zippy Race - TowMes©™")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("monospace", 20, bold=True)
        self.reset()

    def reset(self):
        self.player_x = WIDTH // 2
        self.enemies = []
        self.distance = 0
        self.speed = 10
        self.game_over = False

    def draw_environment(self):
        self.screen.fill(GRASS_COLOR)
        pygame.draw.rect(self.screen, ROAD_COLOR, (60, 0, WIDTH - 120, HEIGHT))
        offset = (self.distance * 5) % 100
        for y in range(-100, HEIGHT, 100):
            pygame.draw.rect(self.screen, WHITE, (WIDTH // 2 - 2, y + offset, 4, 40))

    def run(self):
        while not self.game_over:
            self.draw_environment()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            if pygame.mouse.get_pressed()[0]:
                mouse_x, _ = pygame.mouse.get_pos()
                if mouse_x < self.player_x: self.player_x -= 8
                elif mouse_x > self.player_x: self.player_x += 8

            self.player_x = max(70, min(self.player_x, WIDTH - 105))

            if random.randint(1, 25) == 1:
                self.enemies.append([random.randint(70, WIDTH - 110), -60])
            
            for enemy in self.enemies:
                enemy[1] += self.speed - 2
                pygame.draw.rect(self.screen, ENEMY_COLOR, (enemy[0], enemy[1], 40, 60))
                if pygame.Rect(self.player_x, HEIGHT - 120, 35, 60).colliderect(pygame.Rect(enemy[0], enemy[1], 40, 60)):
                    self.game_over = True

            self.enemies = [e for e in self.enemies if e[1] < HEIGHT]
            pygame.draw.rect(self.screen, PLAYER_COLOR, (self.player_x, HEIGHT - 120, 35, 60))
            
            self.distance += 1
            dist_text = self.font.render(f"Dist: {self.distance}m", True, WHITE)
            watermark = self.font.render("By: TowMes©™", True, YELLOW)
            self.screen.blit(dist_text, (10, 10))
            self.screen.blit(watermark, (10, HEIGHT - 30))

            pygame.display.flip()
            self.clock.tick(FPS)

if __name__ == "__main__":
    ZippyRace().run()
