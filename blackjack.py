#Spolupráce s Fandou a Tomwm

import random

suits = ('hearts', 'diamonds', 'spades', 'clubs')
ranks = ('two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'jack',
         'queen', 'king', 'ace')
values = {'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8,
          'nine': 9, 'ten': 10, 'jack': 10, 'queen': 10, 'king': 10, 'ace': 1}


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[self.rank]

    def __str__(self):
        return self.rank + " of " + self.suit


class Deck:
    def __init__(self):

        self.all_cards = []
        for i in suits:
            for j in ranks:
                created_card = Card(i, j)
                self.all_cards.append(created_card)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop(0)


class Player:
    def __init__(self, balance=10):
        self.balance = balance
        self.all_cards = []

    def hit(self, new_card):
        self.all_cards.append(new_card)

    def win(self):
        self.balance = self.balance + int(placed_bet)
        print("YOU WON!")
        global gameon
        gameon = False

    def lose(self):
        self.balance = self.balance - int(placed_bet)
        print("You lost!")
        global gameon
        gameon = False

    def display_cards(self):
        print("")
        print("Your cards are:")
        for i in self.all_cards:
            print(i)
        print("")


class Choice:
    def __init__(self):
        self.self = self

    def place_bet(self):
        chippies = []
        for i in range(player_one.balance):
            chippies.append(str(i + 1))
        bet = 'obama is a lizard'
        while bet not in chippies or int(bet) < 1:
            bet = input("Please place a bet, you have " + str(player_one.balance) + " chips: ")
            if bet not in chippies or int(bet) < 1:
                print("Please enter a valid number")
        print("You have bet ", bet, " chips.")

        global placed_bet
        placed_bet = bet

    def action_check(self):
        free_will = True

        while free_will:
            global bust
            sum = 0
            for i in player_one.all_cards:
                sum = + i.value

            if sum > 21:
                print("")
                print("BUST")
                player_one.lose()
                print("")
                bust = True
                free_will = False
                break
            actions = ['hit', 'stand']
            cock = 'DICK'
            while cock not in actions:
                cock = input("If you want another card, type 'hit'. If you don't, type 'stand'.")
                if cock not in actions:
                    print("You have to answer by typing 'hit' or 'stand'.")

            if cock == 'hit':
                player_one.hit(new_deck.deal_one())
                player_one.display_cards()
                if player_one.all_cards[-1].rank == 'ace':
                    aces = ['1', '11']
                    mogger = 'PYTHON JE LEPSI NEZ JAVA'
                    while mogger not in aces:
                        mogger = input("Would you like your ace to be a 1 or 11?")
                        if mogger not in aces:
                            print("You need to answer using the numbers 1 or 11")
                    if mogger == '11':
                        player_one.all_cards[-1].value = 11
                    else:
                        pass
                continue
            else:
                print("Okay.")
                player_one.display_cards()
                free_will = False
                break


god = Choice()


def ace_check():
    position = 0
    for i in player_one.all_cards:
        if i.rank == 'ace':
            aces = ['1', '11']
            choice = 'penis'
            while choice not in aces:
                choice = input("Would you like your ace to be a 1 or 11? ")
                if choice not in aces:
                    print("You have to enter using the numbers 1 or 11")
            if choice == '11':
                player_one.all_cards[position].value = 11
            else:
                pass
        else:
            pass
        position += 1


def replay_choice():
    rep = 'seggs'
    yesno = ['yes', 'no']
    while rep not in yesno:
        rep = input("Would you like to play again? [yes/no]")
        if rep not in yesno:
            print("It was a yes or no question")
    if rep == 'yes':
        return True
    else:
        return False


player_one = Player()
dealer_bot = Player()

replay = True
while replay:
    bust = False
    gameon = True
    while gameon:

        if player_one.balance < 1:
            print("You're out of chips. If you don't answer 'no', we're going to be here for a long time.")
            gameon = False
            break

        god.place_bet()

        player_one.all_cards = []
        dealer_bot.all_cards = []
        new_deck = Deck()
        new_deck.shuffle()

        for i in range(2):
            player_one.all_cards.append(new_deck.deal_one())
            dealer_bot.all_cards.append(new_deck.deal_one())

        player_one.display_cards()
        ace_check()

        god.action_check()

        better = True
        while better:
            dealer_bot.all_cards.append(new_deck.deal_one())
            global sum2
            sum2 = 0
            for i in dealer_bot.all_cards:
                sum2 = sum2 + i.value

            if sum2 >= 16:
                better = False
                break
            elif sum2 > 21:
                print("")
                print("The dealer went over 21")
                print("You won!")
                player_one.win()
                better = False
                break
            else:
                continue

        if not bust:
            sum3 = 0
            for a in player_one.all_cards:
                sum3 = sum3 + a.value
            print("Your cards have a combined value of ", sum3)

            sum4 = 0
            for s in dealer_bot.all_cards:
                sum4 = sum4 + s.value

            print("The dealer's cards have a combined value of ", sum4)

            if sum3 > sum4:
                player_one.win()
                break

            elif sum4 > 21:
                print("THE DEALER WENT OVER 21!")
                player_one.win()
            elif sum3 < sum4:
                player_one.lose()
                break
            elif sum3 == sum4:
                print("TIE")
        else:
            break

    obama = replay_choice()
    if not obama:
        break
