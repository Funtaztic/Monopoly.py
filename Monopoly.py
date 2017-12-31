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

#Let's make a player name maker, that uses user input to make class instances.

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



##############################################################################
##############################################################################
##############################################################################
class Field(object):

  def __init__(self, name, color, price, owner):
    self.name = name
    self.color = color
    self.price = price
    self.owner = owner

Field0_instance_name  = "START"
Field0_instance_color = "N/A"
Field0_instance_price = -200
Field0_instance_owner = "N/A"

Field1_instance_name  = "Mediterranean Avenue"
Field1_instance_color = "Brown"
Field1_instance_price = 60
Field1_instance_owner = "N/A"

Field2_instance_name  = "Community Chest"
Field2_instance_color = "Blue Chest"
Field2_instance_price = "N/A"
Field2_instance_owner = "N/A"

Field3_instance_name  = "Baltic Avenue"
Field3_instance_color = "Brown"
Field3_instance_price = 60
Field3_instance_owner = "N/A"

Field4_instance_name  = "Income Tax"
Field4_instance_color = "N/A"
Field4_instance_price = 200
Field4_instance_owner = "N/A"

Field5_instance_name  = "Reading Railroad"
Field5_instance_color = "N/A"
Field5_instance_price = 200
Field5_instance_owner = "N/A"

Field6_instance_name  = "Oriental Avenue"
Field6_instance_color = "Teal"
Field6_instance_price = 100
Field6_instance_owner = "None"

Field7_instance_name  = "Chance"
Field7_instance_color = "N/A"
Field7_instance_price = "N/A"
Field7_instance_owner = "N/A"

Field8_instance_name  = "Vermont Avenue"
Field8_instance_color = "Teal"
Field8_instance_price = 100
Field8_instance_owner = "None"

Field9_instance_name  = "Connecticut Avenue"
Field9_instance_color = "Teal"
Field9_instance_price = 120
Field9_instance_owner = "None"

Field10_instance_name  = "Just Visiting (Jail)"
Field10_instance_color = "N/A"
Field10_instance_price = "N/A"
Field10_instance_owner = "N/A"

Field11_instance_name  = "St. Charles Place"
Field11_instance_color = "Pink"
Field11_instance_price = 140
Field11_instance_owner = "None"

Field12_instance_name  = "Electric Company"
Field12_instance_color = "N/A"
Field12_instance_price = 150
Field12_instance_owner = "None"

Field13_instance_name  = "States Avenue"
Field13_instance_color = "Pink"
Field13_instance_price = 140
Field13_instance_owner = "None"

Field14_instance_name  = "Virginia Avenue"
Field14_instance_color = "Pink"
Field14_instance_price = 160
Field14_instance_owner = "None"

Field15_instance_name  = "Pennsylvania Railroad"
Field15_instance_color = "N/A"
Field15_instance_price = 200
Field15_instance_owner = "None"

Field16_instance_name  = "St. James Place"
Field16_instance_color = "Orange"
Field16_instance_price = 180
Field16_instance_owner = "None"

Field17_instance_name  = "Community Chest"
Field17_instance_color = "Blue Chest"
Field17_instance_price = "N/A"
Field17_instance_owner = "N/A"

Field18_instance_name  = "Tennessee Avenue"
Field18_instance_color = "Orange"
Field18_instance_price = 180
Field18_instance_owner = "None"

Field19_instance_name  = "New York Avenue"
Field19_instance_color = "Orange"
Field19_instance_price = 200
Field19_instance_owner = "None"

Field20_instance_name  = "Free Parking"
Field20_instance_color = "N/A"
Field20_instance_price = "N/A"
Field20_instance_owner = "N/A"

Field21_instance_name  = "Kentucky Avenue"
Field21_instance_color = "Red"
Field21_instance_price = 220
Field21_instance_owner = "None"

Field22_instance_name  = "Chance"
Field22_instance_color = "N/A"
Field22_instance_price = "N/A"
Field22_instance_owner = "N/A"

