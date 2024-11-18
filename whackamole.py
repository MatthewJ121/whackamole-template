import pygame
import random

from pygame.examples.cursors import image

width = 640
height = 512


def main():
    try:
        pygame.init()
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((width, height))
        clock = pygame.time.Clock()
        running = True
        mole_pos = (0, 0)  # from top left corner, starting pos
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    clickX = list(event.pos)[0]
                    clickY = list(event.pos)[1]
                    moleX = list(mole_pos)[0]
                    moleY = list(mole_pos)[1]
                    if moleX < clickX < moleX+32: #check if click is on mole square
                        if moleY < clickY < moleY+32:
                            mole_pos = (random.randrange(0,width//32)*32,random.randrange(0,height//32)*32)
            screen.fill("light green") # can also be RGB value
            screen.blit(mole_image, mole_image.get_rect(topleft=mole_pos)) #draws mole at given location from top left anchor\

            #draw lines
            for i in range(1,width//32 + 1): #loop for vertical lines
                pygame.draw.line(screen,"black", (32*i,0), (32*i,height))
            for i in range(1,height//32 + 1):
                pygame.draw.line(screen, "black", (0, 32*i), (width, 32*i))
            pygame.display.flip() #updates screen
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
