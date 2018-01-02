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
    print("you have ", MONEY, "money")
    print("What do you want to do with the money?")
    print("1. Give")
    print("2. Take")

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
        print("Okay, no transactions then.")
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

Player1_input_name = input("Player1, Please enter your name:")
Player1_input_token = input("Player1, Please select a token:")

Player2_input_name = input("Player2, Please enter your name:")
Player2_input_token = input("Player2, Please select a token:")

Player3_input_name = input("Player3, Please enter your name:")
Player3_input_token = input("Player3, Please select a token:")

Player4_input_name = input("Player4, Please enter your name:")
Player4_input_token = input("Player4, Please select a token:")

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
def dice_throw():
    from random import randint
    result = (randint(1,6))
    return(result)

#It can be used like this, thanks to the return() at the end.
#print('I will go forward', dice_throw(), 'steps.')
# This will actually change the position of the player: position = position + dice_throw()
##############################################################################
##############################################################################
##############################################################################
#Position loop:
#it should tell the player that 'you are on square (position).' before and after a roll.
#Winner: make a list out of players in the game, if only one remains, wins.

active_player = 'P1'

def GIGAFUNCTION():
  global active_player
  if active_player == Player1.name:
    print('Your turn,', active_player)
    active_player = Player2.name
    GIGAFUNCTION()
  elif active_player == Player2.name:
    print('Your turn,', active_player)
    active_player = Player3.name
    GIGAFUNCTION()
  elif active_player == Player3.name:
    print('Your turn,', active_player)
    active_player = Player4.name
    GIGAFUNCTION()
  elif active_player == Player4.name:
    print('Your turn,', active_player)
    active_player = Player1.name
    GIGAFUNCTION()
  else:
    pass

# GIGAFUNCTION()
# print('end')

##############################################################################
##############################################################################
##############################################################################
class Field(object):

  def __init__(self, name, color, price, owner):
    self.name = name
    self.color = color
    self.price = price
    self.owner = owner

# Fold selected lines into 1 line: CTRL + SPACE
# How to:
# 'atom-workspace atom-text-editor:not([mini])':
# 'ctrl-space': 'editor:fold-selection'

Field0_inst_name  = "START"
Field0_inst_color = "N/A"
Field0_inst_price = -200
Field0_inst_owner = "N/A"

Field1_inst_name  = "Mediterranean Avenue"
Field1_inst_color = "Brown"
Field1_inst_price = 60
Field1_inst_owner = "N/A"

Field2_inst_name  = "Community Chest"
Field2_inst_color = "Blue Chest"
Field2_inst_price = "N/A"
Field2_inst_owner = "N/A"

Field3_inst_name  = "Baltic Avenue"
Field3_inst_color = "Brown"
Field3_inst_price = 60
Field3_inst_owner = "N/A"

Field4_inst_name  = "Income Tax"
Field4_inst_color = "N/A"
Field4_inst_price = 200
Field4_inst_owner = "N/A"

Field5_inst_name  = "Reading Railroad"
Field5_inst_color = "N/A"
Field5_inst_price = 200
Field5_inst_owner = "N/A"

Field6_inst_name  = "Oriental Avenue"
Field6_inst_color = "Teal"
Field6_inst_price = 100
Field6_inst_owner = "N/A"

Field7_inst_name  = "Chance"
Field7_inst_color = "N/A"
Field7_inst_price = "N/A"
Field7_inst_owner = "N/A"

Field8_inst_name  = "Vermont Avenue"
Field8_inst_color = "Teal"
Field8_inst_price = 100
Field8_inst_owner = "N/A"

Field9_inst_name  = "Connecticut Avenue"
Field9_inst_color = "Teal"
Field9_inst_price = 120
Field9_inst_owner = "N/A"

Field10_inst_name  = "Just Visiting (Jail)"
Field10_inst_color = "N/A"
Field10_inst_price = "N/A"
Field10_inst_owner = "N/A"

Field11_inst_name  = "St. Charles Place"
Field11_inst_color = "Pink"
Field11_inst_price = 140
Field11_inst_owner = "N/A"

Field12_inst_name  = "Electric Company"
Field12_inst_color = "N/A"
Field12_inst_price = 150
Field12_inst_owner = "N/A"

Field13_inst_name  = "States Avenue"
Field13_inst_color = "Pink"
Field13_inst_price = 140
Field13_inst_owner = "N/A"

Field14_inst_name  = "Virginia Avenue"
Field14_inst_color = "Pink"
Field14_inst_price = 160
Field14_inst_owner = "N/A"

Field15_inst_name  = "Pennsylvania Railroad"
Field15_inst_color = "N/A"
Field15_inst_price = 200
Field15_inst_owner = "N/A"

