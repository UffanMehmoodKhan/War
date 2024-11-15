import pygame
import logic as l
import time

# pygame setup
pygame.init()
size = width, height = 1280, 720
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
state = None
game_state = None
war_deck = []
player1, player2 = None, None
dt = 0

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# Fonts
mediumFont = pygame.font.Font("../OpenSans-Regular.ttf", 28)
largeFont = pygame.font.Font("../OpenSans-Regular.ttf", 40)
smallFont = pygame.font.Font("../OpenSans-Regular.ttf", 15)
moveFont = pygame.font.Font("../OpenSans-Regular.ttf", 60)

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

# Load images once
card_back = pygame.image.load("../assets/Backs/back_0.png").convert()
card_back = pygame.transform.scale(card_back, (100, 150))

while running:
    # poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if state is None:
        screen.fill("black")
        playButton = pygame.Rect((width / 2) - 150, 500, width / 4, 70)
        play = mediumFont.render("Play War", True, black)
        playRect = play.get_rect()
        playRect.center = playButton.center
        pygame.draw.rect(screen, white, playButton)
        screen.blit(play, playRect)

        # Display rules
        rules = [
            "The Deal",
            "The deck is divided evenly, with each player receiving 26 cards, dealt one at a time, face down.",
            "Anyone may deal first. Each player places their stack of cards face down, in front of them.",
            "",
            "The Play",
            "Each player turns up a card at the same time and the player with the higher card takes both cards and "
            "puts them, face down, on the bottom of his stack.",
            "If the cards are the same rank, it is War. Each player turns up one card face down and one card face up.",
            ""
            "The player with the higher cards takes both piles (six cards). If the turned-up cards are again the same "
            "rank, each player places another card face down and turns another card face up. The player with the "
            "higher card takes all 10 cards, and so on.",
            "",
            "How to Keep Score",
            "The game ends when one player has won all the cards"
        ]

        y_offset = 100
        for line in rules:
            rule_text = smallFont.render(line, True, white)
            screen.blit(rule_text, (100, y_offset))
            y_offset += 30

        click, _, _ = pygame.mouse.get_pressed()
        if click == 1:
            mouse = pygame.mouse.get_pos()
            if playButton.collidepoint(mouse):
                state = "playing"
                screen.fill(black)

                # Initialize Players
                player1, player2 = l.initialize()

    else:

        # Back of Deck Design
        screen.blit(card_back, (170, 400))
        player_1_card_number = largeFont.render(f"{len(player1.hand)}", True, white)
        player_1_card_numberRect = player_1_card_number.get_rect()
        player_1_card_numberRect.center = (200, 600)
        screen.blit(player_1_card_number, player_1_card_numberRect)

        screen.blit(card_back, (650, 400))
        player_2_card_number = largeFont.render(f"{len(player2.hand)}", True, white)
        player_2_card_numberRect = player_2_card_number.get_rect()
        player_2_card_numberRect.center = (700, 600)
        screen.blit(player_2_card_number, player_2_card_numberRect)

        # Draw Card Button
        drawCardButton = pygame.Rect(300, 450, width / 4, 70)
        drawCard = mediumFont.render("Draw Card", True, black)
        drawCardRect = drawCard.get_rect()
        drawCardRect.center = drawCardButton.center
        pygame.draw.rect(screen, white, drawCardButton)
        screen.blit(drawCard, drawCardRect)

        if l.winner(player1, player2) is not None:
            winner = largeFont.render(f"{l.winner(player1, player2)} wins!", True, white)
            winnerRect = winner.get_rect()
            winnerRect.center = (1000, 500)
            screen.blit(winner, winnerRect)

        # Game Mechanics
        click, _, _ = pygame.mouse.get_pressed()
        if click == 1:
            mouse = pygame.mouse.get_pos()
            if drawCardButton.collidepoint(mouse):
                if l.winner(player1, player2) is not None:
                    state = None
                    continue

                game_state = "playing"
                screen.fill(black)

                # Player 1 : Info and Card Count
                sprite_1 = largeFont.render(f"{player1.name}", True, white)
                sprite_1Rect = sprite_1.get_rect()
                sprite_1Rect.center = (345, 180)
                screen.blit(sprite_1, sprite_1Rect)

                # Player 2 : Info and Card Count
                sprite_2 = largeFont.render(f"{player2.name}", True, white)
                sprite_2Rect = sprite_2.get_rect()
                sprite_2Rect.center = (570, 180)
                screen.blit(sprite_2, sprite_2Rect)

                if game_state is None:
                    state = None
                    continue
                else:

                    # Draw cards from players
                    drawn_card = player1.draw()
                    drawn_card2 = player2.draw()

                    time.sleep(0.5)

                    rank = l.logic(drawn_card.rank, drawn_card2.rank)

                    # Load and scale images outside the loop
                    card1 = pygame.image.load(
                        f"../assets/{drawn_card.suit}/{drawn_card.suit}_card_0{drawn_card.rank}.png").convert()
                    card1 = pygame.transform.scale(card1, (100, 150))
                    card2 = pygame.image.load(
                        f"../assets/{drawn_card2.suit}/{drawn_card2.suit}_card_0{drawn_card2.rank}.png").convert()
                    card2 = pygame.transform.scale(card2, (100, 150))
                    screen.blit(card1, (300, 220))
                    screen.blit(card2, (530, 220))

                    # Load Rank Determiner
                    strength = largeFont.render(rank, True, white)
                    strengthRect = strength.get_rect()
                    strengthRect.center = (470, 290)
                    screen.blit(strength, strengthRect)

                    # Line Divider
                    start_pos = (820, 100)
                    end_pos = (820, height - 100)
                    pygame.draw.line(screen, white, start_pos, end_pos, 5)  # 5 is the width of the line

                    # WAR Case
                    if rank == "WAR!":
                        strength = largeFont.render("WAR!", True, white)
                        war_deck.append(drawn_card)
                        war_deck.append(drawn_card2)
                        for i in range(1):
                            war_deck.append(player1.draw())
                            war_deck.append(player2.draw())
                        warDeck = largeFont.render(f"War Deck: {len(war_deck)}", True, white)
                        warDeckRect = warDeck.get_rect()
                        warDeckRect.center = (1050, 180)
                        screen.blit(warDeck, warDeckRect)

                        screen.blit(card_back, (1000, 300))
                        player_1_card_number = largeFont.render(f"{len(player1.hand)}", True, white)
                        player_1_card_numberRect = player_1_card_number.get_rect()
                        player_1_card_numberRect.center = (200, 600)
                        screen.blit(player_1_card_number, player_1_card_numberRect)

                        screen.blit(card_back, (1050, 300))
                        player_2_card_number = largeFont.render(f"{len(player2.hand)}", True, white)
                        player_2_card_numberRect = player_2_card_number.get_rect()
                        player_2_card_numberRect.center = (700, 600)
                        screen.blit(player_2_card_number, player_2_card_numberRect)

                        continue

                    # War Deck Count
                    warDeck = largeFont.render(f"War Deck: {len(war_deck)}", True, white)
                    warDeckRect = warDeck.get_rect()
                    warDeckRect.center = (1050, 180)
                    screen.blit(warDeck, warDeckRect)
                    start_pos = (820, 100)
                    end_pos = (820, height - 100)
                    pygame.draw.line(screen, white, start_pos, end_pos, 5)  # 5 is the width of the line

                    player1, player2 = l.resolve(player1, player2, rank, drawn_card, drawn_card2, war_deck)
                    war_deck = []

    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()
