# Example file showing a circle moving on screen
import pygame
import time
import logic as l
import copy
import assets as a
import os

# pygame setup
pygame.init()
size = width, height = 1280, 720
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
state = None
dt = 0

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

mediumFont = pygame.font.Font("OpenSans-Regular.ttf", 28)
largeFont = pygame.font.Font("OpenSans-Regular.ttf", 40)
moveFont = pygame.font.Font("OpenSans-Regular.ttf", 60)

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

player1, player2 = l.initialize()

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if state is None:
        # fill the screen with a color to wipe away anything from last frame
        screen.fill("black")
        playButton = pygame.Rect((width / 2) - 150, 320, width / 4, 70)
        play = mediumFont.render("Play War", True, black)
        playRect = play.get_rect()
        playRect.center = playButton.center
        pygame.draw.rect(screen, white, playButton)
        screen.blit(play, playRect)

        click, _, _ = pygame.mouse.get_pressed()
        if click == 1:
            mouse = pygame.mouse.get_pos()
            if playButton.collidepoint(mouse):
                time.sleep(0.2)
                state = "playing"
    else:
        # fill the screen card game mechanics
        screen.fill("black")

        drawn_card = player1.draw()
        drawn_card2 = player2.draw()

        # Card 1
        card = pygame.image.load(f"assets/{drawn_card.suit}/{drawn_card.suit}_card_0{drawn_card.rank}.png").convert()
        card = pygame.transform.scale(card, (100, 150))
        screen.blit(card, (450, 250))

        # Card 2
        card = pygame.image.load(f"assets/{drawn_card2.suit}/{drawn_card2.suit}_card_0{drawn_card2.rank}.png").convert()
        card = pygame.transform.scale(card, (100, 150))
        screen.blit(card, (750, 250))

        time.sleep(2)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
