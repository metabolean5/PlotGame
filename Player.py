
import sys



class Player:


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
                return True
            else:
                resp = input("\n\n Player" + str(self.pID)  + " : You do not have the counter card.  Lie ? (y/n)")

                if resp == "y":
                    sys.stdout.write("Player " + str(self.pID)  + " blocks the Captain!")  # print to all
                    return True
                else:
                    return False

    # Card action of Capitain
    def cpt_steal(self ,targetNum):

        sys.stdout.write("\n\nPlayer " + str(self.pID) + " wants to steal from Player "
                         + str(self.game.players[targetNum].pID) )  # print to all

        if self.game.players[targetNum].block("Captain"):

            msg = "\n\nPlayer "+ str(self.pID) + " : Verify if Player " + str(self.game.players[targetNum]) + " has cards 'Captain' or 'Inquisitor'? (y/n) "
            resp = input(msg)

            if resp == "y":
                if self.game.players[targetNum].hasCard("Captain") or self.game.players[targetNum].hasCard("Inquisitor"):

                    sys.stdout.write("\n\nPlayer " + str(self.pID) + " got FULL countered by Player "
                                     +  str(self.game.players[targetNum].pID) + "and looses his Captain ")  # print to all

                    self.looseCard("Captain")
                    return
                else:

                    sys.stdout.write("\n\nPlayer " + str(self.game.players[targetNum].pID)
                                     + " lied and got caught")  # print to all

                    self.game.players[targetNum].chooseLooseCard()
                    return
            else:
                sys.stdout.write("\n\nCounter success ! Player " + str(self.game.players[targetNum].pID)
                                 + " is safe\n ")  # print to all
                return

        else:

            self.money += 2
            self.game.players[targetNum].money -= 2

            sys.stdout.write("\n\nPlayer " + str(self.pID)  + " steals 2 coins from Player  "
                             + str(self.game.players[targetNum].pID) )  # print to all




    def action(self, choice):

        if choice == "Captain":

            sys.stdout.write("Player " + str(self.pID) + " plays the Captain!") #print to all

            for i in range(len(self.game.players)):
                sys.stdout.write("\n("+ str(i)+ ")" + str(self.game.players[i]))

            playerNum = input("\n\nPlayer "+ str(self.pID) + " : From whom would you like to steal ? ")

            self.cpt_steal(int(playerNum))



    def play(self):

        tmpOption = []
        honestOptions = "\n\nPlayer "+ str(self.pID) + " :   Options : \n"
        honestOptions += "(0) take 2 \t"

        for i in range(len(self.cards)):
            tmpOption.append(self.cards[i])
            honestOptions += "\t (" + str(i + 1) +  ") " + str(self.cards[i])


        honestOption = input(honestOptions)

        if honestOption == "0":
            self.money += 2
            return

        self.action(tmpOption[int(honestOption)-1].ctype)




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