Field16_inst_name  = "St. James Place"
Field16_inst_color = "Orange"
Field16_inst_price = 180
Field16_inst_owner = "N/A"

Field17_inst_name  = "Community Chest"
Field17_inst_color = "Blue Chest"
Field17_inst_price = "N/A"
Field17_inst_owner = "N/A"

Field18_inst_name  = "Tennessee Avenue"
Field18_inst_color = "Orange"
Field18_inst_price = 180
Field18_inst_owner = "N/A"

Field19_inst_name  = "New York Avenue"
Field19_inst_color = "Orange"
Field19_inst_price = 200
Field19_inst_owner = "N/A"

Field20_inst_name  = "Free Parking"
Field20_inst_color = "N/A"
Field20_inst_price = "N/A"
Field20_inst_owner = "N/A"

Field21_inst_name  = "Kentucky Avenue"
Field21_inst_color = "Red"
Field21_inst_price = 220
Field21_inst_owner = "N/A"

Field22_inst_name  = "Chance"
Field22_inst_color = "N/A"
Field22_inst_price = "N/A"
Field22_inst_owner = "N/A"

Field23_inst_name  = "Indiana Avenue"
Field23_inst_color = "Red"
Field23_inst_price = 220
Field23_inst_owner = "N/A"

Field24_inst_name  = "Illinois Avenue"
Field24_inst_color = "Red"
Field24_inst_price = 240
Field24_inst_owner = "N/A"

Field25_inst_name  = "B. & O. Railroad"
Field25_inst_color = "N/A"
Field25_inst_price = 200
Field25_inst_owner = "N/A"

Field26_inst_name  = "Atlantic Avenue"
Field26_inst_color = "Yellow"
Field26_inst_price = 260
Field26_inst_owner = "N/A"

Field27_inst_name  = "Ventnor Avenue"
Field27_inst_color = "Yellow"
Field27_inst_price = 260
Field27_inst_owner = "N/A"

Field28_inst_name  = "Water Works"
Field28_inst_color = "N/A"
Field28_inst_price = 150
Field28_inst_owner = "N/A"

Field29_inst_name  = "Marvin Gardens"
Field29_inst_color = "Yellow"
Field29_inst_price = 280
Field29_inst_owner = "N/A"

Field30_inst_name  = "Go To Jail"
Field30_inst_color = "N/A"
Field30_inst_price = "N/A"
Field30_inst_owner = "N/A"

Field31_inst_name  = "Pacific Avenue"
Field31_inst_color = "Green"
Field31_inst_price = 300
Field31_inst_owner = "N/A"

Field32_inst_name  = "North Carolina Avenue"
Field32_inst_color = "Green"
Field32_inst_price = 300
Field32_inst_owner = "N/A"

Field33_inst_name  = "Community Chest"
Field33_inst_color = "Blue Chest"
Field33_inst_price = "N/A"
Field33_inst_owner = "N/A"

Field34_inst_name  = "Pennsylvania Avenue"
Field34_inst_color = "Green"
Field34_inst_price = 320
Field34_inst_owner = "N/A"

Field35_inst_name  = "Short Line"
Field35_inst_color = "N/A"
Field35_inst_price = 200
Field35_inst_owner = "N/A"

Field36_inst_name  = "Chance"
Field36_inst_color = "N/A"
Field36_inst_price = "N/A"
Field36_inst_owner = "N/A"

Field37_inst_name  = "Park Place"
Field37_inst_color = "Blue"
Field37_inst_price = 350
Field37_inst_owner = "N/A"

Field38_inst_name  = "Luxury Tax"
Field38_inst_color = "N/A"
Field38_inst_price = 100
Field38_inst_owner = "N/A"

Field39_inst_name  = "Broadwalk"
Field39_inst_color = "Blue"
Field39_inst_price = 400
Field39_inst_owner = "N/A"

