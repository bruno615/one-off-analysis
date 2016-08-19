# Let's play war

import random
import pdb

#create a deck

deck = range(1,53)

# function to translate card name
def identify_card_pretty(card_integer):
  suit = ['C','S','H','D'][int((card_integer - 1) / 13)]
  number = card_integer % 13
  if number == 0:
    number = 13
  if number > 10:
    number = ['J','Q','K','A'][number - 10]

  return (str(number)+suit)

def identify_card(card_integer):
  number = card_integer % 13
  if number == 0:
    number = 13
  if number > 10:
    pretty_number = ['J','Q','K','A'][number - 10]
  else:
    pretty_number = number
  return(number, pretty_number)

# Shuffle function

def shuffle_cards(deck):
  random.shuffle(deck)
  return deck

# Dealing cards returns (hand1, hand2).  Dealer is hand 2
def deal_cards(deck):
  cards_left = len(deck)
  hand1 = []
  hand2 = []

  # This doesn't work for more than 2 players
  while cards_left > 0:
    hand1.append(deck.pop(0))
    cards_left -= 1
    hand2.append(deck.pop(0))
    cards_left -= 1
  return(hand1, hand2)

def play_round(hand1, hand2):
  #pdb.set_trace()
  p1_card = hand1.pop(0)
  p2_card = hand2.pop(0)

  #discarded cards are random
  discard_deck = [p1_card, p2_card]
  random.shuffle(discard_deck)

  if p1_card == p2_card:
    # WAR!
    war_round(p1_card, hand1, hand2)
  elif p1_card > p2_card:
    #hand1 = hand1 + discard_deck
    hand1.append(discard_deck[0])
    hand1.append(discard_deck[1])
    print('P1 wins round. %s beats %s' % (p1_card, p2_card))
  elif p2_card > p1_card:
    #hand2 = hand2 + discard_deck
    hand2.append(discard_deck[0])
    hand2.append(discard_deck[1])
    print('P2 wins round. %s beats %s' % (p2_card, p1_card))

  # Return whether to keep playing
  if len(hand1) == 0 or len(hand2) == 0:
    return(True)
  else:
    return(False)

deck = shuffle_cards(deck = deck)

hands = deal_cards(deck = deck)

hand1 = hands[0]
hand2 = hands[1]

discard_deck1 = []
discard_deck2 = []

game_over = False
rounds_played = 0

while game_over == False:
  game_over = play_round(hand1, hand2)
  rounds_played += 1
else:
  print 'Game over after %s rounds!' % rounds_played


# let's play




