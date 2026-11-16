import pygame
import sys
import vars as v
import classes as c

pygame.init()
screen = pygame.display.set_mode((v.WID, v.HEI))
running = True
game_over = False
clock = pygame.time.Clock()

player = c.Player(v.WID // 2, v.HEI // 2, 5, 30)
enemies = [
    c.EnemyBox(100, 100, 10, 50, v.RED, 150, v.DIRECTIONS),
    c.EnemyBox(100, 700, 10, 50, v.RED, 150, v.DIRECTIONS),
    c.EnemyBox(700, 100, 10, 50, v.RED, 150, v.DIRECTIONS),
    c.EnemyBox(700, 700, 10, 50, v.RED, 150, v.DIRECTIONS),
]

font_small = pygame.font.SysFont(None, 48)
font_big = pygame.font.SysFont(None, 120)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

            if game_over and event.key == pygame.K_r:
                player = c.Player(v.WID // 2, v.HEI // 2, 5, 30)
                enemies = [
                    c.EnemyBox(100, 100, 10, 50, v.RED, 150, v.DIRECTIONS),
                    c.EnemyBox(100, 700, 10, 50, v.RED, 150, v.DIRECTIONS),
                    c.EnemyBox(700, 100, 10, 50, v.RED, 150, v.DIRECTIONS),
                    c.EnemyBox(700, 700, 10, 50, v.RED, 150, v.DIRECTIONS),
                ]
                game_over = False

    if not game_over:
        player.movement()
        player.barrier()

        for e in enemies:
            e.movement(game_over)
            e.barrier()

        if player.is_hit(enemies):
            game_over = True

    screen.fill(v.BLACK)

    if not game_over:
        player.render(screen)
        for e in enemies:
            e.render(screen)
    else:
        game_over_text = font_big.render("GAME OVER", True, v.WHITE)
        screen.blit(game_over_text, (v.WID // 2 - game_over_text.get_width() // 2, v.HEI // 2 - 40))
        restart_text = font_small.render("R to restart", True, v.WHITE)
        screen.blit(restart_text, (v.WID // 2 - restart_text.get_width() // 2, v.HEI // 2 + 40))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
