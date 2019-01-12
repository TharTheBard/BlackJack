class GameAssets():
    def __init__(self):
        self.ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.suits = ['clubs', 'diamonds', 'hearts', 'spades']
        self.deck_visual = [' ---- ', '|////|', '|////|', '|////|', '|////|', ' ---- ']
        self.suits_graphic = {'clubs':['()', 'oo'], 'diamonds':['/\\', '\\/'], 'hearts':['^^', '\\/'], 'spades':['/\\', 'ˇˇ']}
        self.ranks_values = {'A': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}