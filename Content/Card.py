from Content.GameAssets import GameAssets

#Defining a Card class
class Card():
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = GameAssets().ranks_values[self.rank]
    
    #Not needed in this code
    def __str__(self):
        return f'{self.rank} of {self.suit}.'

    #Defining the card visual depending on the rank and suit - requirement for board() function
    #This is a separate method and not __init__, so the space is only allocated for the cards that are actually going to be shown
    def turn(self):
        self.visual = []
        self.visual.append(' ----  ')
        self.visual.append(f'|{self.rank}' + ' '*(4-len(self.rank))+'| ')
        self.visual.append(f'| {GameAssets().suits_graphic[self.suit][0]} | ')
        self.visual.append(f'| {GameAssets().suits_graphic[self.suit][1]} | ')
        self.visual.append('|'+' '*(4-len(self.rank))+f'{self.rank}| ')
        self.visual.append(' ----  ' )