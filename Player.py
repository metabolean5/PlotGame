
import sys
from Card import Card

CARDTYPES = ["Captain", "Duchess", "Comptess", "Assassin", "Inquisitor"]

class Player:

    VERIFICATORS = []
    TMPLIE = ""

    def __init__(self, isCPU, id, game):

        self.name = ""
        self.pID = id
        self.cards = []
        self.isCPU = isCPU
        self.money = 2
        self.lieCount = 0
        self.game = game



    def __str__(self):

        return "\nPlayer " + str(self.pID) + "\tbifton: " + str(self.money) +  "\t(" + str(len(self.cards)) + " cards left)\n"


    # Block card action of opponent
    def block(self,cardName):

        if cardName == "Captain":

            if self.hasCard("Captain") or self.hasCard("Inquisitor"):
                sys.stdout.write("\n\nPlayer " + str(self.pID) + " blocks the Captain!")  # print to all

                if self.hasCard("Captain") == "1":
                    Player.TMPLIE = "Captain"
                if self.hasCard("Inquisitor"):
                    Player.TMPLIE = "Inquisitor"


                return True
            else:
                resp = input("\n\n Player" + str(self.pID)  + " : You do not have the counter card.  Lie ? (y/n)")

                if resp == "y":

                    resp2 = input("Choose lie : (1) Captain (2) Inquisitor")

                    if resp2 == "1":
                        Player.TMPLIE  = "Captain"
                    else:
                        Player.TMPLIE = "Inquisitor"

                    sys.stdout.write("Player " + str(self.pID)  + " blocks the Captain!")  # print to all
                    return True
                else:
                    return False

    # Card action of Capitain
    def cpt_steal(self ,targetNum):

        sys.stdout.write("\n\nPlayer " + str(self.pID) + " wants to steal from Player "
                         + str(self.game.players[targetNum].pID) )  # print to all


        lie = self.allVerify("Captain")
        if lie: return


        if self.game.players[targetNum].block("Captain"):

            lie = self.allVerify(Player.TMPLIE)

            if not lie:
                sys.stdout.write("\n\nCounter success ! Player " + str(self.game.players[targetNum].pID)
                                 + " is safe\n ")  # print to all
                return


        self.money += 2
        self.game.players[targetNum].money -= 2

        sys.stdout.write("\n\nPlayer " + str(self.pID)  + " steals 2 coins from Player  "
                        + str(self.game.players[targetNum].pID) )  # print to all



    # Assasinate action from you know who
    def ass_kill(self, targetNum):

        sys.stdout.write("\n\nPlayer " + str(self.pID) + " wants to KILL Player "
                         + str(self.game.players[targetNum].pID))  # print to all

        lie = self.allVerify("Assassin")

        # IMPLEMENT ACTION


    def action(self, choice):

        if choice == "Captain":

            sys.stdout.write("Player " + str(self.pID) + " plays the Captain!") #print to all

            for i in range(len(self.game.players)):
                sys.stdout.write("\n("+ str(i)+ ")" + str(self.game.players[i]))

            playerNum = input("\n\nPlayer "+ str(self.pID) + " : From whom would you like to steal ? ")

            self.cpt_steal(int(playerNum))

        if choice == "Assassin":

            sys.stdout.write("Player " + str(self.pID) + " plays the Assassin!")  # print to all

            for i in range(len(self.game.players)):
                sys.stdout.write("\n("+ str(i)+ ")" + str(self.game.players[i]))

            playerNum = input("\n\nPlayer "+ str(self.pID) + " : Who would you like to kill? ")

            self.ass_kill(int(playerNum))


    def play(self):

        tmpOption = []
        lastCount = 0

        # Load honest options
        honestOptions = "\n\nPlayer "+ str(self.pID) + " : Honest  Options : \n"
        honestOptions += "(0) take 2 \t"

        for i in range(len(self.cards)):
            tmpOption.append(str(self.cards[i]))
            honestOptions += "\t (" + str(i + 1) +  ") " + str(self.cards[i])
            lastCount = i


        # Load lying options
        lieOptions = "\n\n Lying Options : \n"

        i=1
        for lieCard in CARDTYPES:
            if lieCard not in tmpOption:
                tmpOption.append(lieCard)
                lieOptions += "\t (" + str(lastCount + i + 1) +  ") " + lieCard
                i += 1


        # Display all Options

        options = honestOptions + lieOptions

        option = input(options)

        if option == "0":
            self.money += 2
            return

        self.action(tmpOption[int(option)-1])




    # UTILITY FUNCTIONs

    def hasCard(self, cardName):

        for card in self.cards:
            if card.ctype == cardName:
                return True

        return False



    def looseCard(self, cardName):

        sys.stdout.write("\nPlayer " + str(self.pID) + " looses a " + cardName)  # print to all

        for card in self.cards:
            if card.ctype == cardName:
                self.cards.remove(card)
                break


    def chooseLooseCard(self):

        options = "\n\n"

        for i in range(len(self.cards)):
            options += "\t (" + str(i) + ") " + str(self.cards[i])

        print(options)
        resp = input("\n\nPlayer "+ str(self.pID) + " : Choose card to loose")

        sys.stdout.write("\nPlayer " + str(self.pID) + " looses a " + str(self.cards[int(resp)]))  # print to all
        self.cards.remove(self.cards[int(resp)])



    def allVerify(self, cardName):

        Player.VERIFICATORS = []
        Player.VERIFYB = False

        # All players get to say if they want to verify or not
        for player in self.game.players:

            if player == self:
                continue

            player.verify(cardName, self)


        # Checks if somebody detected a lie
        if Player.VERIFICATORS:
            for ver in Player.VERIFICATORS:
                sys.stdout.write("\nPlayer " + str(ver.pID) + " declares Player "
                                 + str(self.pID) + " a liar !")  # print to all

            if self.hasCard(cardName):
                sys.stdout.write("\n\nPlayer " + str(self.pID) + " is NOT a liar !\n")  # print to all

                for ver in Player.VERIFICATORS:
                    sys.stdout.write("\nPlayer " + str(ver.pID) + " is a suspicious Linus...") # print to all
                    ver.chooseLooseCard()
                    return False

            else:
                sys.stdout.write("\n\nPlayer " + str(self.pID) + " is indeed a liar!\n")
                self.looseCard(cardName)
                return True

        else:
            sys.stdout.write("\n\nPlayer " + str(self.pID) + " seems honest" ) # print to all
            return False







    def verify(self, cardName,  opponent):

        resp = input("\n\nPlayer " + str(self.pID) + " : do you want to verify if Player " +
                     str(opponent.pID) + " has card '" + cardName + "' ? Declare liar ? (y/n)")

        if resp == "y":
            Player.VERIFICATORS.append(self)





































