import random
from os import system

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace')
values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

playing = True

class Card():
    value = 0
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return f'{self.rank} of {self.suit}'

class Deck():

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                a = Card(suit, rank)
                self.deck.append(a)

    def __str__(self):
        for card in self.deck:
            return str(card)

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        self.shuffle()
        return self.deck.pop()

class Hand():
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card) # Here card is the returned object from deal method of deck class
        if card.rank == 'Ace':
            self.value += self.adjust_for_ace()
        else:
            self.value += values[card.rank]

    def adjust_for_ace(self):
        if self.value == 20:
            return 1
        else:
            return 11

class Chips():
    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet

def take_bet(chips):
    while True:
        try:
            chips.bet = int(input('Enter bet chips: '))
        except:
            print('Invalid input, Please Try again.')
            continue
        else:
            if chips.total < chips.bet:
                print('Less amount left, Try another bet.')
                continue
            else:
                break

def hit(deck, hand):
    hand.add_card(deck.deal())

def hit_or_stand(deck, hand):
    global playing
    while playing:
        choice = int(input('Do you want to hit or stand\n1 for hit/0 for stand: '))
        if choice == 1:
            hit(deck, hand)
        else:
            playing = False

def show_some(player, dealer):
    print(f"Player's Hand's Value: {player.value}")
    print(f"Dealer's Hand's Value: {dealer.value - values[dealer.cards[0].rank]}")

def show_all(player, dealer):
    print(f"Player's Hand's Value: {player.value}")
    print(f"Dealer's Hand's Value: {dealer.value}")

def player_busts(chips):
    print('You Lost')
    chips.lose_bet()

def player_wins(chips):
    print('You Win!')
    chips.win_bet()

def dealer_busts(chips):
    print('You Win!')
    chips.win_bet()

def dealer_wins(chips):
    print('You Lost')
    chips.lose_bet()

def push():
    print('Tie Game')

while True:
    system('clear')

      # Print an opening statement
    print(':::Welcome to BlackJack:::')


    # Create & shuffle the deck, deal two cards to each player
    player = Hand()
    dealer = Hand()
    deck = Deck()
    deck.shuffle()
    player.add_card(deck.deal())
    player.add_card(deck.deal())
    dealer.add_card(deck.deal())
    dealer.add_card(deck.deal())

    # Set up the Player's chips
    chip = Chips()

    # Prompt the Player for their bet
    chip.bet = int(input('Enter amount to bet: '))

    # Show cards (but keep one dealer card hidden)
    show_some(player, dealer)

    while playing:  # recall this variable from our hit_or_stand function

        # Prompt for Player to Hit or Stand
        hit_or_stand(deck, player)

        # Show cards (but keep one dealer card hidden)
        show_some(player, dealer)

        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player.value > 21:
            player_busts(chip)
            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
        while dealer.value >= 17:
            hit(deck, dealer)

        # Show all cards
        show_all(player, dealer)
        # Run different winning scenarios
        if player.value > 21:
            player_busts(chip)
        if dealer.value > 17:
            dealer_busts(chip)
        if player.value > dealer.value:
            player_wins(chip)
        else:
            dealer_wins(chip)

    # Inform Player of their chips total
    print(f'You have {chip.total} chips left.')
    # Ask to play again
    choice = int(input('Do you want to play again(1/0): '))
    if choice == 0:
        break
