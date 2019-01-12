#This is a rough copy paste from the old version, therefore it supports only two players (1 human, 1 AI),
#unlike the game itself, which could support unlimited amount of players
from Content.GameAssets import GameAssets

class ConsoleRender():
    def board(players, deck, currentBet):
        print('\n'*16)
        print("Balance:{:4}".format(players[-1].chips) + " "*50 + "Bet: {}".format(currentBet))

        #Dealer's hand
        if len(players[-1].hand) == 0:
            print("\n"*5)
        elif len(players[-1].hand) == 1:
            for row in range(0,6):
                print(end = ' '*13)
                print(f'{players[-1].hand[0].visual[row]}{GameAssets().deck_visual[row]}')
        else:
            for row in range(0,6):
                print(end = ' '*13)
                for card in players[-1].hand:
                    print(card.visual[row][:(7-2*int(len(players[-1].hand)/5))], end = '') #After each 5th card a card visual collapses by 2 chars creating a folding effect ..
                print(players[-1].hand[-1].visual[row][(7-2*int(len(players[-1].hand)/5)):])    #.. (if someone ever managed to have >14 cards in hand this would break - might add solution later)

        #Deck visual drawn here
        for row in range(0,6):
            print(end = GameAssets().deck_visual[row])
            if row == 2:
                print(end = "{:4}".format(len(deck)))
            if row == 3:
                print(end = " left")
            print("")

        #Player's hand (almost same as dealer's, dealer just gets a special visual when only 1 card in hand)
        if len(players[0].hand) == 0:
            print("\n"*5) 
        else:   
            for row in range(0,6):
                print(end = ' '*13)
                for card in players[0].hand:
                    print(card.visual[row][:(7-2*int(len(players[0].hand)/5))], end = '') #After each 5th card a card visual collapses by 2 chars creating a folding effect ..
                print(players[0].hand[-1].visual[row][(7-2*int(len(players[0].hand)/5)):])    #.. (if someone ever managed to have >14 cards in hand this would break - might add solution later)

        print("Balance:{:4}".format(players[0].chips) + "\n")