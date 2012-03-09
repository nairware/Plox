import random

#***GLOBAL VARIABLES INIT***

class Card:
  rank = 0
  suit = "x"
  name = "Xx"

hand = []
for each in range(4):
  hand.append(Card())

board_source = []
for each in range(5):
  board_source.append(Card())

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

#***USER INPUT***

number_of_players = input("Enter the number of players: ")

#hard-code number of players for now, even though this comes it as input
number_of_players = 2

hand_list = [hand] * number_of_players
player_input_list = ["None"] * number_of_players

for i in range(0, number_of_players):
  player_input_list[i] = raw_input("Player %d cards: " % (i + 1))

#hard-code hand_list for now
#use player_input_list later to set hand_list
#player_input_list is a text list. it will be used to sort through the deck
#list, and then populate the hand_list with actual cards from the deck, using
#player_input_list as a reference.
hand_list = [hand] * number_of_players
hand_list[0] = [deck[51], deck[50], deck[38], deck[37]] #AsAhTcJd
hand_list[1] = [deck[25], deck[24], deck[23], deck[22]]  #AcAd9d6d
del deck[51]; del deck[50]; del deck[38]; del deck[37]  #card removal
del deck[25]; del deck[24]; del deck[23]; del deck[22]  #card removal

board_input = raw_input("Board: ")

final_tally = [0.00] * number_of_players

#***LOOP***

number_of_trials = 500

