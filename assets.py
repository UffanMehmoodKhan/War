import logic as l
import os
import time

var = l.Deck()

player1 = l.Player("Omni")
player2 = l.Player("AI")


deck_1, deck_2 = var.split_deck()

player1.deck(deck_1)
player2.deck(deck_2)


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
        while war:
            war_set = []
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
    #time.sleep(2)
    os.system('cls')

    if len(player1.hand) == 0:
        print(f"{player1.name} has no more cards left!")
        print(f"{player2.name} wins the game!")
        break

    elif len(player2.hand) == 0:
        print(f"{player2.name} has no more cards left!")
        print(f"{player1.name} wins the game!")
        break