Field0 = Field(Field0_inst_name,  Field0_inst_color,  Field0_inst_price, Field0_inst_owner)
Field1 = Field(Field1_inst_name,  Field1_inst_color,  Field1_inst_price, Field1_inst_owner)
Field2 = Field(Field2_inst_name,  Field2_inst_color,  Field2_inst_price, Field2_inst_owner)
Field3 = Field(Field3_inst_name,  Field3_inst_color,  Field3_inst_price, Field3_inst_owner)
Field4 = Field(Field4_inst_name,  Field4_inst_color,  Field4_inst_price, Field4_inst_owner)
Field5 = Field(Field5_inst_name,  Field5_inst_color,  Field5_inst_price, Field5_inst_owner)
Field6 = Field(Field6_inst_name,  Field6_inst_color,  Field6_inst_price, Field6_inst_owner)
Field7 = Field(Field7_inst_name,  Field7_inst_color,  Field7_inst_price, Field7_inst_owner)
Field8 = Field(Field8_inst_name,  Field8_inst_color,  Field8_inst_price, Field8_inst_owner)
Field9 = Field(Field9_inst_name,  Field9_inst_color,  Field9_inst_price, Field9_inst_owner)
Field10 = Field(Field10_inst_name,  Field10_inst_color,  Field10_inst_price, Field10_inst_owner)
Field11 = Field(Field11_inst_name,  Field11_inst_color,  Field11_inst_price, Field11_inst_owner)
Field12 = Field(Field12_inst_name,  Field12_inst_color,  Field12_inst_price, Field12_inst_owner)
Field13 = Field(Field13_inst_name,  Field13_inst_color,  Field13_inst_price, Field13_inst_owner)
Field14 = Field(Field14_inst_name,  Field14_inst_color,  Field14_inst_price, Field14_inst_owner)
Field15 = Field(Field15_inst_name,  Field15_inst_color,  Field15_inst_price, Field15_inst_owner)
Field16 = Field(Field16_inst_name,  Field16_inst_color,  Field16_inst_price, Field16_inst_owner)
Field17 = Field(Field17_inst_name,  Field17_inst_color,  Field17_inst_price, Field17_inst_owner)
Field18 = Field(Field18_inst_name,  Field18_inst_color,  Field18_inst_price, Field18_inst_owner)
Field19 = Field(Field19_inst_name,  Field19_inst_color,  Field19_inst_price, Field19_inst_owner)
Field20 = Field(Field20_inst_name,  Field20_inst_color,  Field20_inst_price, Field20_inst_owner)
Field21 = Field(Field21_inst_name,  Field21_inst_color,  Field21_inst_price, Field21_inst_owner)
Field22 = Field(Field22_inst_name,  Field22_inst_color,  Field22_inst_price, Field22_inst_owner)
Field23 = Field(Field23_inst_name,  Field23_inst_color,  Field23_inst_price, Field23_inst_owner)
Field24 = Field(Field24_inst_name,  Field24_inst_color,  Field24_inst_price, Field24_inst_owner)
Field25 = Field(Field25_inst_name,  Field25_inst_color,  Field25_inst_price, Field25_inst_owner)
Field26 = Field(Field26_inst_name,  Field26_inst_color,  Field26_inst_price, Field26_inst_owner)
Field27 = Field(Field27_inst_name,  Field27_inst_color,  Field27_inst_price, Field27_inst_owner)
Field28 = Field(Field28_inst_name,  Field28_inst_color,  Field28_inst_price, Field28_inst_owner)
Field29 = Field(Field29_inst_name,  Field29_inst_color,  Field29_inst_price, Field29_inst_owner)
Field30 = Field(Field30_inst_name,  Field30_inst_color,  Field30_inst_price, Field30_inst_owner)
Field31 = Field(Field31_inst_name,  Field31_inst_color,  Field31_inst_price, Field31_inst_owner)
Field32 = Field(Field32_inst_name,  Field32_inst_color,  Field32_inst_price, Field32_inst_owner)
Field33 = Field(Field33_inst_name,  Field33_inst_color,  Field33_inst_price, Field33_inst_owner)
Field34 = Field(Field34_inst_name,  Field34_inst_color,  Field34_inst_price, Field34_inst_owner)
Field35 = Field(Field35_inst_name,  Field35_inst_color,  Field35_inst_price, Field35_inst_owner)
Field36 = Field(Field36_inst_name,  Field36_inst_color,  Field36_inst_price, Field36_inst_owner)
Field37 = Field(Field37_inst_name,  Field37_inst_color,  Field37_inst_price, Field37_inst_owner)
Field38 = Field(Field38_inst_name,  Field38_inst_color,  Field38_inst_price, Field38_inst_owner)
Field39 = Field(Field39_inst_name,  Field39_inst_color,  Field39_inst_price, Field39_inst_owner)