Field23_instance_name  = "Indiana Avenue"
Field23_instance_color = "Red"
Field23_instance_price = 220
Field23_instance_owner = "None"

Field24_instance_name  = "Illinois Avenue"
Field24_instance_color = "Red"
Field24_instance_price = 240
Field24_instance_owner = "None"

Field25_instance_name  = "B. & O. Railroad"
Field25_instance_color = "N/A"
Field25_instance_price = 200
Field25_instance_owner = "None"

Field26_instance_name  = "Atlantic Avenue"
Field26_instance_color = "Yellow"
Field26_instance_price = 260
Field26_instance_owner = "None"

Field27_instance_name  = "Ventnor Avenue"
Field27_instance_color = "Yellow"
Field27_instance_price = 260
Field27_instance_owner = "None"

Field28_instance_name  = "Water Works"
Field28_instance_color = "N/A"
Field28_instance_price = 150
Field28_instance_owner = "None"

Field29_instance_name  = "Marvin Gardens"
Field29_instance_color = "Yellow"
Field29_instance_price = 280
Field29_instance_owner = "None"

Field30_instance_name  = "Go To Jail"
Field30_instance_color = "N/A"
Field30_instance_price = "N/A"
Field30_instance_owner = "N/A"

Field31_instance_name  = "Pacific Avenue"
Field31_instance_color = "Green"
Field31_instance_price = 300
Field31_instance_owner = "None"

Field32_instance_name  = "North Carolina Avenue"
Field32_instance_color = "Green"
Field32_instance_price = 300
Field32_instance_owner = "None"

Field33_instance_name  = "Community Chest"
Field33_instance_color = "Blue Chest"
Field33_instance_price = "N/A"
Field33_instance_owner = "N/A"

Field34_instance_name  = "Pennsylvania Avenue"
Field34_instance_color = "Green"
Field34_instance_price = 320
Field34_instance_owner = "None"

Field35_instance_name  = "Short Line"
Field35_instance_color = "N/A"
Field35_instance_price = 200
Field35_instance_owner = "None"

Field36_instance_name  = "Chance"
Field36_instance_color = "N/A"
Field36_instance_price = "N/A"
Field36_instance_owner = "N/A"

Field37_instance_name  = "Park Place"
Field37_instance_color = "Blue"
Field37_instance_price = 350
Field37_instance_owner = "None"

Field38_instance_name  = "Luxury Tax"
Field38_instance_color = "N/A"
Field38_instance_price = 100
Field38_instance_owner = "N/A"

Field39_instance_name  = "Broadwalk"
Field39_instance_color = "Blue"
Field39_instance_price = 400
Field39_instance_owner = "None"

