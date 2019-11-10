#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: patrick vermillion
"""

from random import shuffle

"""
Define card types through dictionary
"""
CARDS = {"A": 11, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10}
SHOE_SIZE = 1
"""
Variable for triggering when the game is over (No more cards in shoe)
"""
GAME_OVER = False


class Card(object):
    """
    For playing cards containing both a name (rank and suit) and a value (1 - 11)
    """
    def __init__(self, rank, suit, value):
        self.rank = rank
        self.suit = suit
        self.value = value
        
    def __str__(self): 
        """
        Print card name directly
        """
        return "%s %s" % (self.rank, self.suit)        
    
    
class Shoe(object):
    """
    Consists 6 playing decks
    """
    def __init__(self):
        self.count = 0
        self.count_history = []
        self.ideal_count = {}
        self.cards = self.initialize_cards()
        self.initialize_count()
        
    """
    Print out all cards in the shoe
    """
    def __str__(self):
        shoe = ""
        for card in self.cards:
            shoe += "%s\n" % card
        return shoe
    
    def initialize_cards(self):
        """
        Set up the shoe with a full set of 6 playing card decks
        """
        self.count = 0
        self.count_history.append(self.count)
        
        cards = []
        for deck in range(SHOE_SIZE): 
            """
            There must be 6 decks in the shoe
            """
            for card in CARDS:
                """
                Add suits to each card
                """
                cards.append(Card(card, "Diamonds", CARDS[card]))
                cards.append(Card(card, "Clubs", CARDS[card]))
                cards.append(Card(card, "Hearts", CARDS[card]))
                cards.append(Card(card, "Spades", CARDS[card]))       
        shuffle(cards)
        return cards
    
    def initialize_count(self):
        """
        Track number of cards throught the program
        """
        for card in CARDS:
            self.ideal_count[card] = 4 * SHOE_SIZE # 4 of each card * shoe size
    
    def deal(self):
        """
        Pulls next card off top of the shoe, if shoe is empty then program ends
        """
        if self.cards:
            card = self.cards.pop()
            """
            Check wether there are any copies of that card left
            """
            assert self.ideal_count[card.rank] > 0, "Error, no more of that card"
            self.ideal_count[card.rank] -= 1
            return card
        else:
            global GAME_OVER 
            GAME_OVER = True
    
    def length(self):
        return len(self.cards)
    
    
class Hand(object):
    """
    Both player and dealer will have a playing hand
    """
    _value = 0
    _aces = []
    _soft_aces = 0
    
    def __init__(self, cards):
        self.cards = cards
        
    def __str__(self):
        hand = ""
        for card in self.cards:
            hand += "%s " % card
        return hand
    
    @property
    def aces(self):
        """
        Returns any aces in hand
        """
        self._aces = []
        for card in self.cards:
            if card.rank == "A":
                self._aces.append(card)
        return self._aces
    
    @property
    def soft_aces(self):
        """
        Returns any soft aces (Aces valued at 11)
        """
        self._soft_aces = 0
        for ace in self.aces:
            if ace.value == 11:
                self._soft_aces += 1
        return self._soft_aces
    
    @property
    def value(self):
        """
        Will return value of cards in hand
        """
        self._value = 0
        if self.cards:
            for card in self.cards:
                if card:
                    self._value += card.value
                else:
                    break
                
            if self._value > 21 and self.soft_aces > 0:
                for ace in self.aces:
                    if ace.value == 11:
                        self._value -= 10
                        ace.value = 1
                        if self._value <= 21:
                            break
            return self._value
        else:
            global GAME_OVER 
            GAME_OVER = True
    
    def add_card(self, card):
        """
        Add a card to given hand
        """
        self.cards.append(card)
        
    def soft(self):
        """
        Figures out if hand is soft
        """
        if self.soft_aces > 0:
            return True
        else:
            return False
        
    def busted(self):
        """
        Check's to see if hand's value goes over 21
        """
        if self.value == None:
            global GAME_OVER
            GAME_OVER = True
        else:
            if self.value > 21:
                return True
            else:
                return False
        
    def length(self):
        """
        Determines how many cards are in hand
        """
        return len(self.cards)
    
    
class Player(object):
    def __init__(self, hand = None, dealer_hand = None):
        self.hands = hand
        self.dealer_hand = dealer_hand
        
    def play_hand(self, hand, shoe):
        if hand.length() < 2:
            if hand.cards[0].name == "A":
                hand.cards[0].value = 11
            self.hit(hand, shoe)
        """
        Player will always hit as long as hand isn't busted 
        and the players hand value is less than 16
        """
        while not hand.busted() and hand.value < 16 and not GAME_OVER:
            self.hit(hand, shoe)
            
    def set_hands(self, new_hand, new_dealer_hand):
        """
        Sets new player and dealer hand
        """
        self.hands = [new_hand]
        self.dealer_hand = new_dealer_hand
        
    def play(self, shoe):
        """
        Depends on play_hand method
        """
        for hand in self.hands:
            self.play_hand(hand, shoe)
            
    def hit(self, hand, shoe):
        """
        Player adds a card to hand from shoe
        """
        card = shoe.deal()
        hand.add_card(card)   
    
    
class Dealer(object):     
    def __init__(self, hand = None, player_hand = None):
        self.hand = hand
        self.player_hand = player_hand
        
    def set_hand(self, new_hand):
        self.hand = new_hand
                
    def hit(self, shoe):
        card = shoe.deal()
        self.hand.add_card(card)
        
    def check_player_hand(self, player_final_hand):
        self.player_hand = player_final_hand
        return self.player_hand
        
    def play(self, shoe, player_final_hand):
        """
        Dealer will continue to play until they beat player or bust or not enough cards to play
        Not certain on logic here
        """
        if player_final_hand <= 21:
            while not (self.hand.busted()) and self.hand.value < player_final_hand and not GAME_OVER:  
                self.hit(shoe)

           
class Game(object):
    """
    Manages the order of games and logging
    """
    def __init__(self):
        self.shoe = Shoe()
        self.player = Player()
        self.dealer = Dealer()
        self.wins = 0
        self.loses = 0
        self.winning_hands = []
        
    """
    Checks who won the round
    """
    def won_or_lost(self, hand):
        win = 0
        if hand.busted():
            win = -1
        else:
            if self.dealer.hand.busted():
                win = 1
            elif self.dealer.hand.value < hand.value:
                win = 1
            elif self.dealer.hand.value > hand.value:
                win = -1
            elif self.dealer.hand.value == hand.value:
                win = 0
        return win
    
    def play_round(self):
        player_hand = Hand([self.shoe.deal(), self.shoe.deal()])
        dealer_hand = Hand([self.shoe.deal()])

        if not GAME_OVER:
            self.player.set_hands(player_hand, dealer_hand)
            self.dealer.set_hand(dealer_hand)
            
            self.player.play(self.shoe)
            self.dealer_check = self.dealer.check_player_hand(player_hand).value
            self.dealer.play(self.shoe, self.dealer_check)
            
            print("Player Hand: " + str(player_hand) + "= " + str(player_hand.value))
            print("Dealer Hand: " + str(dealer_hand) + "= " + str(dealer_hand.value))
                    
            """
            Keep track of wins/loses
            """
            for hand in self.player.hands:
                if self.won_or_lost(hand) == 1:
                    self.wins += 1
                    print("Result: Player wins!\n")
                    self.winning_hands.append(player_hand.value)
                elif self.won_or_lost(hand) == -1:
                    self.loses += 1
                    print("Result: Dealer wins!\n")
                else:
                    print("Result: It's a tie...\n")  
            return self.wins, self.loses
    
    def get_wins(self):
        return self.wins
    
    def get_winning_hands(self):
        return self.winning_hands
    
    def log_winning_hands(self, winning_hands):
        self._21 = 0
        self._20 = 0
        self._19 = 0
        self._18 = 0
        self._17 = 0
        self._16 = 0
        
        """
        Add up winning values
        """
        for hand in winning_hands:
            if hand == 21:
                self._21 += 1
            if hand == 20:
                self._20 += 1
            if hand == 19:
                self._19 += 1
            if hand == 18:
                self._18 += 1
            if hand == 17:
                self._17 += 1
            if hand == 16:
                self._16 += 1
                
        """
        Print winning values out
        """
        print("Player Winning Hand => # of times achieved")
        print("21 => " + str(self._21))
        print("20 => " + str(self._20))
        print("19 => " + str(self._19))
        print("18 => " + str(self._18))
        print("17 => " + str(self._17))
        print("16 => " + str(self._16))
        
    
if __name__ == "__main__":
    wins = 0
    loses = 0
    number_hands = 0
    game = Game()
    number_of_games = 0
    
    while not GAME_OVER:
        game.play_round()
        number_of_games += 1
        
    print("Number of games: " + str(number_of_games) + "\n")
    print("Player Success: " + str((game.get_wins()/number_of_games)*100) + "%\n")
    game.log_winning_hands(game.winning_hands)
    
    
    
    
    
    
    
    
    
    
    
    