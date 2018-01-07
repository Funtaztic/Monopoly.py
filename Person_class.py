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
# Player1_input_name = input('Player1, please enter your Name.')
# Player2_input_name = input('Player2, please enter your Name.')
# Player3_input_name = input('Player3, please enter your Name.')
# Player4_input_name = input('Player4, please enter your Name.')
# Player1 = Player(Player1_input_name, 100, 0)
# Player2 = Player(Player2_input_name, 100, 0)
# Player3 = Player(Player3_input_name, 100, 0)
# Player4 = Player(Player4_input_name, 100, 0)

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
dict_for_active_stuff = [0, 1, 2, 3, 4, 5]

def ACTIVATOR_FUNCTION(player_name,player_position,player_properties_list,player_money,field_owner,field_price):

  # for player in players:
    dict_for_active_stuff[0] = (player_name)
    dict_for_active_stuff[1] = (player_position)
    dict_for_active_stuff[2] = (player_properties_list)
    dict_for_active_stuff[3] = (player_money)
    dict_for_active_stuff[4] = (field_owner)
    dict_for_active_stuff[5] = (field_price)

#####################################################
def field_name_list_maker():
    global field_name_list
    field_name_list = [
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
field_name_list_maker()

def field_price_list_maker():
    global field_price_list
    field_price_list = [
    Field0.price,
    Field1.price,
    Field2.price,
    Field3.price,
    Field4.price,
    Field5.price,
    Field6.price,
    Field7.price,
    Field8.price,
    Field9.price,
    Field10.price,
    Field11.price,
    Field12.price,
    Field13.price,
    Field14.price,
    Field15.price,
    Field16.price,
    Field17.price,
    Field18.price,
    Field19.price,
    Field20.price,
    Field21.price,
    Field22.price,
    Field23.price,
    Field24.price,
    Field25.price,
    Field26.price,
    Field27.price,
    Field28.price,
    Field29.price,
    Field30.price,
    Field31.price,
    Field32.price,
    Field33.price,
    Field34.price,
    Field35.price,
    Field36.price,
    Field37.price,
    Field38.price,
    Field39.price
    ]
field_price_list_maker()

def field_owner_list_maker():
    global field_owner_list
    field_owner_list = [
    Field0.owner,
    Field1.owner,
    Field2.owner,
    Field3.owner,
    Field4.owner,
    Field5.owner,
    Field6.owner,
    Field7.owner,
    Field8.owner,
    Field9.owner,
    Field10.owner,
    Field11.owner,
    Field12.owner,
    Field13.owner,
    Field14.owner,
    Field15.owner,
    Field16.owner,
    Field17.owner,
    Field18.owner,
    Field19.owner,
    Field20.owner,
    Field21.owner,
    Field22.owner,
    Field23.owner,
    Field24.owner,
    Field25.owner,
    Field26.owner,
    Field27.owner,
    Field28.owner,
    Field29.owner,
    Field30.owner,
    Field31.owner,
    Field32.owner,
    Field33.owner,
    Field34.owner,
    Field35.owner,
    Field36.owner,
    Field37.owner,
    Field38.owner,
    Field39.owner
    ]
field_owner_list_maker()

def MAIN_MOVE_FUNCTION(player, position, properties_list, money, owner, price):
  print('Hi',player)
  print('You are on field',field_name_list[position])
  print('Press Enter to roll the dice:')
  enter_to_roll_the_dice = input()
  dice_result = dice_roll()
  print('******************************************')
  print(player, 'rolled:' ,dice_result)
  Player1.position = Player1.position + dice_result
  print('Now you are on field',field_name_list[position])
  print('******************************************')
  #BUY IF/ELSE
  answer = '0'
  if  field_owner_list[position] == 'None': #if field has no ownder yet
      while answer != 'Y' or answer != 'N': #while player does not give answer
          print('This property has no owner yet.')
          print('You can buy this property:', field_name_list[position])
          answer = input('Do you want to buy it? (Y/N)').upper()
          if answer == 'Y' and money >= field_price_list[position]:
              print('Your answer was YES')
              print('and you have enough money')
              money -= price
              owner = player
              player.properties_list.append(field_name_list[position])
              Player1.intro()
              print(owner)
          elif answer == 'N':
              print('Your answer was NO')
              pass
          else:
              print("Please enter 'N' for 'NO' or 'Y' for 'YES'.")

  else:
      print('This property belongs to', field_owner_list[position])


  # class Field(object):
  #   def __init__(self,number,name,price,owner,category):
  # class Player(object):
  #   def __init__(self,name,money,position):
  #

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



ACTIVATOR_FUNCTION(Player1.name,Player1.position,Player1.properties_list,Player1.money,field_owner_list[Player1.position],field_price_list[Player1.position])
print(dict_for_active_stuff)

#This does not work perfectly yet, but it is close.
MAIN_MOVE_FUNCTION(*dict_for_active_stuff)
print(dict_for_active_stuff)
