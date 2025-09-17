# Créé par Arborescence Projekt, le 14/09/2025 en Python 3.7

import pygame, time, random
from players import Player
from ball import Ball
from file_manager import ressource_path

width, height = 1000, 500

class Pong:

    def __init__(self, screen):
        self.screen = screen
        self.running = True
        self.started = False
        self.clock = pygame.time.Clock()
        self.player1 = Player(20, height/2 - 50)
        self.player2 = Player(width - 40, height/2 - 50)
        self.ball = Ball(width/2, height/2)
        self.font = pygame.font.SysFont(None, 48)
        self.ground_color1 = [random.randint(0, 100),random.randint(0, 100),random.randint(0, 100), 30]
        self.ground_color2 = [random.randint(0, 100),random.randint(0, 100),random.randint(0, 100), 30]
        self.score1 = 0
        self.score2 = 0

    def handling_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if not self.started:
                    self.ball.velocity = [random.choice([-1,1]), random.choice([-1,1])]
                self.started = True


        keys = pygame.key.get_pressed()
        if keys[pygame.K_s]:
            self.player1.velocity[1] = 1
        elif keys[pygame.K_z]:
            self.player1.velocity[1] = -1
        elif keys[pygame.K_q]:
            self.player1.velocity[0] = -1
        elif keys[pygame.K_d]:
            self.player1.velocity[0] = 1
        else:
            self.player1.velocity[1] = 0
            self.player1.velocity[0] = 0

        if keys[pygame.K_DOWN]:
            self.player2.velocity[1] = 1
        elif keys[pygame.K_UP]:
            self.player2.velocity[1] = -1
        elif keys[pygame.K_LEFT]:
            self.player2.velocity[0] = -1
        elif keys[pygame.K_RIGHT]:
            self.player2.velocity[0] = 1
        else:
            self.player2.velocity[1] = 0
            self.player2.velocity[0] = 0

        if self.player1.rect.left < 20:
            self.player1.rect.left = 20
        if self.player1.rect.right > 200:
            self.player1.rect.right = 200
        if self.player2.rect.left < width - 200:
            self.player2.rect.left = width - 200
        if self.player2.rect.right > width - 20:
            self.player2.rect.right = width - 20


    def update(self):
        if self.started:
            keys = pygame.key.get_pressed()
            self.player1.move()
            self.player2.move()
            self.ball.move(self.player1, self.player2, keys)

            score = self.ball.move(self.player1, self.player2, keys)

            if score == "player1":
                self.score1 += 1
                self.reset_round()
            if score == "player2":
                self.score2 += 1
                self.reset_round()

        if (self.score1 or self.score2) >= 9:
            self.ball.change_image(ressource_path("Images/balllost.png"))


    def score(self, score, x, y, screen):
        if score < 10:
            score_str = str(score).zfill(1)
        if score >= 10:
            score_str = str(score).zfill(2)

        for i, char in enumerate(score_str):
            image = pygame.image.load(ressource_path(f"Images/{char}.png"))
            rect = image.get_rect()
            rect.topleft = (x + i * rect.width, y)
            screen.blit(image, rect)



    def display(self):
        self.screen.fill([200,200,200])
        self.ball.draw(self.screen)
        ground_player_1 = pygame.Surface((190, height), pygame.SRCALPHA)
        ground_player_1.fill(self.ground_color1)
        screen.blit(ground_player_1,(15, 0))
        ground_player_2 = pygame.Surface((190, height), pygame.SRCALPHA)
        ground_player_2.fill(self.ground_color2)
        screen.blit(ground_player_2,(width - 190 - 15, 0))
        self.score(self.score1, width / 4 * 1.5 - 66 , 20, screen)
        self.score(self.score2, width / 4 * 2.5, 20, screen)
        self.player1.draw(self.screen)
        self.player2.draw(self.screen)


        if not self.started:
            self.player1 = Player(20, height/2 - 50)
            self.player2 = Player(width - 40, height/2 - 50)
            self.ball = Ball(width/2, height/2)
            overlay = pygame.Surface((width, height), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 120))
            screen.blit(overlay,(0, 0))
            text1 = self.font.render("Press any key play", True, "white")
            text2 = self.font.render("(P1) WASD and (P2) arrow keys", True, "white")
            text_rect1 = text1.get_rect(center=(width/2, height/2))
            text_rect2 = text2.get_rect(center=(width/2, height/2 + 48))
            self.screen.blit(text1, text_rect1)
            self.screen.blit(text2, text_rect2)

        pygame.display.flip()

    def reset_round(self):
        time.sleep(0.3)
        self.ball.velocity = [0, 0]
        self.ball.rect.center = (width / 2, height / 2)
        self.started = False
        pygame.mixer.Sound(ressource_path("Sounds/point.wav")).play()

    def run(self):
        while self.running:
            self.handling_event()
            self.update()
            self.display()
            self.clock.tick(60)


pygame.init()
screen = pygame.display.set_mode((width, height))
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("PONGPY! v1.0")
game = Pong(screen)
game.run()

pygame.quit()