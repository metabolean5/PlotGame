
class Card:

    cardTypes = ["Captain", "Duchess", "Comptess", "Assassin", "Inquisitor"]
    cardCount = 0

    def __init__(self,type):

        self.ctype = type

    def __str__(self):
        return self.ctype




