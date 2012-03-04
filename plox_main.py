import random

class Card:
  rank = 0
  suit = "x"
  name = "Xx"

hand = []
for each in range(4):
  hand.append(Card())

board = []
for each in range(5):
  board.append(Card())

deck = []
for each in range(52):
  deck.append(Card())

deck[0].rank = 2; deck[0].suit = "d"; deck[0].name = "2d"
deck[1].rank = 3; deck[1].suit = "d"; deck[1].name = "3d"
deck[2].rank = 4; deck[2].suit = "d"; deck[2].name = "4d"
deck[3].rank = 5; deck[3].suit = "d"; deck[3].name = "5d"
deck[4].rank = 6; deck[4].suit = "d"; deck[4].name = "6d"
deck[5].rank = 7; deck[5].suit = "d"; deck[5].name = "7d"
deck[6].rank = 8; deck[6].suit = "d"; deck[6].name = "8d"
deck[7].rank = 9; deck[7].suit = "d"; deck[7].name = "9d"
deck[8].rank = 10; deck[8].suit = "d"; deck[8].name = "Td"
deck[9].rank = 11; deck[9].suit = "d"; deck[9].name = "Jd"
deck[10].rank = 12; deck[10].suit = "d"; deck[10].name = "Qd"
deck[11].rank = 13; deck[11].suit = "d"; deck[11].name = "Kd"
deck[12].rank = 14; deck[12].suit = "d"; deck[12].name = "Ad"
deck[13].rank = 2; deck[13].suit = "c"; deck[13].name = "2c"
deck[14].rank = 3; deck[14].suit = "c"; deck[14].name = "3c"
deck[15].rank = 4; deck[15].suit = "c"; deck[15].name = "4c"
deck[16].rank = 5; deck[16].suit = "c"; deck[16].name = "5c"
deck[17].rank = 6; deck[17].suit = "c"; deck[17].name = "6c"
deck[18].rank = 7; deck[18].suit = "c"; deck[18].name = "7c"
deck[19].rank = 8; deck[19].suit = "c"; deck[19].name = "8c"
deck[20].rank = 9; deck[20].suit = "c"; deck[20].name = "9c"
deck[21].rank = 10; deck[21].suit = "c"; deck[21].name = "Tc"
deck[22].rank = 11; deck[22].suit = "c"; deck[22].name = "Jc"
deck[23].rank = 12; deck[23].suit = "c"; deck[23].name = "Qc"
deck[24].rank = 13; deck[24].suit = "c"; deck[24].name = "Kc"
deck[25].rank = 14; deck[25].suit = "c"; deck[25].name = "Ac"
deck[26].rank = 2; deck[26].suit = "h"; deck[26].name = "2h"
deck[27].rank = 3; deck[27].suit = "h"; deck[27].name = "3h"
deck[28].rank = 4; deck[28].suit = "h"; deck[28].name = "4h"
deck[29].rank = 5; deck[29].suit = "h"; deck[29].name = "5h"
deck[30].rank = 6; deck[30].suit = "h"; deck[30].name = "6h"
deck[31].rank = 7; deck[31].suit = "h"; deck[31].name = "7h"
deck[32].rank = 8; deck[32].suit = "h"; deck[32].name = "8h"
deck[33].rank = 9; deck[33].suit = "h"; deck[33].name = "9h"
deck[34].rank = 10; deck[34].suit = "h"; deck[34].name = "Th"
deck[35].rank = 11; deck[35].suit = "h"; deck[35].name = "Jh"
deck[36].rank = 12; deck[36].suit = "h"; deck[36].name = "Qh"
deck[37].rank = 13; deck[37].suit = "h"; deck[37].name = "Kh"
deck[38].rank = 14; deck[38].suit = "h"; deck[38].name = "Ah"
deck[39].rank = 2; deck[39].suit = "s"; deck[39].name = "2s"
deck[40].rank = 3; deck[40].suit = "s"; deck[40].name = "3s"
deck[41].rank = 4; deck[41].suit = "s"; deck[41].name = "4s"
deck[42].rank = 5; deck[42].suit = "s"; deck[42].name = "5s"
deck[43].rank = 6; deck[43].suit = "s"; deck[43].name = "6s"
deck[44].rank = 7; deck[44].suit = "s"; deck[44].name = "7s"
deck[45].rank = 8; deck[45].suit = "s"; deck[45].name = "8s"
deck[46].rank = 9; deck[46].suit = "s"; deck[46].name = "9s"
deck[47].rank = 10; deck[47].suit = "s"; deck[47].name = "Ts"
deck[48].rank = 11; deck[48].suit = "s"; deck[48].name = "Js"
deck[49].rank = 12; deck[49].suit = "s"; deck[49].name = "Qs"
deck[50].rank = 13; deck[50].suit = "s"; deck[50].name = "Ks"
deck[51].rank = 14; deck[51].suit = "s"; deck[51].name = "As"

number_of_players = input("Enter the number of players: ")

#hard-code number of players for now, even though this comes it as input
number_of_players = 2

hand_list = [hand] * number_of_players
player_input_list = ["None"] * number_of_players

for i in range(0, number_of_players):
  player_input_list[i] = raw_input("Player %d cards: " % (i + 1))

board_input = raw_input("Board: ")

#hard-code hand_list for now
#use player_input_list later to set hand_list
#player_input_list is a text list. it will be used to sort through the deck
#list, and then populate the hand_list with actual cards from the deck, using
#player_input_list as a reference.

