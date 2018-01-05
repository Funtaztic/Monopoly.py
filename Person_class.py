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
Player1 = Player('John', 100, 0)
Player2 = Player('James',100, 0)
Player3 = Player('Jeno', 100, 0)
players = []
players.append(Player1.name)
players.append(Player2.name)
players.append(Player3.name)
print('Player list:',players)
#####################################################
class Field(object):

  def __init__(self,name,price,owner):
    self.name   = name
    self.price  = price
    self.owner  = owner

  def intro(self):
    print('**Property name\t\t',self.name)
    print('**Property price\t', self.price)
    print('**Property owner\t', self.owner)
    print('******************************************')

  def buy(self,new_owner_name, new_owner_money):
    self.owner = new_owner_name
#####################################################
Field1  = Field('Miskolc',    10,   'None')
Field2  = Field('Debrecen',   15,   'None')
Field3  = Field('Pest',       20,   'None')
Field4  = Field('Röcsöge',    5,    'None')
#####################################################
dict_for_active_stuff = [1, 2, 3]

def ACTIVATOR_FUNCTION(active_player, active_player_position, active_field):
  # for player in players:
  dict_for_active_stuff[0] = (active_player)
  dict_for_active_stuff[1] = (active_player_position)
  dict_for_active_stuff[2] = (active_field)

#####################################################
field_list = [Field1.name, Field2.name, Field3.name]

def MAIN_MOVE_FUNCTION(player, position, field):
  print('Hi',player)
  print('You are on field',field_list[position])
  print('Do you want to buy',field)

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

ACTIVATOR_FUNCTION(Player1.name, Player1.position, Field1.name)
print(dict_for_active_stuff)

#This does not work perfectly yet, but it is close.
MAIN_MOVE_FUNCTION(*dict_for_active_stuff)
print(dict_for_active_stuff)
Player1.position =+ dice_roll()
print(dict_for_active_stuff)
ACTIVATOR_FUNCTION(Player1.name, Player1.position, Field1.name)
print(dict_for_active_stuff)
MAIN_MOVE_FUNCTION(*dict_for_active_stuff)