for each in range(0, number_of_trials):

  temp_deck = deck[:]
  board = board_source

  #only works for scenario in which flop is not specified
  for i in range(5):
    x = random.randrange(0, len(temp_deck))
    board[i] = temp_deck[x]
    del temp_deck[x]
  
  #generate 60 combos per player
  unranked_combos = []
  for i in range(0, number_of_players):
    combos = []
    for j in range(60):
      five_card_hand = []
      for k in range(5):
        five_card_hand.append(Card())
      combos.append(five_card_hand)
    unranked_combos.append(combos)
  
  #i is player number, j is index in 60 hand list
  #a/b from individual hand, c/d/e from board
  def combo_builder(i, j, a, b, c, d, e):
    temp_hand = [hand_list[i][a], hand_list[i][b], board[c], board[d], board[e]]
    #sort temp_hand before building unranked_combos
    temp_hand.sort(key = lambda temp: temp.rank, reverse = True)
    unranked_combos[i][j] = temp_hand
    #attach the overall hand rank element to each combo
    unranked_combos[i][j].append(-1)
  
  #***DEFINE GLOBAL FUNCTIONS***
  
  #create function for taking 5 unsorted cards as a parameter and generating
  #a ranked player combo record with 5 sorted cards and an updated int to
  #indicate the overall rank
  def rank_hand(unranked_hand):
    #check if any pairs exist
    if (unranked_hand[0].rank == unranked_hand[1].rank or
      unranked_hand[1].rank == unranked_hand[2].rank or
      unranked_hand[2].rank == unranked_hand[3].rank or
      unranked_hand[3].rank == unranked_hand[4].rank):
      #pairs exist!
      if ((unranked_hand[0].rank == unranked_hand[1].rank and
        unranked_hand[1].rank != unranked_hand[2].rank and
        unranked_hand[2].rank != unranked_hand[3].rank and
        unranked_hand[3].rank != unranked_hand[4].rank) or
        (unranked_hand[0].rank != unranked_hand[1].rank and
        unranked_hand[1].rank == unranked_hand[2].rank and
        unranked_hand[2].rank != unranked_hand[3].rank and
        unranked_hand[3].rank != unranked_hand[4].rank) or
        (unranked_hand[0].rank != unranked_hand[1].rank and
        unranked_hand[1].rank != unranked_hand[2].rank and
        unranked_hand[2].rank == unranked_hand[3].rank and
        unranked_hand[3].rank != unranked_hand[4].rank) or
        (unranked_hand[0].rank != unranked_hand[1].rank and
        unranked_hand[1].rank != unranked_hand[2].rank and
        unranked_hand[2].rank != unranked_hand[3].rank and
        unranked_hand[3].rank == unranked_hand[4].rank)):
        unranked_hand[5] = 1
      elif ((unranked_hand[0].rank == unranked_hand[1].rank and
        unranked_hand[1].rank != unranked_hand[2].rank and
        unranked_hand[2].rank == unranked_hand[3].rank and
        unranked_hand[3].rank != unranked_hand[4].rank) or
        (unranked_hand[0].rank == unranked_hand[1].rank and
        unranked_hand[1].rank != unranked_hand[2].rank and
        unranked_hand[2].rank != unranked_hand[3].rank and
        unranked_hand[3].rank == unranked_hand[4].rank) or
        (unranked_hand[0].rank != unranked_hand[1].rank and
        unranked_hand[1].rank == unranked_hand[2].rank and
        unranked_hand[2].rank != unranked_hand[3].rank and
        unranked_hand[3].rank == unranked_hand[4].rank)):
        unranked_hand[5] = 2
      elif ((unranked_hand[0].rank == unranked_hand[1].rank and
        unranked_hand[1].rank == unranked_hand[2].rank and
        unranked_hand[2].rank != unranked_hand[3].rank and
        unranked_hand[3].rank != unranked_hand[4].rank) or
        (unranked_hand[0].rank != unranked_hand[1].rank and
        unranked_hand[1].rank == unranked_hand[2].rank and
        unranked_hand[2].rank == unranked_hand[3].rank and
        unranked_hand[3].rank != unranked_hand[4].rank) or
        (unranked_hand[0].rank != unranked_hand[1].rank and
        unranked_hand[1].rank != unranked_hand[2].rank and
        unranked_hand[2].rank == unranked_hand[3].rank and
        unranked_hand[3].rank == unranked_hand[4].rank)):
        unranked_hand[5] = 3
      elif ((unranked_hand[0].rank == unranked_hand[1].rank and
        unranked_hand[1].rank == unranked_hand[2].rank and
        unranked_hand[2].rank != unranked_hand[3].rank and
        unranked_hand[3].rank == unranked_hand[4].rank) or
        (unranked_hand[0].rank == unranked_hand[1].rank and
        unranked_hand[1].rank != unranked_hand[2].rank and
        unranked_hand[2].rank == unranked_hand[3].rank and
        unranked_hand[3].rank == unranked_hand[4].rank)):
        unranked_hand[5] = 6
      else:
        unranked_hand[5] = 7
    else:
      #pairs do not exist!
      straight_bool = False
      flush_bool = False
      if ((unranked_hand[0].rank == 14 and unranked_hand[1].rank == 5) or
        (unranked_hand[0].rank - unranked_hand[4].rank == 4)):
        straight_bool = True
      if (unranked_hand[0].suit == unranked_hand[1].suit and
        unranked_hand[1].suit == unranked_hand[2].suit and
        unranked_hand[2].suit == unranked_hand[3].suit and
        unranked_hand[3].suit == unranked_hand[4].suit):
        flush_bool = True
      if straight_bool == False and flush_bool == False:
        unranked_hand[5] = 0
      elif straight_bool == True and flush_bool == False:
        unranked_hand[5] = 4
      elif straight_bool == False and flush_bool == True:
        unranked_hand[5] = 5
      else:
        unranked_hand[5] = 8
  
  #only need to sort paired hands and straights/straight flush (consider wheel)
  def sort_hand(unranked_hand):
    #one pair
    if unranked_hand[5] == 1:
      if unranked_hand[1].rank == unranked_hand[2].rank:
        unranked_hand[0], unranked_hand[2] = unranked_hand[2], unranked_hand[0]
      elif unranked_hand[2].rank == unranked_hand[3].rank:
        unranked_hand[0], unranked_hand[2] = unranked_hand[2], unranked_hand[0]
        unranked_hand[1], unranked_hand[3] = unranked_hand[3], unranked_hand[1]
      elif unranked_hand[3].rank == unranked_hand[4].rank:
        unranked_hand[0], unranked_hand[3] = unranked_hand[3], unranked_hand[0]
        unranked_hand[1], unranked_hand[4] = unranked_hand[4], unranked_hand[1]
        unranked_hand[2], unranked_hand[3] = unranked_hand[3], unranked_hand[2]
        unranked_hand[3], unranked_hand[4] = unranked_hand[4], unranked_hand[3]
    #two pair
    elif unranked_hand[5] == 2:
      if (unranked_hand[0].rank == unranked_hand[1].rank and
        unranked_hand[3].rank == unranked_hand[4].rank):
        unranked_hand[2], unranked_hand[4] = unranked_hand[4], unranked_hand[2]
      elif (unranked_hand[1].rank == unranked_hand[2].rank and
        unranked_hand[3].rank == unranked_hand[4].rank):
        unranked_hand[0], unranked_hand[2] = unranked_hand[2], unranked_hand[0]
        unranked_hand[2], unranked_hand[4] = unranked_hand[4], unranked_hand[2]
    #trips
    elif unranked_hand[5] == 3:
      if (unranked_hand[1].rank == unranked_hand[2].rank and
        unranked_hand[2].rank == unranked_hand[3].rank):
        unranked_hand[0], unranked_hand[3] = unranked_hand[3], unranked_hand[0]
      elif (unranked_hand[2].rank == unranked_hand[3].rank and
        unranked_hand[3].rank == unranked_hand[4].rank):
        unranked_hand[0], unranked_hand[3] = unranked_hand[3], unranked_hand[0]
        unranked_hand[1], unranked_hand[4] = unranked_hand[4], unranked_hand[1]
    #straight and straight flush (wheel check)
    elif unranked_hand[5] == 4 or unranked_hand[5] == 8:
      if unranked_hand[0].rank == 14 and unranked_hand[1].rank == 5:
        unranked_hand[0], unranked_hand[1] = unranked_hand[1], unranked_hand[0]
        unranked_hand[1], unranked_hand[2] = unranked_hand[2], unranked_hand[1]
        unranked_hand[2], unranked_hand[3] = unranked_hand[3], unranked_hand[2]
        unranked_hand[3], unranked_hand[4] = unranked_hand[4], unranked_hand[3]
    #full house
    elif unranked_hand[5] == 6:
      if unranked_hand[2].rank == unranked_hand[3].rank:
        unranked_hand[0], unranked_hand[3] = unranked_hand[3], unranked_hand[0]
        unranked_hand[1], unranked_hand[4] = unranked_hand[4], unranked_hand[1]
    #quads
    else:
      if unranked_hand[3].rank == unranked_hand[4].rank:
        unranked_hand[0], unranked_hand[4] = unranked_hand[4], unranked_hand[0]
  
  #function to compare two hands, overall hand strengths unknown
  #takes two ranked/sorted 5 card hands as parameters
  #returns int: 1 for hand 1, 2 for hand 2, 0 for tie
  def compare_hands(hand1, hand2):
    if hand1[5] > hand2[5]:
      return 1
    elif hand1[5] < hand2[5]:
      return 2
    else:
      #high card/flush comparison, hand rank = 0 or 5
      if hand1[5] == 0 or hand1[5] == 5:
        if hand1[0].rank > hand2[0].rank:
          return 1
        elif hand1[0].rank < hand2[0].rank:
          return 2
        else:
          if hand1[1].rank > hand2[1].rank:
            return 1
          elif hand1[1].rank < hand2[1].rank:
            return 2
          else:
            if hand1[2].rank > hand2[2].rank:
              return 1
            elif hand1[2].rank < hand2[2].rank:
              return 2
            else:
              if hand1[3].rank > hand2[3].rank:
                return 1
              elif hand1[3].rank < hand2[3].rank:
                return 2
              else:
                if hand1[4].rank > hand2[4].rank:
                  return 1
                elif hand1[4].rank < hand2[4].rank:
                  return 2
                else:
                  return 0
      #one pair comparison, hand rank = 1
      elif hand1[5] == 1:
        if hand1[0].rank > hand2[0].rank:
          return 1
        elif hand1[0].rank < hand2[0].rank:
          return 2
        else:
          if hand1[2].rank > hand2[2].rank:
            return 1
          elif hand1[2].rank < hand2[2].rank:
            return 2
          else:
            if hand1[3].rank > hand2[3].rank:
              return 1
            elif hand1[3].rank < hand2[3].rank:
              return 2
            else:
              if hand1[4].rank > hand2[4].rank:
                return 1
              elif hand1[4].rank < hand2[4].rank:
                return 2
              else:
                return 0
      #two pair comparison, hand rank = 2
      elif hand1[5] == 2:
        if hand1[0].rank > hand2[0].rank:
          return 1
        elif hand1[0].rank < hand2[0].rank:
          return 2
        else:
          if hand1[2].rank > hand2[2].rank:
            return 1
          elif hand1[2].rank < hand2[2].rank:
            return 2
          else:
            if hand1[4].rank > hand2[4].rank:
              return 1
            elif hand1[4].rank < hand1[4].rank:
              return 2
            else:
              return 0
      #trips comparison, hand rank = 3
      elif hand1[5] == 3:
        if hand1[0].rank > hand2[0].rank:
          return 1
        elif hand1[0].rank < hand2[0].rank:
          return 2
        else:
          if hand1[3].rank > hand2[3].rank:
            return 1
          elif hand1[3].rank < hand2[3].rank:
            return 2
          else:
            if hand1[4].rank > hand2[4].rank:
              return 1
            elif hand1[4].rank < hand2[4].rank:
              return 2
            else:
              return 0
      #straight/straight flush comparison, hand rank = 4 or 8
      elif hand1[5] == 4 or hand1[5] == 8:
        if hand1[0].rank > hand2[0].rank:
          return 1
        elif hand1[0].rank < hand2[0].rank:
          return 2
        else:
          return 0
      #full house comparison, hand rank = 6
      elif hand1[5] == 6:
        if hand1[0].rank > hand2[0].rank:
          return 1
        elif hand1[0].rank < hand2[0].rank:
          return 2
        else:
          if hand1[3].rank > hand2[3].rank:
            return 1
          elif hand1[3].rank < hand2[3].rank:
            return 2
          else:
            return 0
      #quads comparison, hand rank = 7
      else:
        if hand1[0].rank > hand2[0].rank:
          return 1
        elif hand1[0].rank < hand2[0].rank:
          return 2
        else:
          if hand1[4].rank > hand2[4].rank:
            return 1
          elif hand1[4].rank < hand2[4].rank:
            return 2
          else:
            return 0
  
  #***EXECUTE RANK/SORT***
  
  #build hand combos for each player
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
  
  #rank and sort all combos for all players
  for i in range(0, number_of_players):
    for j in range(0, 60):
      rank_hand(unranked_combos[i][j])
      sort_hand(unranked_combos[i][j])
  
  #top hand array, one hand per each player
  top_hand = []
  for i in range(0, number_of_players):
    top_hand.append(unranked_combos[i][0])
  
  #find the highest rank of all 60 combos for each player
  for i in range(0, number_of_players):
    for j in range(1, 60):
      if compare_hands(unranked_combos[i][j], top_hand[i]) == 1:
        top_hand[i] = unranked_combos[i][j]
  
  #search for the strongest hand amongst the list of top hands
  #search amongst all player hands for matches with the highest hand strength
  #increment hand tallies using winning player indices
  #increment by value based on the quantity of winning player indices
  strongest_hand = top_hand[0]
  for i in range(1, number_of_players):
    if compare_hands(top_hand[i], strongest_hand) == 1:
      strongest_hand = top_hand[i]
  
  winner_indices = []
  for i in range(0, number_of_players):
    if (top_hand[i][0].rank == strongest_hand[0].rank and
      top_hand[i][1].rank == strongest_hand[1].rank and
      top_hand[i][2].rank == strongest_hand[2].rank and
      top_hand[i][3].rank == strongest_hand[3].rank and
      top_hand[i][4].rank == strongest_hand[4].rank and
      top_hand[i][5] == strongest_hand[5]):
      winner_indices.append(i)
  
  #hand tally
  hand_tally = [0.00] * number_of_players
  for i in range(0, len(winner_indices)):
    hand_tally[winner_indices[i]] = (1.00 / len(winner_indices))
  
  for i in range(0, number_of_players):
    final_tally[i] = final_tally[i] + hand_tally[i]

player_zero_percentage = (final_tally[0] / number_of_trials) * 100
player_one_percentage = (final_tally[1] / number_of_trials) * 100

print player_zero_percentage, "%"
print player_one_percentage, "%"