import assets as a


def initialize():
    deck = a.Deck()

    player_1 = a.Player("Player 1")
    player_2 = a.Player("Player 2")

    deck1, deck2 = deck.split_deck()

    player_1.deck(deck1)
    player_2.deck(deck2)

    return player_1, player_2


def logic(card_1, card_2):

    if card_1 > card_2:
        return "<" if card_2 == 1 else ">"
    elif card_1 < card_2:
        return ">" if card_1 == 1 else "<"
    else:
        return "WAR!"


def war():
    pass


def winner(player1, player2):
    if len(player1.hand) == 0 or len(player2.hand) == 0:
        if len(player2.hand) == 0:
            return player1.name
        else:
            return player2.name
    return None


def resolve(player1, player2, rank, drawn_card, drawn_card2, war_deck):
    if rank == ">":
        player1.hand.append(drawn_card)
        player1.hand.append(drawn_card2)
        player1.hand.extend(war_deck)
    elif rank == "<":
        player2.hand.append(drawn_card)
        player2.hand.append(drawn_card2)
        player2.hand.extend(war_deck)

    return player1, player2
