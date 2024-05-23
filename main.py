import random
sum

def create_deck():
    suits = ["♥", "♦", "♣", "♠"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    deck = [(s, r)
            for r in ranks
            for s in suits]
    random.shuffle(deck)
    return deck


def draw_card(deck):
    hand = deck.pop()
    return (hand, deck)

print(draw_card(create_deck()))