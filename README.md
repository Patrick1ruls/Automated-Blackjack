# Automated-Blackjack

**************************************************

## Coding Challenge:

Write an object oriented program that runs an automated game of Blackjack with a shoe (collection of decks) of 6 decks of cards.  There will be a dealer and one player.  Log the results as the hands are played (example below).  After all games have been finished display: the number of games played, the player's success rate, the winning hands of the player and the number of times won by each hand, and finally a timestamp of how long it took to run through all hands.  If there are an inefficient number of cards to play the final hand, the last hand should be abandoned.  

Log Template/Example:

    Player hand: 4 Spades, 5 Spades, 10 Clubs = 19
    Dealer hand: J Hearts, K Diamonds = 20
    Result: Dealer wins!

    Player: Q Spades K Spades = 20
    Dealer: J Diamonds, 6 Clubs, 2 Diamonds, A Hearts, 5 Clubs = 24
    Result: Player wins!

  ...and so on

    Number of games: ####

    Player Success: 33.2%

    Player Winning Hand => # of times achieved
    21 => 2
    20 => 5
    19 => 2
    ...

**************************************************

## Rules:
 - Must use shoe (collection of decks) containing 6 decks of cards
 - Each card played must have a suite to let us know that individual cards identity
 - Aces may be played as 1 or 11, the Ace should be played as 11 unless this would cause Player/Dealer to bust

 Player:
 - The Player must always stay at 16 or above and hit on anything below.  

 Dealer:
 - The Dealer must hit until player hand is beaten or bust
 - If the dealer and player tie, it is just a "Push" and no one wins.

**************************************************

## Additional clarification:

The goal for blackjack is to get 21 or as close to 21 as possible.  Number cards have their face value.  Jacks, kings and queens are worth 10. Ace can be either 1 or 11 and the player who holds the ace gets to choose the value of the card. The dealer and all other players have two cards.

Deck: Every deck is made up of 4 suites: Hearts, Spades, Diamonds, and Clubs.  Each suite contains the cards A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J(ack), Q(ueen), K(ing).

Card values:
 - A: 1 or 11 (player decides)
 - 2 - 10: face value 
 - J(ack), Q(ueen), K(ing): 10

Definitions:
 - Shoe: a collection of card decks (in this case 6 decks of cards)
 - Bust: a hand greater than 21
 - Push: player and dealer hands are equal (tie)
