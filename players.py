# Créé par Arborescence Projekt, le 14/09/2025 en Python 3.7

import pygame
from file_manager import ressource_path
size = width, height = 500, 500

class Player:

    def __init__(self, x, y):
        self.player = pygame.image.load(ressource_path("Images/player.png"))
        self.rect = self.player.get_rect(x=x, y=y)
        self.speed = 6
        self.velocity = [0, 0]

    def move(self):
        self.rect.move_ip(self.velocity[0] * self.speed, self.velocity[1] * self.speed)
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > width:
            self.rect.bottom = width


    def draw(self, screen):
        screen.blit(self.player, self.rect)

