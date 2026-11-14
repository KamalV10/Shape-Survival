import pygame
import vars as v
import random
class Player():
    def __init__(self, x, y, speed, size):
        self.x = x
        self.y = y
        self.speed = speed
        self.size = size
    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.y -= self.speed
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.x -= self.speed            
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.y += self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.x += self.speed
    def barrier(self):
        if self.x < self.size:
            self.x = self.size
        if self.x > v.WID - self.size:
            self.x = v.WID - self.size
        if self.y < self.size:
            self.y = self.size
        if self.y > v.HEI - self.size:
            self.y = v.HEI - self.size
    def render(self, screen):
        pygame.draw.rect(screen, v.WHITE, (self.x, self.y, self.size, self.size))
        pygame.display.flip()
class Enemy_box():
    def __init__(self, enemy_x, enemy_y, enemy_speed):
        self.enemyx = enemy_x
        self.enemyy = enemy_y
        self.enemy_speed = enemy_speed
    def movement(self):
        pass # soon...