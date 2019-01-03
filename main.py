import pygame
from pygame.locals import *
from tearoom import Tearoom


def main():
    """Runs the art piece."""
    teacup_count = 9
    tearoom = Tearoom(teacup_count)
    screen_width = 300 / teacup_count
    screen_height = 300 / teacup_count

    pygame.init()
    screen = pygame.display.set_mode((screen_height, screen_width))
    pygame.display.set_caption('Tearoom')
    pygame.mouse.set_visible(False)

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 0))

    font = pygame.font.Font(None, 36)
    text = font.render("Hello There", 1, (10, 10, 10))

    while True:

        for event in pygame.event.get():
            if event.type == QUIT:
                return
            screen.blit(background, (0, 0))
            pygame.display.flip()


if __name__ == '__main__':
    main()
