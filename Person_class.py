#####################################################
import math

def dice_roll():
    from random import randint
    result = (randint(1,6))
    return(result)

class Player(object):

  def __init__(self,name,money,position):
    self.name               = name
    self.money              = money
    self.position           = position
    self.properties_list    = []

  def intro(self):
    print('Player name:\t\t',     self.name)
    print('Player money:\t\t',    self.money)
    print('Player position:\t',   self.position)
    print('Player properties:\t', self.properties_list)
    print('******************************************')

  def get(self,new_property):
    self.properties_list.append(new_property)
    print(self.name, '\thave bought\t', new_property)
    print('******************************************')

  # def roll_the_dice(self,position):

#####################################################
#The Player1_input_name stuff can be copied from original.
Player1 = Player('Annabel', 100, 0)
Player2 = Player('Bernard', 100, 0)
Player3 = Player('Clara',   100, 0)
Player4 = Player('Daniel',  100, 0)
players = []
players.append(Player1.name)
players.append(Player2.name)
players.append(Player3.name)
players.append(Player4.name)
print('Player list:',players)
#####################################################
class Field(object):

  def __init__(self,number,name,price,owner,category):
    self.number   = number
    self.name     = name
    self.price    = price
    self.owner    = owner
    self.category = category

  def intro(self):
    print('**Property name\t\t',self.name)
    print('**Property price\t', self.price)
    print('**Property owner\t', self.owner)
    print('******************************************')

  def buy(self,new_owner_name, new_owner_money):
    self.owner = new_owner_name

#####################################################
Field0  = Field(0,  'START',                   0,    'None', 'None')
Field1  = Field(1,  'Mediterranean Avenue',    60,   'None', 'Property')
Field2  = Field(2,  'Community Chest',         0,    'None', 'Chest')
Field3  = Field(3,  'Baltic Avenue',           60,   'None', 'Property')
Field4  = Field(4,  'Income Tax',              200,  'None', 'Penalty')
Field5  = Field(5,  'Reading Railroad',        200,  'None', 'Property')
Field6  = Field(6,  'Oriental Avenue',         100,  'None', 'Property')
Field7  = Field(7,  'Chance',                  0,    'None', 'Chance')
Field8  = Field(8,  'Vermont Avenue',          100,  'None', 'Property')
Field9  = Field(9,  'Connecticut Avenue',      120,  'None', 'Property')
Field10 = Field(10, 'Just Visiting (Jail)',    0,    'None', 'None')
Field11 = Field(11, 'St. Charles Place',       140,  'None', 'Property')
Field12 = Field(12, 'Electric Company',        150,  'None', 'Property')
Field13 = Field(13, 'States Avenue',           140,  'None', 'Property')
Field14 = Field(14, 'Virginia Avenue',         160,  'None', 'Property')
Field15 = Field(15, 'Pennsylvania Railroad',   200,  'None', 'Property')
Field16 = Field(16, 'St. James Place',         180,  'None', 'Property')
Field17 = Field(17, 'Community Chest',         0,    'None', 'Chest')
Field18 = Field(18, 'Tennessee Avenue',        180,  'None', 'Property')
Field19 = Field(19, 'New York Avenue',         200,  'None', 'Property')
Field20 = Field(20, 'Free Parking',            0,    'None', 'None')
Field21 = Field(21, 'Kentucky Avenue',         220,  'None', 'Property')
Field22 = Field(22, 'Chance',                  0,    'None', 'Chance')
Field23 = Field(23, 'Indiana Avenue',          220,  'None', 'Property')
Field24 = Field(24, 'Illinois Avenue',         240,  'None', 'Property')
Field25 = Field(25, 'B. & O. Railroad',        200,  'None', 'Property')
Field26 = Field(26, 'Atlantic Avenue',         260,  'None', 'Property')
Field27 = Field(27, 'Ventnor Avenue',          260,  'None', 'Property')
Field28 = Field(28, 'Water Works',             150,  'None', 'Property')
Field29 = Field(29, 'Marvin Gardens',          280,  'None', 'Property')
Field30 = Field(30, 'Go To Jail',              0,    'None', 'Penalty')
Field31 = Field(31, 'Pacific Avenue',          300,  'None', 'Property')
Field32 = Field(32, 'North Carolina Avenue',   300,  'None', 'Property')
Field33 = Field(33, 'Community Chest',         0,    'None', 'Chest')
Field34 = Field(34, 'Pennsylvania Avenue',     320,  'None', 'Property')
Field35 = Field(35, 'Short Line',              200,  'None', 'Property')
Field36 = Field(36, 'Chance',                  0,    'None', 'Chance')
Field37 = Field(37, 'Park Place',              350,  'None', 'Property')
Field38 = Field(38, 'Luxury Tax',              100,  'None', 'Penalty')
Field39 = Field(39, 'Broadwalk',               400,  'None', 'Property')


#####################################################
dict_for_active_stuff = [1, 2]

def ACTIVATOR_FUNCTION(active_player, active_player_position):
  # for player in players:
  dict_for_active_stuff[0] = (active_player)
  dict_for_active_stuff[1] = (active_player_position)

