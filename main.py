import pygame

SIZE_BLOCK = 20
FRAME_COLOR = (50, 50, 204)
WHITE = (255, 255, 255)
BLUE = (204, 255, 255)
COUNT_BLOCKS = 20
MARGIN = 1

size = [400, 600]

screen = pygame.display.set_mode(size)
pygame.display.set_caption('Змеюка')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('exit')
            pygame.quit()

    screen.fill(FRAME_COLOR)

    for column in range(COUNT_BLOCKS):
        if column % 2 == 0:
            color = BLUE
        else:
            color = WHITE
        pygame.draw.rect(screen, color, [10 + column * SIZE_BLOCK + MARGIN, 20, SIZE_BLOCK, SIZE_BLOCK])

    pygame.display.flip()


    jkvbguyhfguttg4