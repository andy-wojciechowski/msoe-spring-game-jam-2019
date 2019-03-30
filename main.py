import pygame
import sys
from game.player import Player
from game.level1 import Level1

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700


def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
    pygame.display.set_caption('Cross Dimensional Platformer')

    player = Player(pygame.image.load("anim1.png"), SCREEN_WIDTH)
    current_level = Level1(player)

    sprite_list = pygame.sprite.Group()
    sprite_list.add(player)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    player.move_right()
                elif event.key == pygame.K_LEFT:
                    player.move_left()
                elif event.key == pygame.K_UP:
                    player.jump()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    player.stop()

        screen.fill((0, 0, 0))
        sprite_list.update()
        current_level.update()

        current_level.draw(screen)
        sprite_list.draw(screen)

        pygame.display.update()


if __name__ == "__main__":
    main()
