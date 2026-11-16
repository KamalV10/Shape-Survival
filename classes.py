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
        if self.x < 0:
            self.x = 0
        if self.x > v.WID - self.size:
            self.x = v.WID - self.size
        if self.y < 0:
            self.y = 0
        if self.y > v.HEI - self.size:
            self.y = v.HEI - self.size

    def render(self, screen):
        pygame.draw.rect(screen, v.WHITE, (self.x, self.y, self.size, self.size))

    def get_rect(self):
            return pygame.Rect(self.x, self.y, self.size, self.size)
    
    def is_hit(self, enemies):
        for enemy in enemies:
            if self.get_rect().colliderect(enemy.get_rect()):
                return True
        return False
class EnemyBox():
    def __init__(self, x, y, speed, size, color, frames, directions):
        self.x = x
        self.y = y
        self.speed = speed
        self.size = size
        self.color = color
        self.frames = frames
        self.directions = directions

    def movement(self, game_over):
        if game_over:
            return
        if self.frames == 0:
            self.directions = random.choice(v.DIRECTIONS)
            self.frames = 30
        if self.directions == "up":
            self.y -= self.speed
        elif self.directions == "down":
            self.y += self.speed
        elif self.directions == "left":
            self.x -= self.speed
        elif self.directions == "right":
            self.x += self.speed
        self.frames -= 1

    def barrier(self):
        if self.x < 0:
            self.x = 0
        if self.x > v.WID - self.size:
            self.x = v.WID - self.size
        if self.y < 0:
            self.y = 0
        if self.y > v.HEI - self.size:
            self.y = v.HEI - self.size

    def render(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.size, self.size)

    def check_collision(self, other):
        return self.get_rect().colliderect(other.get_rect())