#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: patrickvermillion
"""

class Card(object):
    # For playing cards containing both a name (rank and suit) and a value (1 - 11)
    def __init__(self, name, value):
        self.name = name
        self.value = value
        
    def __str__(self): # Print card name directly
        return "%s" % (self.name)
    
test_card = Card("K Diamonds", 10)

print("%s = %d" % (test_card, test_card.value))

print("Hello Blackjack!")
