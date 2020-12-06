import pygame
import sys



if __name__ == '__main__':
    pygame.init()
    running = True
    try:
        data = [int(line) for line in sys.stdin]
        size = width, height = data[0], data[1]
        screen = pygame.display.set_mode(size)
    except Exception:
        print('Неправильный формат ввода')
        running = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.draw.line(screen, (255, 255, 255), (0, 0), (width, height), width=5)
        pygame.draw.line(screen, (255, 255, 255), (0, height), (width, 0), width=5)
        pygame.display.flip()
    pygame.quit()
