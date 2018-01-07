##############################################################################
####This should be the digital version of the classic boardgame: Monopoly.####
##############################################################################
#Make it for 1 player first, or start development with multiple players?

##############################################################################
import math

ActivePlayer = 'None'
##############################################################################
#Make a wait() function with a configurable parameter, like: wait(1) or wait(2).
#Source: https://www.pythoncentral.io/pythons-time-sleep-pause-wait-sleep-stop-your-code/
def wait(sec):
    time.sleep(sec)

def test_wait():
    print('1')
    wait(1)
    print('2')
    wait(2)
    print('3')
    wait(3)

#test_wait()

##############################################################################

def basic_money_function():
    global MONEY
    print(you have , MONEY, money)
    print(What do you want to do with the money?)
    print(1. Give)
    print(2. Take)

    answer = input().lower()
    if answer == '1':
        MONEY -= 100
        answer = 'none'
        basic_money_function()
    elif answer == '2':
        MONEY += 100
        answer = 'none'
        basic_money_function()
    else:
        print(Okay, no transactions then.)
        #this function call is not needed in the long run, can be deleted.
        #it may be replaced with a return?
        basic_money_function()

#basic_money_function()

##############################################################################

#This class will create the players, instead of player_registration_v1:
#source: https://jeffknupp.com/blog/2014/06/18/improve-your-python-python-classes-and-object-oriented-programming/
class Player(object):
  money = 100
  position = 0
  in_jail = False
  owned_properties = []

  def __init__(self, name, token):
    self.name = name
    self.token = token

#Let's make a player name maker, that uses user input to make class insts.

Player1_input_name = input(Player1, Please enter your name:)
Player1_input_token = input(Player1, Please select a token:)

Player2_input_name = input(Player2, Please enter your name:)
Player2_input_token = input(Player2, Please select a token:)

Player3_input_name = input(Player3, Please enter your name:)
Player3_input_token = input(Player3, Please select a token:)

Player4_input_name = input(Player4, Please enter your name:)
Player4_input_token = input(Player4, Please select a token:)

Player1 = Player(Player1_input_name,Player1_input_token)
Player2 = Player(Player2_input_name,Player2_input_token)
Player3 = Player(Player3_input_name,Player3_input_token)
Player4 = Player(Player4_input_name,Player4_input_token)

print(Player1.name, Player1.token)
print(Player2.name, Player2.token)
print(Player3.name, Player3.token)
print(Player4.name, Player4.token)


#remove last item from the dict, until number_of_players number of players remain.
#Source: https://www.tutorialspoint.com/python3/python_lists.htm

#racecar
#iron
#top_hat

#-> basic_money_function is not needed anymore?/needs to be modified?

##############################################################################
#This is a dice throw, it gives us a random number from a normal, 6-sided dice.
#Source: http://www.pythonforbeginners.com/random/how-to-use-the-random-module-in-python
def dice_roll():
    from random import randint
    result = (randint(1,6))
    return(result)

#It can be used like this, thanks to the return() at the end.
#print('I will go forward', dice_roll(), 'steps.')
# This will actually change the position of the player: position = position + dice_roll()
##############################################################################
##############################################################################
##############################################################################
#Position loop:
#it should tell the player that 'you are on square (position).' before and after a roll.
#Winner: make a list out of players in the game, if only one remains, wins.

active_player = 'initial_none'

##############################################################################
####This should be the digital version of the classic boardgame: Monopoly.####
##############################################################################
#Make it for 1 player first, or start development with multiple players?

##############################################################################
import math

ActivePlayer = 'None'
##############################################################################
#Make a wait() function with a configurable parameter, like: wait(1) or wait(2).
#Source: https://www.pythoncentral.io/pythons-time-sleep-pause-wait-sleep-stop-your-code/
def wait(sec):
    time.sleep(sec)

def test_wait():
    print('1')
    wait(1)
    print('2')
    wait(2)
    print('3')
    wait(3)

#test_wait()

##############################################################################

def basic_money_function():
    global MONEY
    print(you have , MONEY, money)
    print(What do you want to do with the money?)
    print(1. Give)
    print(2. Take)

    answer = input().lower()
    if answer == '1':
        MONEY -= 100
        answer = 'none'
        basic_money_function()
    elif answer == '2':
        MONEY += 100
        answer = 'none'
        basic_money_function()
    else:
        print(Okay, no transactions then.)
        #this function call is not needed in the long run, can be deleted.
        #it may be replaced with a return?
        basic_money_function()

