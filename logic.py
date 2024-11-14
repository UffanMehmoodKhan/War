import random


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def deck(self, deck):
        self.hand = deck

    def reveal_hand(self):
        print(f"Deck of {self.name}")
        for card in self.hand:
            card.show()

    def draw(self):
        return self.hand.pop(0)


class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for suit in ["Diamond", "Club", "Heart", "Spade"]:
            for rank in range(1, 13):
                self.cards.append(Card(suit, rank))
        random.shuffle(self.cards)

    def print_deck(self):
        for card in self.cards:
            card.show()

    def split_deck(self):
        mid = len(self.cards) // 2
        return self.cards[:mid], self.cards[mid:]


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def show(self):
        print(f"{self.rank} of {self.suit}")


# class Card subtypes:

# class Diamond(Card):
#     def __init__(self, rank):
#         super().__init__("Diamond", rank)
#
#     def show(self):
#         print(f"{self.rank} of {self.suit}")
#
#
# class Club(Card):
#     def __init__(self, rank):
#         super().__init__("Club", rank)
#
#
# class Heart(Card):
#     def __init__(self, rank):
#         super().__init__("Heart", rank)
#
#
# class Spade(Card):
#     def __init__(self, rank):
#         super().__init__("Spade", rank)
#
#
# class Hand:
#     def __init__(self):
#         self.cards = []
#
#     def add_card(self, card):
#         self.cards.append(card)
#
#     def remove_card(self, card):
#         self.cards.remove(card)
#
#     def show(self):
#         for card in self.cards:
#             print(card.rank, card.suit)
#