#####################################################
field_list = [
Field0.name,
Field1.name,
Field2.name,
Field3.name,
Field4.name,
Field5.name,
Field6.name,
Field7.name,
Field8.name,
Field9.name,
Field10.name,
Field11.name,
Field12.name,
Field13.name,
Field14.name,
Field15.name,
Field16.name,
Field17.name,
Field18.name,
Field19.name,
Field20.name,
Field21.name,
Field22.name,
Field23.name,
Field24.name,
Field25.name,
Field26.name,
Field27.name,
Field28.name,
Field29.name,
Field30.name,
Field31.name,
Field32.name,
Field33.name,
Field34.name,
Field35.name,
Field36.name,
Field37.name,
Field38.name,
Field39.name
]

def MAIN_MOVE_FUNCTION(player, position):
  print('Hi',player)
  print('You are on field',field_list[position])


# which_one = int(input("What month (1-12)? "))
# months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
#           'August', 'September', 'October', 'November', 'December']

# if 1 <= which_one <= 12:
#     print("The month is", months[which_one - 1])

#####################################################
Player1.intro()
# Player2.intro()
# Player3.intro()

Field1.intro()
# Field2.intro()
# Field3.intro()
#####################################################
Player1.get(Field1.name)
Player2.get(Field2.name)
Player3.get(Field3.name)
# Player3.get(Field4.name)
#####################################################
Player1.intro()
Player2.intro()
Player3.intro()

def do_you_have_it(Field_name,Player_props,Player_name):
  if Field_name in Player_props:
    print(Player_name, 'you have', Field_name)
  else:
    print(Player_name, 'you do not have', Field_name)

def do_you_have_it_question_for_everybody():
    do_you_have_it(Field1.name, Player1.properties_list,Player1.name)
    do_you_have_it(Field2.name, Player1.properties_list,Player1.name)
    do_you_have_it(Field3.name, Player1.properties_list,Player1.name)

    # do_you_have_it(Field1.name, Player2.properties_list,Player2.name)
    # do_you_have_it(Field2.name, Player2.properties_list,Player2.name)
    # do_you_have_it(Field3.name, Player2.properties_list,Player2.name)

    # do_you_have_it(Field1.name, Player3.properties_list,Player3.name)
    # do_you_have_it(Field2.name, Player3.properties_list,Player3.name)
    # do_you_have_it(Field3.name, Player3.properties_list,Player3.name)

do_you_have_it_question_for_everybody()

ACTIVATOR_FUNCTION(Player1.name, Player1.position)
print(dict_for_active_stuff)

#This does not work perfectly yet, but it is close.
MAIN_MOVE_FUNCTION(*dict_for_active_stuff)
# print(dict_for_active_stuff)
dice_result = dice_roll()
print('You rolled:' ,dice_result)
Player1.position = Player1.position + dice_result
ACTIVATOR_FUNCTION(Player1.name, Player1.position)
# print(dict_for_active_stuff)
# MAIN_MOVE_FUNCTION(*dict_for_active_stuff)

#This does not work perfectly yet, but it is close.
MAIN_MOVE_FUNCTION(*dict_for_active_stuff)
# print(dict_for_active_stuff)
dice_result = dice_roll()
print('You rolled:' ,dice_result)
Player1.position = Player1.position + dice_result
ACTIVATOR_FUNCTION(Player1.name, Player1.position)
# print(dict_for_active_stuff)
# MAIN_MOVE_FUNCTION(*dict_for_active_stuff)

#This does not work perfectly yet, but it is close.
MAIN_MOVE_FUNCTION(*dict_for_active_stuff)
# print(dict_for_active_stuff)
dice_result = dice_roll()
print('You rolled:' ,dice_result)
Player1.position = Player1.position + dice_result
ACTIVATOR_FUNCTION(Player1.name, Player1.position)
# print(dict_for_active_stuff)
# MAIN_MOVE_FUNCTION(*dict_for_active_stuff)

#This does not work perfectly yet, but it is close.
MAIN_MOVE_FUNCTION(*dict_for_active_stuff)
# print(dict_for_active_stuff)
dice_result = dice_roll()
print('You rolled:' ,dice_result)
Player1.position = Player1.position + dice_result
ACTIVATOR_FUNCTION(Player1.name, Player1.position)
# print(dict_for_active_stuff)
# MAIN_MOVE_FUNCTION(*dict_for_active_stuff)

#This does not work perfectly yet, but it is close.
MAIN_MOVE_FUNCTION(*dict_for_active_stuff)
# print(dict_for_active_stuff)
dice_result = dice_roll()
print('You rolled:' ,dice_result)
Player1.position = Player1.position + dice_result
ACTIVATOR_FUNCTION(Player1.name, Player1.position)
# print(dict_for_active_stuff)
# MAIN_MOVE_FUNCTION(*dict_for_active_stuff)

#This does not work perfectly yet, but it is close.
MAIN_MOVE_FUNCTION(*dict_for_active_stuff)
# print(dict_for_active_stuff)
dice_result = dice_roll()
print('You rolled:' ,dice_result)
Player1.position = Player1.position + dice_result
ACTIVATOR_FUNCTION(Player1.name, Player1.position)
# print(dict_for_active_stuff)
# MAIN_MOVE_FUNCTION(*dict_for_active_stuff)
