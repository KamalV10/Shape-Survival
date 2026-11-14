import pygame
import sys
import vars as v
import classes as c

pygame.init()
screen = pygame.display.set_mode((v.WID, v.HEI))
running = True
clock = pygame.time.Clock()
x, y = v.WID // 2, v.HEI // 2

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player = c.Player(x, y, 5, 20)
    player.movement()
    player.barrier()
    player.render()

    x, y = player.x, player.y
    screen.fill(v.BLACK)
    
    clock.tick(60)
pygame.quit
sys.exit