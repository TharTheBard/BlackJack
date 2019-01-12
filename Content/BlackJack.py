import time
from random import shuffle
from Content.Card import Card
from Content.ConsoleRender import ConsoleRender
from Content.Player import Player, Human, Dealer
from Content.GameAssets import GameAssets

class BlackJack():
    def __init__(self):
        self.deck = []
        self.players = []
        self.currentBet = 0

    def run(self):
        self.generate_deck()
        self.initialize_players(1)
        while self.amount_of_players() > 1:
            self.initial_card_draws()
            self.bets()
            self.round()
            self.round_winner()
            self.eliminations()
            self.clear_players_cards()
        self.victory_message()


    def generate_deck(self):
        for suit in GameAssets().suits:
            for rank in GameAssets().ranks:
                self.deck.append(Card(rank, suit))
        shuffle(self.deck)

    def round(self):
        ConsoleRender.board(self.players, self.deck, self.currentBet)
        for player in self.players:
            player.isActive = True
        for player in self.players:
            if self.everyone_but_dealer_busted():
                break
            while True:
                player.hit_or_stand()
                if player.isActive == False:
                    break
                player.draw(self.deck)
                player.update_aces_if_bust()
                ConsoleRender.board(self.players, self.deck, self.currentBet)
                if player.is_bust():
                    player.isActive = False
                    print(f"{player.name} busted!")
                    time.sleep(1)
                    break


    def initialize_players(self, numberOfPlayers):
        for i in range(0, numberOfPlayers):
            self.players.append(Human(f'Player {i+1}', 100))
        self.players.append(Dealer('Dealer', 100))

    def bets(self):
        ConsoleRender.board(self.players, self.deck, self.currentBet)
        activePlayerIndex = 0
        self.currentBet = 10
        if self.min_player_balance() < 10 :
            self.currentBet = self.min_player_balance()
            return
        remainingBets = self.amount_of_players()
        while remainingBets > 0:
            print(f'The current bet is {self.currentBet}.')
            previousBet = self.currentBet
            self.currentBet = self.players[activePlayerIndex].bet(self.currentBet, self.min_player_balance)
            if self.currentBet > previousBet:
                remainingBets = self.amount_of_players()
            remainingBets -= 1
            activePlayerIndex = self.next_player_index(activePlayerIndex)
        for player in self.players:
            player.chips -= self.currentBet

    def next_player_index(self, currentPlayerIndex):
        return (currentPlayerIndex + 1) % self.amount_of_players()

    def amount_of_players(self):
        return len(self.players)

    def min_player_balance(self):
        playerBalances = []
        for player in self.players:
            playerBalances.append(player.chips)
        return min(playerBalances)

    def initial_card_draws(self):
        for i in range (0, self.amount_of_players()-1):
            self.players[i].draw(self.deck)
            self.players[i].draw(self.deck)
        self.players[-1].draw(self.deck)

    def clear_players_cards(self):
        for player in self.players:
            player.hand = []

    def everyone_but_dealer_busted(self):
        bustCount = 0
        for player in self.players:
            if player.is_bust():
                bustCount += 1
        return bustCount == self.amount_of_players() - 1

    def round_winner(self):
        bestHandTotal = 0
        winner = None
        for player in self.players:
            if player.hand_total() > bestHandTotal and player.is_bust() == False:
                winner = player
                bestHandTotal = player.hand_total()
        winner.chips += self.currentBet * self.amount_of_players()
        self.currentBet = 0
        print(f'{winner.name} won the round and rakes the bet!')
        time.sleep(1)

    def eliminations(self):
        loserIndexes = []
        for index, player in enumerate(self.players):
            if player.chips <= 0:
                loserIndexes.append(index)
        if len(loserIndexes) == 0:
            return
        print('Eliminations this round:')
        for index in reversed(loserIndexes):
            print(self.players[index].name)
            self.players.pop(index)
        time.sleep(1)

    def victory_message(self):
        ConsoleRender.board(self.players, self.deck, self.currentBet)
        print()
        print(f'{self.players[0].name} won the game!')