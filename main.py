import pygame
from constants import *
from player import * 

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    player = Player((SCREEN_WIDTH/2),(SCREEN_HEIGHT/2))
    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        player.draw(screen)
        pygame.display.flip()

        #limit the framerate to 60fps
        dt = clock.tick(60)/1000
    

if __name__ == "__main__":
    main()