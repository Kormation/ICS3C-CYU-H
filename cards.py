# Programmer : Alexander Walker
# Description : This program prints every possible card in a a deck of cards.

#Ever card suit
suits = ["Clubs", "Diamonds", "Spades", "Hearts"]

#Every card value
values = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight",
          "Nine", "Ten", "Jack", "Queen", "King", "Ace"]

#Prints every possible card in a deck
for value in values:
    for suit in suits:
        print(f"{value} of {suit}")