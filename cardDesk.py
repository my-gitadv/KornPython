# A deck of cards contains 52 cards starts from A(1) to K with
# 4 suits which are clubs (♣), diamonds (♦), hearts (♥), and spades (♠)
# A 2 3 4 5 6 7 8 9 10 J Q K
# PART 1
# Try building a new deck and print the deck.

number = ("A 2 3 4 5 6 7 8 9 10 J Q K").split()
# print('♣ ♦ ♥ ♠')
deck = []
clubs = ('♣ ♦ ♥ ♠').split()

print(number)
print(clubs)

# example => deck = ["A♣","2♣",...,"K♠"] (52 elements)


# Write your code here...
def newDeck():
  for i in clubs:
    for j in number:
      print(j + i)
      deck.append(j + i)
  return deck


# PART 2
# Shuffle the deck
import random


# write your code here...
def shuffle():
  card = random.shuffle(deck)
  return card




# PART 3

# Write a draw function that returns top of the deck, print number of the remaining card and add it to hand and dont forget to sort hand.

hand = []


def draw(n):
  # Write your code here...
  for i in range(n):
    top = deck.pop(-1)
    hand.append(top)
  # print(top)
  print(deck)

  return top



# PART 4


# Write a function that raturn cards on hand onto the deck
def handToDeck():
  global hand
  for i in hand :
    deck.append(i)
  hand = []
  return 