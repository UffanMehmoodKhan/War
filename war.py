import pygame
import logic as l
import time
import assets as a

# pygame setup
pygame.init()
size = width, height = 1280, 720
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
state = None
game_state = None
dt = 0

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

mediumFont = pygame.font.Font("OpenSans-Regular.ttf", 28)
largeFont = pygame.font.Font("OpenSans-Regular.ttf", 40)
moveFont = pygame.font.Font("OpenSans-Regular.ttf", 60)

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

player1, player2 = l.initialize()

# Load images once
card_back = pygame.image.load("assets/Backs/back_0.png").convert()
card_back = pygame.transform.scale(card_back, (100, 150))

while running:
    # poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if state is None:
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
                state = "playing"
                screen.fill(black)
    else:
        # Back of Deck Design
        screen.blit(card_back, (150, 400))
        screen.blit(card_back, (950, 400))

        # Draw Card Button
        drawCardButton = pygame.Rect(460, 450, width / 4, 70)
        drawCard = mediumFont.render("Draw Card", True, black)
        drawCardRect = drawCard.get_rect()
        drawCardRect.center = drawCardButton.center
        pygame.draw.rect(screen, white, drawCardButton)
        screen.blit(drawCard, drawCardRect)

        # Game Mechanics
        click, _, _ = pygame.mouse.get_pressed()
        if click == 1:
            mouse = pygame.mouse.get_pos()
            if drawCardButton.collidepoint(mouse):
                game_state = "playing"
                screen.fill(black)

                # Draw cards from players
                drawn_card = player1.draw()
                drawn_card2 = player2.draw()

                time.sleep(0.5)

                # Load and scale images outside the loop
                card1 = pygame.image.load(
                    f"assets/{drawn_card.suit}/{drawn_card.suit}_card_0{drawn_card.rank}.png").convert()
                card1 = pygame.transform.scale(card1, (100, 150))
                card2 = pygame.image.load(
                    f"assets/{drawn_card2.suit}/{drawn_card2.suit}_card_0{drawn_card2.rank}.png").convert()
                card2 = pygame.transform.scale(card2, (100, 150))
                screen.blit(card1, (420, 220))
                screen.blit(card2, (700, 220))

                # Load Rank Determiner
                strength = largeFont.render(">", True, white)
                strengthRect = strength.get_rect()
                strengthRect.center = (620, 290)
                screen.blit(strength, strengthRect)

                # Player 1 : Info and Card Count
                sprite_1 = largeFont.render(f"{player1.name}", True, white)
                sprite_1Rect = sprite_1.get_rect()
                sprite_1Rect.center = (465, 180)
                screen.blit(sprite_1, sprite_1Rect)
                player_1_card_number = largeFont.render(f"{len(player1.hand)}", True, white)
                player_1_card_numberRect = player_1_card_number.get_rect()
                player_1_card_numberRect.center = (200, 600)
                screen.blit(player_1_card_number, player_1_card_numberRect)

                # Player 2 : Info and Card Count
                sprite_2 = largeFont.render(f"{player2.name}", True, white)
                sprite_2Rect = sprite_2.get_rect()
                sprite_2Rect.center = (750, 180)
                screen.blit(sprite_2, sprite_2Rect)
                player_2_card_number = largeFont.render(f"{len(player2.hand)}", True, white)
                player_2_card_numberRect = player_2_card_number.get_rect()
                player_2_card_numberRect.center = (1000, 600)
                screen.blit(player_2_card_number, player_2_card_numberRect)

    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()