print(Field0.name, Field0.color, Field0.price, Field0.owner)
print(Field1.name, Field1.color, Field1.price, Field1.owner)
print(Field2.name, Field2.color, Field2.price, Field2.owner)
print(Field3.name, Field3.color, Field3.price, Field3.owner)
print(Field4.name, Field4.color, Field4.price, Field4.owner)
print(Field5.name, Field5.color, Field5.price, Field5.owner)
print(Field6.name, Field6.color, Field6.price, Field6.owner)
print(Field7.name, Field7.color, Field7.price, Field7.owner)
print(Field8.name, Field8.color, Field8.price, Field8.owner)
print(Field9.name, Field9.color, Field9.price, Field9.owner)
print(Field10.name, Field10.color, Field10.price, Field10.owner)
print(Field11.name, Field11.color, Field11.price, Field11.owner)
print(Field12.name, Field12.color, Field12.price, Field12.owner)
print(Field13.name, Field13.color, Field13.price, Field13.owner)
print(Field14.name, Field14.color, Field14.price, Field14.owner)
print(Field15.name, Field15.color, Field15.price, Field15.owner)
print(Field16.name, Field16.color, Field16.price, Field16.owner)
print(Field17.name, Field17.color, Field17.price, Field17.owner)
print(Field18.name, Field18.color, Field18.price, Field18.owner)
print(Field19.name, Field19.color, Field19.price, Field19.owner)
print(Field20.name, Field20.color, Field20.price, Field20.owner)
print(Field21.name, Field21.color, Field21.price, Field21.owner)
print(Field22.name, Field22.color, Field22.price, Field22.owner)
print(Field23.name, Field23.color, Field23.price, Field23.owner)
print(Field24.name, Field24.color, Field24.price, Field24.owner)
print(Field25.name, Field25.color, Field25.price, Field25.owner)
print(Field26.name, Field26.color, Field26.price, Field26.owner)
print(Field27.name, Field27.color, Field27.price, Field27.owner)
print(Field28.name, Field28.color, Field28.price, Field28.owner)
print(Field29.name, Field29.color, Field29.price, Field29.owner)
print(Field30.name, Field30.color, Field30.price, Field30.owner)
print(Field31.name, Field31.color, Field31.price, Field31.owner)
print(Field32.name, Field32.color, Field32.price, Field32.owner)
print(Field33.name, Field33.color, Field33.price, Field33.owner)
print(Field34.name, Field34.color, Field34.price, Field34.owner)
print(Field35.name, Field35.color, Field35.price, Field35.owner)
print(Field36.name, Field36.color, Field36.price, Field36.owner)
print(Field37.name, Field37.color, Field37.price, Field37.owner)
print(Field38.name, Field38.color, Field38.price, Field38.owner)
print(Field39.name, Field39.color, Field39.price, Field39.owner)

##############################################################################
##############################################################################
##############################################################################

#MAKE ActivePlayer.money work! var needed! global var!

##############################################################################
# def Field_1():
#     global Player1
#     print("You are on", Field_1.Name)
#     if Field_1.Owner == "N/A":
#         player_wants_to_buy = input("Do you want to buy it? (Y/N)")
#         player_wants_to_buy.upper()
#         if player_wants_to_buy == "Y" and Player1.money >= Field_1.Price:
#             Player1.money = Player1.money - Field_1.Price
#             Field_1.Owner = Player1.Name
#             Player1.owned_properties.append(Field_1.Name)
#         else:
#             print("You don't want to buy, or you don't have enough money.")
#     else:
#         print("This property is already owned by someone.")
#
#     empty_useless_var = input("If you don't want to do anything, just press Enter.")

##############################################################################
# Linear control flow with consecutive functions and dice roll
# Comment keyboard shortcut in Atom: Ctrl + /
# def dice_throw(): -> this has already been done above. (row 103)
#
def Field_0():
  print('You are on Field 0')
  dice_result = dice_throw()
  # global dice_result
  # print('Throw result:',dice_result)
  # let's make dice_result = 0 just to test the below if statement:
  dice_result = 0
  if dice_result == 0:
      print(Field0.name, Field0.color, Field0.price, Field0.owner)
      if Field0.owner == "N/A":
          answer = input('Do you want to buy this property? (Y/N)')
          answer = str(answer.upper())
          if answer == 'Y' and Player1.money >= Field0.price:
              Player1.money -= Field0.price
              Field0.owner = Player1.name
              print('Player 1 money:', Player1.money)
              print("Field 1's owner:", Field0.owner)
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
  dice_result = dice_throw()
  # global dice_result
  print('Throw result:',dice_result)
  if dice_result == 0:
      print('*do stuff*')
  else:
      dice_result = dice_result - 1
      Field_2()

def Field_2():
  print("There is no Field_2() yet.")
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
# dice_result = dice_throw()
#
# Field_0()
##############################################################################

##############################################################################

##############################################################################

##############################################################################

##############################################################################
#THE GAME STARTS:
dice_throw()
print('The first roll of dice is:',dice_throw())
##############################################################################
print('Player1 money:' + str(Player1.money))

print("Now the player has crossed the START field, and receives 200 money")

print('Player1 money:' + str(Player1.money))



#Let's try and manipulate Player1's position through input().

print("Player1's position is " + str(Player1.position))
print("What should be the next position for Player1?")
position_input = input()
Player1.position = position_input

print("Player1's position is " + str(Player1.position))
print("Please press Enter to roll the dice for Player1")
position_input = input()
Player1.position = dice_throw()
print("Player1's position is " + str(Player1.position))
Field_0()