Field0 = Field(Field0_instance_name,  Field0_instance_color,  Field0_instance_price, Field0_instance_owner)
Field1 = Field(Field1_instance_name,  Field1_instance_color,  Field1_instance_price, Field1_instance_owner)
Field2 = Field(Field2_instance_name,  Field2_instance_color,  Field2_instance_price, Field2_instance_owner)
Field3 = Field(Field3_instance_name,  Field3_instance_color,  Field3_instance_price, Field3_instance_owner)
Field4 = Field(Field4_instance_name,  Field4_instance_color,  Field4_instance_price, Field4_instance_owner)
Field5 = Field(Field5_instance_name,  Field5_instance_color,  Field5_instance_price, Field5_instance_owner)
Field6 = Field(Field6_instance_name,  Field6_instance_color,  Field6_instance_price, Field6_instance_owner)
Field7 = Field(Field7_instance_name,  Field7_instance_color,  Field7_instance_price, Field7_instance_owner)
Field8 = Field(Field8_instance_name,  Field8_instance_color,  Field8_instance_price, Field8_instance_owner)
Field9 = Field(Field9_instance_name,  Field9_instance_color,  Field9_instance_price, Field9_instance_owner)
Field10 = Field(Field10_instance_name,  Field10_instance_color,  Field10_instance_price, Field10_instance_owner)
Field11 = Field(Field11_instance_name,  Field11_instance_color,  Field11_instance_price, Field11_instance_owner)
Field12 = Field(Field12_instance_name,  Field12_instance_color,  Field12_instance_price, Field12_instance_owner)
Field13 = Field(Field13_instance_name,  Field13_instance_color,  Field13_instance_price, Field13_instance_owner)
Field14 = Field(Field14_instance_name,  Field14_instance_color,  Field14_instance_price, Field14_instance_owner)
Field15 = Field(Field15_instance_name,  Field15_instance_color,  Field15_instance_price, Field15_instance_owner)
Field16 = Field(Field16_instance_name,  Field16_instance_color,  Field16_instance_price, Field16_instance_owner)
Field17 = Field(Field17_instance_name,  Field17_instance_color,  Field17_instance_price, Field17_instance_owner)
Field18 = Field(Field18_instance_name,  Field18_instance_color,  Field18_instance_price, Field18_instance_owner)
Field19 = Field(Field19_instance_name,  Field19_instance_color,  Field19_instance_price, Field19_instance_owner)
Field20 = Field(Field20_instance_name,  Field20_instance_color,  Field20_instance_price, Field20_instance_owner)
Field21 = Field(Field21_instance_name,  Field21_instance_color,  Field21_instance_price, Field21_instance_owner)
Field22 = Field(Field22_instance_name,  Field22_instance_color,  Field22_instance_price, Field22_instance_owner)
Field23 = Field(Field23_instance_name,  Field23_instance_color,  Field23_instance_price, Field23_instance_owner)
Field24 = Field(Field24_instance_name,  Field24_instance_color,  Field24_instance_price, Field24_instance_owner)
Field25 = Field(Field25_instance_name,  Field25_instance_color,  Field25_instance_price, Field25_instance_owner)
Field26 = Field(Field26_instance_name,  Field26_instance_color,  Field26_instance_price, Field26_instance_owner)
Field27 = Field(Field27_instance_name,  Field27_instance_color,  Field27_instance_price, Field27_instance_owner)
Field28 = Field(Field28_instance_name,  Field28_instance_color,  Field28_instance_price, Field28_instance_owner)
Field29 = Field(Field29_instance_name,  Field29_instance_color,  Field29_instance_price, Field29_instance_owner)
Field30 = Field(Field30_instance_name,  Field30_instance_color,  Field30_instance_price, Field30_instance_owner)
Field31 = Field(Field31_instance_name,  Field31_instance_color,  Field31_instance_price, Field31_instance_owner)
Field32 = Field(Field32_instance_name,  Field32_instance_color,  Field32_instance_price, Field32_instance_owner)
Field33 = Field(Field33_instance_name,  Field33_instance_color,  Field33_instance_price, Field33_instance_owner)
Field34 = Field(Field34_instance_name,  Field34_instance_color,  Field34_instance_price, Field34_instance_owner)
Field35 = Field(Field35_instance_name,  Field35_instance_color,  Field35_instance_price, Field35_instance_owner)
Field36 = Field(Field36_instance_name,  Field36_instance_color,  Field36_instance_price, Field36_instance_owner)
Field37 = Field(Field37_instance_name,  Field37_instance_color,  Field37_instance_price, Field37_instance_owner)
Field38 = Field(Field38_instance_name,  Field38_instance_color,  Field38_instance_price, Field38_instance_owner)
Field39 = Field(Field39_instance_name,  Field39_instance_color,  Field39_instance_price, Field39_instance_owner)

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
# def dice_throw():
#     from random import randint
#     result = (randint(1,6))
#     return(result)
#
# def Field_0():
#   print('You are on Field 0')
#   global dice_result
#   print('Throw result:',dice_result)
#   if dice_result == 0:
#       print('*do stuff*')
#   else:
#       dice_result = dice_result - 1
#       Field_1()
#
# def Field_1():
#   print('You are on Field 1')
#   global dice_result
#   print('Throw result:',dice_result)
#   if dice_result == 0:
#       print('*do stuff*')
#   else:
#       dice_result = dice_result - 1
#       Field_2()
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
Field_1()
