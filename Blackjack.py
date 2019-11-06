#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: patrickvermillion
"""

from random import shuffle


# Define card types through dictionary
CARDS = {"A": 11, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10}
SHOE_SIZE = 1


"""
class Card(object):
    # For playing cards containing both a name (rank and suit) and a value (1 - 11)
    def __init__(self, rank, suit, value):
        self.name = rank + " " + suit
        self.value = value
        
    def __str__(self): # Print card name directly
        return "%s" % (self.name)
"""
class Card(object):
    # For playing cards containing both a name (rank and suit) and a value (1 - 11)
    def __init__(self, rank, suit, value):
        self.rank = rank
        self.suit = suit
        self.value = value
        
    def __str__(self): # Print card name directly
        return "%s %s" % (self.rank, self.suit)        
    
class Shoe(object):
    # Consists 6 playing decks
    def __init__(self):
        self.count = 0
        self.count_history = []
        self.ideal_count = {}
        self.cards = self.initialize_cards()
        self.initialize_count()
        
    # Print out all cards in the shoe
    def __str__(self):
        shoe = ""
        for card in self.cards:
            shoe += "%s\n" % card
        return shoe
    
    def initialize_cards(self):
        # Set up the shoe with a full set of 6 playing card decks
        self.count = 0
        self.count_history.append(self.count)
        
        cards = []
        for deck in range(SHOE_SIZE): # There must be 6 decks in the shoe
            for card in CARDS:
                # Add suits to each card
                cards.append(Card(card, "Diamonds", CARDS[card]))
                cards.append(Card(card, "Clubs", CARDS[card]))
                cards.append(Card(card, "Hearts", CARDS[card]))
                cards.append(Card(card, "Spades", CARDS[card]))       
        shuffle(cards)
        return cards
    
    def initialize_count(self):
        # Track number of cards throught the program
        for card in CARDS:
            self.ideal_count[card] = 4 * SHOE_SIZE # 4 of each card * shoe size
    
    def deal(self):
        # Pulls next card off top of the shoe, if shoe is empty then program ends
        card = self.cards.pop()
        
        # Check wether there are any copies of that card left
        assert self.ideal_count[card.rank] > 0, "Error, no more of that card"
        self.ideal_count[card.rank] -= 1
        
        return card
    
class Hand(object):
    # Both player and dealer will have a playing hand
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
        # Returns any aces in hand
        self._aces = []
        for card in self.cards:
            if card.name == "A":
                self._aces.append(card)
        return self._aces
    
    @property
    def soft_aces(self):
        # Returns any soft aces (Aces valued at 11)
        self._soft_aces = 0
        for ace in self.aces:
            if ace.value == 11:
                self._soft_aces += 1
        return self._soft_aces
    
    @property
    def value(self):
        # Will return value of cards in hand
        self._value = 0
        for card in self.cards:
            self._value += card.value
            
        if self._value > 21 and self.soft_aces > 0:
            for ace in self.aces:
                if ace.value == 11:
                    self._value -= 10
                    ace.value = 1
                    if self._value <= 21:
                        break
        return self._value
    
    def add_card(self, card): #TODO: Fix GitHub bug #16
        # Add a card to given hand
        self.cards.append(card)
        
    def soft(self):
        # Figures out if hand is soft
        if self.soft_aces > 0:
            return True
        else:
            return False
        
    def busted(self):
        # Check's to see if hand's value goes over 21
        if self.value > 21:
            return True
        else:
            return False
        
    def length(self):
        # Determines how many cards are in hand
        return len(self.cards)
    
class Player(object):
    def __init__(self, hand = None, dealer_hand = None):
        self.hands = [hand]
        self.dealer_hand = dealer_hand
        
    def play_hand(self, hand, shoe):
        if hand.length() < 2:
            if hand.cards[0].name == "A":
                hand.cards[0].value = 11
            self.hit(hand, shoe)
            
    def set_hands(self, new_hand, new_dealer_hand):
        # Sets new player and dealer hand
        self.hands [new_hand]
        self.dealer_hand = [new_dealer_hand]
    
class Dealer(object):     
    def __init__(self, hand = None):
        self.hand = hand
    

# Test to make sure deck is generated properly
# Test to make sure deck is suffled properly
# Test to make sure deal functions properly
test_shoe = Shoe()

print(test_shoe)

for card in test_shoe.cards:
    print(len(test_shoe.cards))
    print(test_shoe.deal())
    
for card in test_shoe.cards:
    print(len(test_shoe.cards))
    print(test_shoe.deal())    
    
for card in test_shoe.cards:
    print(len(test_shoe.cards))
    print(test_shoe.deal())  
    
for card in test_shoe.cards:
    print(len(test_shoe.cards))
    print(test_shoe.deal())
    
print(len(test_shoe.cards))
print(test_shoe.deal())

print(len(test_shoe.cards))
print(test_shoe.deal())

print(len(test_shoe.cards))
print(test_shoe.deal())

print(len(test_shoe.cards))


print("Hello Blackjack!")

