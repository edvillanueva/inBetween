import random

def in_between(card1, card2, in_between_card):
  ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

  player_rank1 = ranks.index(card1)
  player_rank2 = ranks.index(card2)
  in_between_rank = ranks.index(in_between_card)
  
  if player_rank1 < in_between_rank < player_rank2:
    print("The third card, {}, is between the ranks of the first two cards. You win!".format(in_between_card))
  elif in_between_rank == player_rank1 or in_between_rank == player_rank2:
    print("The third card, {}, is a tie with one of the first two cards. You lose!".format(in_between_card))
  else:
    print("The third card, {}, is not between the ranks of the first two cards. You lose!".format(in_between_card))

deck = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
random.shuffle(deck)

card1 = deck.pop(0)
card2 = deck.pop(0)

print("Your cards: {}, {}".format(card1, card2))

bet = input("Do you want to bet on the third card? Enter 'y' for yes or 'n' for no: ")

if bet == "y":
  in_between_card = deck.pop(0)
  in_between(card1, card2, in_between_card)
else:
  print("You have chosen not to bet. Game over!")