#basic_money_function()

##############################################################################

#This class will create the players, instead of player_registration_v1:
#source: https://jeffknupp.com/blog/2014/06/18/improve-your-python-python-classes-and-object-oriented-programming/
class Player(object):
  money = 100
  position = 0
  in_jail = False
  owned_properties = []

  def __init__(self, name, token):
    self.name = name
    self.token = token

#Let's make a player name maker, that uses user input to make class insts.

Player1_input_name = input(Player1, Please enter your name:)
Player1_input_token = input(Player1, Please select a token:)

Player2_input_name = input(Player2, Please enter your name:)
Player2_input_token = input(Player2, Please select a token:)

Player3_input_name = input(Player3, Please enter your name:)
Player3_input_token = input(Player3, Please select a token:)

Player4_input_name = input(Player4, Please enter your name:)
Player4_input_token = input(Player4, Please select a token:)

Player1 = Player(Player1_input_name,Player1_input_token)
Player2 = Player(Player2_input_name,Player2_input_token)
Player3 = Player(Player3_input_name,Player3_input_token)
Player4 = Player(Player4_input_name,Player4_input_token)

print(Player1.name, Player1.token)
print(Player2.name, Player2.token)
print(Player3.name, Player3.token)
print(Player4.name, Player4.token)


#remove last item from the dict, until number_of_players number of players remain.
#Source: https://www.tutorialspoint.com/python3/python_lists.htm

#racecar
#iron
#top_hat

#-> basic_money_function is not needed anymore?/needs to be modified?

##############################################################################
#This is a dice throw, it gives us a random number from a normal, 6-sided dice.
#Source: http://www.pythonforbeginners.com/random/how-to-use-the-random-module-in-python
def dice_roll():
    from random import randint
    result = (randint(1,6))
    return(result)

#It can be used like this, thanks to the return() at the end.
#print('I will go forward', dice_roll(), 'steps.')
# This will actually change the position of the player: position = position + dice_roll()
##############################################################################
##############################################################################
##############################################################################
#Position loop:
#it should tell the player that 'you are on square (position).' before and after a roll.
#Winner: make a list out of players in the game, if only one remains, wins.
#GIGAFUNCTION test variables: ...maybe this is not needed?
#Player1.name could be put directly inside of GIGAFUNCTION?
# P1_name  = Player1.name
# P1_money = Player1.money
# P2_name  = Player2.name
# P2_money = Player2.money
# P3_name  = Player3.name
# P3_money = Player3.money
# P4_name  = Player4.name
# P4_money = Player4.money
#active_player variables: this is the SOLUTION to the player-loop problem!!! :D
active_player_name  = Player1.name
active_player_money = Player1.money

active_field_name   = Field0.name
active_field_price  = Field0.price
######################################
#THIS WHOLE IF-ELIF branching is of NO USE!!! It can be done by variables assignment!
def GIGAFUNCTION():
  global active_player_name
  global active_player_money
  if active_player_name == Player1.name:
    print('Your turn,', active_player_name)
    active_player_name   = Player2.name
    GIGAFUNCTION()
  elif active_player_name == Player2.name:
    print('Your turn,', active_player_name)
    active_player_name   = Player3.name
    GIGAFUNCTION()
  elif active_player_name == Player3.name:
    print('Your turn,', active_player_name)
    active_player_name   = Player4.name
    GIGAFUNCTION()
  elif active_player_name == Player4.name:
    print('Your turn,', active_player_name)
    active_player_name   = Player1.name
    GIGAFUNCTION()
  else:
    pass

GIGAFUNCTION()
print('end')

##############################################################################
##############################################################################
##############################################################################
class Field(object):

  def __init__(self, name, color, price, owner, number, number_of_houses, number_of_villas):
    self.name = name
    self.color = color
    self.price = price
    self.owner = owner
    self.number = number
    self.number_of_houses = number_of_houses
    self.number_of_villas = number_of_villas

# Fold selected lines into 1 line: CTRL + SPACE
# How to:
# 'atom-workspace atom-text-editor:not([mini])':
# 'ctrl-space': 'editor:fold-selection'

Field0_inst_name  = START
Field0_inst_color = N/A
Field0_inst_price = -200
Field0_inst_owner = N/A"
Field0_inst_number = 0
Field0_inst_number_of_houses = 0
Field0_inst_number_of_villas = 0

*********************************



#MAKE ActivePlayer.money work! var needed! global var!

