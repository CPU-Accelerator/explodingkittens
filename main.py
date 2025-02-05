# Exploding kittens made my me!
# check out this cool guy --> https://www.github.com/ant-throw-pology
import random as rd


numberofCards = 56
numberOfPlayers = input('How many people are playing? \n')
maxCardsInHand = 8


class Card:
    def __init__(self, name, effect, card):

        def printCards(cardName):
            

        self.name = input("What is the player's name? \n")
        self.effect = effect

    def playCard(self, player, game):
        if self.effect:
            self.effect(game, player)

    def __repr__(self):
        return f"Card({self.name})"


class Deck:
    def __init__(self):
        self.cards = []

    def shuffle(self):
        rd.shuffle(self.cards)

    def draw(self):
        if self.cards:
            return self.cards.pop()
        else:
            print('Draw a card!')

    def add_card(self, card):
        self.cards.append(card)

    def shuffleDeck(self, card):
        if (self.card == "Shuffle"):
            rd.shuffle(self.cards)
        else return


def main