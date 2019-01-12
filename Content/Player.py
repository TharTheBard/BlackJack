import time

class Player:
    def __init__(self, name, chips):
        self.name = name
        self.chips = chips
        self.hand = []
        self.isActive = True

    def draw(self,gameDeck):
        self.hand.append(gameDeck.pop())
        self.hand[-1].turn()
        time.sleep(1)

    def hand_total(self):
        total = 0
        for card in self.hand:
            total += card.value
        return total

    def is_bust(self):
        return self.hand_total() > 21

    def update_aces_if_bust(self):
        if self.is_bust():
            for card in self.hand:
                if card.value == 11:
                    card.value = 1
                    break



class Human(Player):
    def bet(self, currentBet, min_player_balance):
        while True:
            try:
                amount = int(input("How much would you like to bet? "))
            except:
                print("That's not a number!")
            else:
                if (amount > min_player_balance()):
                    print("Your bet exceeds someone's balance!")
                elif amount < currentBet:
                    print("You must enter a number above current bet amount or at least call!")
                else:
                    return amount

    def hit_or_stand(self):
        result = input(f"{self.name} - Hit or Stand? (H/S)")
        while True:
            if result.upper() in ['H', 'S']:
                break
            else:
                result = input("That's not a valid input. Try again: ")
        if result.upper() == 'S':
            self.isActive = False

class Dealer(Player):
    def bet(self, currentBet, min_player_balance):
        time.sleep(1)
        print('The dealer called')
        return currentBet

    def hit_or_stand(self):
        time.sleep(1)
        if self.hand_total() > 17:
            self.isActive = False