##############################################################################
# def Field_1():
#     global Player1
#     print(You are on, Field_1.Name)
#     if Field_1.Owner == N/A:
#         player_wants_to_buy = input(Do you want to buy it? (Y/N))
#         player_wants_to_buy.upper()
#         if player_wants_to_buy == Y and Player1.money >= Field_1.Price:
#             Player1.money = Player1.money - Field_1.Price
#             Field_1.Owner = Player1.Name
#             Player1.owned_properties.append(Field_1.Name)
#         else:
#             print(You don't want to buy, or you don't have enough money.)
#     else:
#         print(This property is already owned by someone.)
#
#     empty_useless_var = input(If you don't want to do anything, just press Enter.)

##############################################################################
# Linear control flow with consecutive functions and dice roll
# Comment keyboard shortcut in Atom: Ctrl + /
# def dice_roll(): -> this has already been done above. (row 103)
#
def Field_0():
  print('You are on Field 0')
  dice_result = dice_roll()
  # global dice_result
  # print('Throw result:',dice_result)
  # let's make dice_result = 0 just to test the below if statement:
  dice_result = 0
  if dice_result == 0:
      print(Field0.name, Field0.color, Field0.price, Field0.owner)
      if Field0.owner == N/A:
          answer = input('Do you want to buy this property? (Y/N)')
          answer = str(answer.upper())
          if answer == 'Y' and Player1.money >= Field0.price:
              Player1.money -= Field0.price
              Field0.owner = Player1.name
              print('Player 1 money:', Player1.money)
              print(Field 1's owner:, Field0.owner)
          elif answer == 'Y' and Player1.money < Field0.price:
              print('You do not have enough money.')
              #Here shold be the generic player loop
              Field_0() #This way the player gets to throw again.
          elif answer == 'N':
              Field_1()
      elif Field0_owner == Player1.name:
          print ('*You should be able to buy houses in this part*')
          Field_0() #This way the player gets to throw again.
          # This does not work this way, some more Field_N functions may be needed for this to work well.
  else:
      dice_result = dice_result - 1
      Field_1()

def Field_1():
  print('You are on Field 1')
  dice_result = dice_roll()
  # global dice_result
  print('Throw result:',dice_result)
  if dice_result == 0:
      print('*do stuff*')
  else:
      dice_result = dice_result - 1
      Field_2()

def Field_2():
  print(There is no Field_2() yet.)
#
# def Field_2():
#   print('You are on Field 2')
#   global dice_result
#   print('Throw result:',dice_result)
#   if dice_result == 0:
#       print('*do stuff*')
#   else:
#       dice_result = dice_result - 1
#       Field_3()
#
# def Field_3():
#   print('You are on Field 3')
#   global dice_result
#   print('Throw result:',dice_result)
#   if dice_result == 0:
#       print('*do stuff*')
#   else:
#       dice_result = dice_result - 1
#       Field_4()
#
# def Field_4():
#   print('You are on Field 4')
#   global dice_result
#   print('Throw result:',dice_result)
#   if dice_result == 0:
#       print('*do stuff*')
#   else:
#       dice_result = dice_result - 1
#       Field_5()
#
# def Field_5():
#   print('You are on Field 5')
#   global dice_result
#   print('Throw result:',dice_result)
#   if dice_result == 0:
#       print('*do stuff*')
#   else:
#       dice_result = dice_result - 1
#       Field_6()
#
# def Field_6():
#   print('You are on Field 6')
#   global dice_result
#   print('Throw result:',dice_result)
#   if dice_result == 0:
#       print('*do stuff*')
#   else:
#       dice_result = dice_result - 1
#       Field_1()
#
# dice_result = dice_roll()
#
# Field_0()
##############################################################################
randomcard:

card1: you win 287329783
card2: sdaasd


##############################################################################

##############################################################################

##############################################################################

##############################################################################
#THE GAME STARTS:
dice_roll()
print('The first roll of dice is:',dice_roll())
##############################################################################
print('Player1 money:' + str(Player1.money))

print(Now the player has crossed the START field, and receives 200 money)

print('Player1 money:' + str(Player1.money))



#Let's try and manipulate Player1's position through input().

print(Player1's position is  + str(Player1.position))
print(What should be the next position for Player1?)
position_input = input()
Player1.position = position_input

print(Player1's position is  + str(Player1.position))
print(Please press Enter to roll the dice for Player1)
position_input = input()
Player1.position = dice_roll()
print(Player1's position is  + str(Player1.position))
Field_0()
