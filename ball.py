# Créé par Arborescence Projekt, le 14/09/2025 en Python 3.7

import pygame, sys, os
from file_manager import ressource_path, Sound_Manager

width, height = 1000, 500
pygame.mixer.init()
sm = Sound_Manager()


class Ball:

    def __init__(self, x, y, alpha):
        self.ball = pygame.image.load(ressource_path("Images/ball.png"))
        self.rect = self.ball.get_rect(x=x, y=y)
        self.speed = 5
        self.velocity = [0, 0]
        self.sfx = False
        self.alpha = alpha
        self.volume = 1

    def move(self, player1, player2, keys):
        self.rect.x += self.velocity[0] * self.speed
        self.rect.y += self.velocity[1] * self.speed

        if self.rect.top <= 0 or self.rect.bottom >= height:
            self.velocity[1] *= -1

        if self.rect.colliderect(player1.rect):
            if self.rect.left - player1.rect.right < 0 or (self.rect.left - player1.rect.right <= 10 and keys[pygame.K_d]):
                self.velocity[0] *= -1
                self.rect.left = player1.rect.right + 1
                if not self.sfx:
                    if self.alpha > 139:
                        sm.play("sfx_ball_glitched")
                    else:
                        sm.play("sfx_ball")
                    self.sfx = True
        elif self.rect.colliderect(player2.rect):
            if self.rect.right - player2.rect.left > 0 or (self.rect.right - player2.rect.left <= 10 and keys[pygame.K_LEFT]):
                self.velocity[0] *= -1  # ← ici, on INVERSE au lieu de forcer
                self.rect.right = player2.rect.left - 1
                if not self.sfx:
                    if self.alpha > 139:
                        sm.play("sfx_ball_glitched")
                    else:
                        sm.play("sfx_ball")
                    self.sfx = True
        else:
            self.sfx = False

        if self.rect.left < 0:
            if self.alpha > 139:
                sm.play("sfx_explosion_glitched")
            else:
                sm.play("sfx_explosion")
            return "player2"
        elif self.rect.right > width:
            if self.alpha > 139:
                sm.play("sfx_explosion_glitched")
            else:
                sm.play("sfx_explosion")
            return "player1"
        else:
            return None

    def change_image(self, path):
        self.ball = pygame.image.load(ressource_path(path))

    def draw(self, screen):
        screen.blit(self.ball, self.rect)
