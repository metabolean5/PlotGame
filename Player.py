
import sys



class Player:


    def __init__(self, isCPU, id):

        self.name = ""
        self.pID = id
        self.cards = []
        self.isCPU = isCPU
        self.money = 2
        self.lieCount = 0

    def __str__(self):

        return "\nPlayer " + str(self.pID) + "\tbifton: " + str(self.money) +  "\t(" + str(len(self.cards)) + " cards left)\n"

    def block(self):
        return




    def steal(self ,targetNum, game):


        if game.players[targetNum].block():

            #VERFIFY
            return




        return




    def action(self, choice, game):

        if choice == "Captain":

            for i in range(len(game.players)):
                sys.stdout.write("\n("+ str(i)+ ")" + str(game.players[i]))

            playerNum = input("From whom would you like to steal ? ")

            self.steal(int(playerNum))



    def play(self, game):

        tmpOption = []



        honestOptions = "\n Options : \n"
        honestOptions += "(0) take 2 \t"

        for i in range(len(self.cards)):
            tmpOption.append(self.cards[i])
            honestOptions += "\t (" + str(i + 1) +  ") " + str(self.cards[i])


        honestOption = input(honestOptions)

        if honestOption == "0":
            self.money += 2
            return

        self.action(tmpOption[int(honestOption)-1].ctype, game)




        # self.lieCount += 1
        # return



















