import copy

import assets as a
import os
import time


def initialize():
    deck = a.Deck()

    player_1 = a.Player("Player 1")
    player_2 = a.Player("Player 2")

    deck1, deck2 = deck.split_deck()

    player_1.deck(deck1)
    player_2.deck(deck2)

    return player_1, player_2


def logic(sprite1, sprite2):
    player1 = copy.deepcopy(sprite1)
    player2 = copy.deepcopy(sprite2)

    while True:
        card = player1.draw()
        card2 = player2.draw()

        print(f"{player1.name} drew: {card.rank} of {card.suit}")
        print(f"{player2.name} drew: {card2.rank} of {card2.suit}")

        if card.rank > card2.rank:
            print(f"\n{player1.name} wins this round!")
            player1.hand.append(card)
            player1.hand.append(card2)
        elif card.rank < card2.rank:
            print(f"\n{player2.name} wins this round!")
            player2.hand.append(card)
            player2.hand.append(card2)
        else:
            print("War!")
            war = True
            war_set = []
            while war:
                war_set.append(card)
                war_set.append(card2)

                card = player1.draw()
                card2 = player2.draw()
                print(f"{player1.name} drew: {card.rank} of {card.suit}")
                print(f"{player2.name} drew: {card2.rank} of {card2.suit}")
                if card.rank > card2.rank:
                    print(f"\n{player1.name} wins this round!")
                    player1.hand.append(card2)
                    player1.hand.append(card)
                    player1.hand.extend(war_set)
                    war = False
                elif card.rank < card2.rank:
                    print(f"\n{player2.name} wins this round!")
                    player2.hand.append(card)
                    player2.hand.append(card2)
                    player2.hand.extend(war_set)
                    war = False
                else:
                    print("War!")
                    war = True
        time.sleep(2)
        os.system('cls')

        if len(player1.hand) == 0:
            print(f"{player1.name} has no more cards left!")
            print(f"{player2.name} wins the game!")
            break

        elif len(player2.hand) == 0:
            print(f"{player2.name} has no more cards left!")
            print(f"{player1.name} wins the game!")
            break
