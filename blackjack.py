import random


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank['rank']} of {self.suit}"


class Deck:
    def __init__(self):
        self.cards = []
        suits = ["Hearts", "Clubs", "Diamonds", "Spades"]
        ranks = [
            {"rank": "A", "value": 11},
            {"rank": "2", "value": 2},
            {"rank": "3", "value": 3},
            {"rank": "4", "value": 4},
            {"rank": "5", "value": 5},
            {"rank": "6", "value": 6},
            {"rank": "7", "value": 7},
            {"rank": "8", "value": 8},
            {"rank": "9", "value": 9},
            {"rank": "10", "value": 10},
            {"rank": "J", "value": 10},
            {"rank": "Q", "value": 10},
            {"rank": "K", "value": 10},
        ]

        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        if len(self.cards) > 1:
            random.shuffle(self.cards)

    def dealCard(self, numCards):
        cardsDealt = []
        for i in range(numCards):
            if len(self.cards) == 0:
                return "No more cards in deck"
            card = self.cards.pop()
            cardsDealt.append(card)
        return cardsDealt


class Hand:
    def __init__(self, isDealer=False):
        # list cards in hand
        self.cards = []
        # total value of cards in hand
        self.value = 0
        # is Hand a dealer or player
        self.isDealer = isDealer

    # takes in card list from shuffled cards
    def add_card(self, card_list):
        self.cards.extend(card_list)

    def calculate_value(self):
        self.value = 0
        has_ace = False
        for card in self.cards:
            card_value = int(card.rank["value"])
            self.value += card_value
            if card.rank["rank"] == "A":
                has_ace = True
        if has_ace and self.value > 21:
            self.value -= 10

    def get_value(self):
        self.calculate_value()
        return self.value

    def is_blackjack(self):
        return self.get_value() == 21

    def displayHand(self, showAllDealerCards):
        print(f"""{"Dealer's" if self.isDealer else "Your" } hand: """)
        for index, card in enumerate(self.cards):
            if (
                index == 0
                and self.isDealer
                and not showAllDealerCards
                and not self.is_blackjack()
            ):
                print("Hidden")
            else:
                print(card)

        if not self.isDealer:
            print("Value:", self.get_value())
        print()


class Game:
    def play(self):
        game_number = 0
        games_to_play = 0

        while games_to_play <= 0:
            try:
                games_to_play = int(input("How many games would you like to play? "))
            except:
                print("You must enter a number")

        while game_number < games_to_play:
            game_number = game_number + 1

            deck = Deck()
            deck.shuffle()

            player_hand = Hand()
            dealer_hand = Hand(True)

            for i in range(2):
                player_hand.add_card(deck.dealCard(1))
                dealer_hand.add_card(deck.dealCard(1))

            print()
            print("*" * 50)
            print(f"Game {game_number} of {games_to_play}")
            player_hand.displayHand(False)
            dealer_hand.displayHand(False)

            if self.check_winner(player_hand, dealer_hand):
                continue

            choice = ""
            while player_hand.get_value() < 21 and choice not in ["s", "stand"]:
                choice = input("Please choose 'Hit' or 'Stand': ").lower()
                print()
                while choice not in ["h", "s", "hit", "stand"]:
                    choice = input("Please enter 'hit' or 'stand'").lower()
                    print()
                if choice in ["h", "hit"]:
                    player_hand.add_card(deck.dealCard(1))
                    player_hand.displayHand(False)

            if self.check_winner(player_hand, dealer_hand):
                continue

            player_hand_value = player_hand.get_value()
            dealer_hand_value = dealer_hand.get_value()

            while dealer_hand_value < 17:
                dealer_hand.add_card(deck.dealCard(1))
                dealer_hand_value = dealer_hand.get_value()

            dealer_hand.displayHand(showAllDealerCards=True)

            if self.check_winner(player_hand, dealer_hand):
                continue

            print("Final Results: ")
            print(f"Your Hand: {player_hand_value}")
            print(f"Dealer's Hand: {dealer_hand_value}")

            self.check_winner(player_hand, dealer_hand, True)

        print("Thanks for playing!")

    def check_winner(self, playerHand, dealerHand, game_over=False):
        if not game_over:
            if playerHand.get_value() > 21:
                print("You went over 21!")
                return True
            elif dealerHand.get_value() > 21:
                print("Dealer busted! You win!")
                return True
            elif dealerHand.is_blackjack() and playerHand.is_blackjack():
                print("Both players have Blackjack. It's a tie!")
                return True
            elif playerHand.is_blackjack():
                print("You have a Blackjack! You win!")
                return True
            elif dealerHand.is_blackjack():
                print("Dealer has a Blackjack! Dealer wins!")
                return True
        else:
            if playerHand.get_value() > dealerHand.get_value():
                print("You win!")
            elif dealerHand.get_value() > playerHand.get_value():
                print("Dealer wins!")
            elif dealerHand.get_value() == playerHand.get_value():
                print("It's a  tie!")
            return True
        return False


g = Game()
g.play()