hand_list = [hand] * number_of_players
hand_list[0] = [deck[51], deck[38], deck[21], deck[9]] #AsAhTcJd
del deck[51]; del deck[38]; del deck[21]; del deck[9] #card removal
hand_list[1] = [deck[34], deck[22], deck[12], deck[6]] #QhKc2c8d
del deck[34]; del deck[22]; del deck[12]; del deck[6] #card removal

#this part below initiates after user says "Go!"

#generate rest of board randomly, depending on what is needed

if board[0].rank == 0:
  for i in range(0, 3):
    x = random.randrange(0, len(deck))
    board[i] = deck[x]
    del deck[x]

if board[3].rank == 0:
  x = random.randrange(0, len(deck))
  board[3] = deck[x]
  del deck[x]

x = random.randrange(0, len(deck))
board[4] = deck[x]

#generate 60 combos per player

player_combos = []
for i in range(0, number_of_players):
  combos = []
  for j in range(60):
    five_card_hand = []
    for k in range(5):
      five_card_hand.append(Card())
    combos.append(five_card_hand)
  player_combos.append(combos)

#i is player number, j is index in 60 hand list
#a/b from individual hand, c/d/e from board

def combo_builder(i, j, a, b, c, d, e):
  temp_hand = [hand_list[i][a], hand_list[i][b], board[c], board[d], board[e]]
  player_combos[i][j] = temp_hand

for i in range(0, number_of_players):
  combo_builder(i, 0, 0, 1, 0, 1, 2)
  combo_builder(i, 1, 0, 1, 0, 1, 3)
  combo_builder(i, 2, 0, 1, 0, 1, 4)
  combo_builder(i, 3, 0, 1, 0, 2, 3)
  combo_builder(i, 4, 0, 1, 0, 2, 4)
  combo_builder(i, 5, 0, 1, 0, 3, 4)
  combo_builder(i, 6, 0, 1, 1, 2, 3)
  combo_builder(i, 7, 0, 1, 1, 2, 4)
  combo_builder(i, 8, 0, 1, 1, 3, 4)
  combo_builder(i, 9, 0, 1, 2, 3, 4)
  combo_builder(i, 10, 0, 2, 0, 1, 2)
  combo_builder(i, 11, 0, 2, 0, 1, 3)
  combo_builder(i, 12, 0, 2, 0, 1, 4)
  combo_builder(i, 13, 0, 2, 0, 2, 3)
  combo_builder(i, 14, 0, 2, 0, 2, 4)
  combo_builder(i, 15, 0, 2, 0, 3, 4)
  combo_builder(i, 16, 0, 2, 1, 2, 3)
  combo_builder(i, 17, 0, 2, 1, 2, 4)
  combo_builder(i, 18, 0, 2, 1, 3, 4)
  combo_builder(i, 19, 0, 2, 2, 3, 4)
  combo_builder(i, 20, 0, 3, 0, 1, 2)
  combo_builder(i, 21, 0, 3, 0, 1, 3)
  combo_builder(i, 22, 0, 3, 0, 1, 4)
  combo_builder(i, 23, 0, 3, 0, 2, 3)
  combo_builder(i, 24, 0, 3, 0, 2, 4)
  combo_builder(i, 25, 0, 3, 0, 3, 4)
  combo_builder(i, 26, 0, 3, 1, 2, 3)
  combo_builder(i, 27, 0, 3, 1, 2, 4)
  combo_builder(i, 28, 0, 3, 1, 3, 4)
  combo_builder(i, 29, 0, 3, 2, 3, 4)
  combo_builder(i, 30, 1, 2, 0, 1, 2)
  combo_builder(i, 31, 1, 2, 0, 1, 3)
  combo_builder(i, 32, 1, 2, 0, 1, 4)
  combo_builder(i, 33, 1, 2, 0, 2, 3)
  combo_builder(i, 34, 1, 2, 0, 2, 4)
  combo_builder(i, 35, 1, 2, 0, 3, 4)
  combo_builder(i, 36, 1, 2, 1, 2, 3)
  combo_builder(i, 37, 1, 2, 1, 2, 4)
  combo_builder(i, 38, 1, 2, 1, 3, 4)
  combo_builder(i, 39, 1, 2, 2, 3, 4)
  combo_builder(i, 40, 1, 3, 0, 1, 2)
  combo_builder(i, 41, 1, 3, 0, 1, 3)
  combo_builder(i, 42, 1, 3, 0, 1, 4)
  combo_builder(i, 43, 1, 3, 0, 2, 3)
  combo_builder(i, 44, 1, 3, 0, 2, 4)
  combo_builder(i, 45, 1, 3, 0, 3, 4)
  combo_builder(i, 46, 1, 3, 1, 2, 3)
  combo_builder(i, 47, 1, 3, 1, 2, 4)
  combo_builder(i, 48, 1, 3, 1, 3, 4)
  combo_builder(i, 49, 1, 3, 2, 3, 4)
  combo_builder(i, 50, 2, 3, 0, 1, 2)
  combo_builder(i, 51, 2, 3, 0, 1, 3)
  combo_builder(i, 52, 2, 3, 0, 1, 4)
  combo_builder(i, 53, 2, 3, 0, 2, 3)
  combo_builder(i, 54, 2, 3, 0, 2, 4)
  combo_builder(i, 55, 2, 3, 0, 3, 4)
  combo_builder(i, 56, 2, 3, 1, 2, 3)
  combo_builder(i, 57, 2, 3, 1, 2, 4)
  combo_builder(i, 58, 2, 3, 1, 3, 4)
  combo_builder(i, 59, 2, 3, 2, 3, 4)