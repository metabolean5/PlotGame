from Player import Player
from Card import Card
import random
import sys


class Game:

    def __init__(self):

        self.players = []
        self.playerNum = 0
        self.deck = []


    # PRINT ALL PLAYER CARDS
    def printPlayerCards(self):

        for i in range(len(self.players)):
            sys.stdout.write("\n\nPlayer " +  str(self.players[i].pID) + " has cards ")
            sys.stdout.write("\t\t")
            for j in range(len(self.players[i].cards)):
                sys.stdout.write(str(self.players[i].cards[j]) +"\t")


    # SHUFFLE AND DISTRIBUTE
    def shuffleNdistribute(self):

        # Create all cards
        if len(self.players) < 5:

            for i in range(8):
                self.deck.append(Card("Brule"))

            for i in range(4):
                self.deck.append(Card("Captain"))
                self.deck.append(Card("Duchess"))
                self.deck.append(Card("Comptess"))
                self.deck.append(Card("Assassin"))
                self.deck.append(Card("Inquisitor"))

        # Shuffle
        for i in range(len(self.deck)):
            randint = random.randint(0 ,len(self.deck) -1)
            self.deck[i] , self.deck[randint] = self.deck[randint] , self.deck[i]

        # Distribute
        for i in range(len(self.players)):
            for j in range(4):
                self.players[i].cards.append(self.deck.pop())


    # GAME INITIALIZER
    def GameInit(self):

        # Player Creation phase
        self.playerNum = input("ENTER PLAYER NUMBER\n")

        for i in range(int(self.playerNum)):
            self.players.append(Player(True,i,self))

        # Card distribution Phase
        self.shuffleNdistribute()


    # UPDATE BEFORE EACH NEW ROUND
    def update(self):

        # remove dead player
        for i in range(len(self.players)):
            if len(self.players[i].cards) < 1:
                sys.stdout.write(str(self.players[i])  +  " is DEAD.\n")
                self.players.remove(self.players[i])


        sys.stdout.write("\n Players still in game :\n")

        # print player data
        for i in range(len(self.players)):
            sys.stdout.write("\n" + str(self.players[i]))


    # MAIN GAME LOOP
    def MainGameLoop(self):

        rrcount = 0
        while(len(self.players) > 2):

            self.update()

            sys.stdout.write("\n NOW PLAYING : " + str(self.players[rrcount % len(self.players)]))

            self.players[rrcount % len(self.players)].play()
            rrcount += 1




























