#####################################################
import math
#####################################################
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
#####################################################
#We could use some more global variables to make the money system work.
#You need 'global' before accessing these in any way.
houses_owned_by_the_bank = 32
hotels_owned_by_the_bank = 12

def dice_roll():
    from random import randint
    result = (randint(1,6))
    return(result)

class Player(object):

  def __init__(self,name,money,position,roundnum):
    self.name               = name
    self.money              = money
    self.position           = position
    self.roundnum           = roundnum
    self.properties_list    = []

  def intro(self):
    print('Player name:\t\t',     self.name)
    print('Player money:\t\t',    self.money)
    print('Player position:\t',   self.position)
    print('Player round:\t\t',    self.roundnum)
    print('Player properties:\t', self.properties_list)
    print('******************************************')

  def get(self,new_property):
    self.properties_list.append(new_property)
    print(self.name, '\thave bought\t', new_property)
    print('******************************************')

  # def roll_the_dice(self,position):

# ####################################################
# The Player1_input_name stuff can be copied from original.
# Player1_input_name = input('Player1, please enter your Name.')
# Player2_input_name = input('Player2, please enter your Name.')
# Player3_input_name = input('Player3, please enter your Name.')
# Player4_input_name = input('Player4, please enter your Name.')
# Player1 = Player(Player1_input_name, 100, 0)
# Player2 = Player(Player2_input_name, 100, 0)
# Player3 = Player(Player3_input_name, 100, 0)
# Player4 = Player(Player4_input_name, 100, 0)

Player1 = Player('Annabel', 100, 0, 1)
Player2 = Player('Bernard', 100, 0, 1)
Player3 = Player('Clara',   100, 0, 1)
Player4 = Player('Daniel',  100, 0, 1)

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

# + number_of_houses, number_of_villas

  def intro(self):
    print('******************************************')
    print('**Property name\t\t',self.name)
    print('**Property price\t', self.price)
    print('**Property owner\t', self.owner)
    print('******************************************')

  def buy(self,new_owner_name, new_owner_money):
    self.owner = new_owner_name

#####################################################

Field0  = Field(0,  'START',                   0,    'Bank', 'None') #This should not be buyable. Set price back to 0, or none.
Field1  = Field(1,  'Mediterranean Avenue',    60,   'Bank', 'Property')
Field2  = Field(2,  'Community Chest',         0,    'Bank', 'Chest')
Field3  = Field(3,  'Baltic Avenue',           60,   'Bank', 'Property')
Field4  = Field(4,  'Income Tax',              200,  'Bank', 'Penalty')
Field5  = Field(5,  'Reading Railroad',        200,  'Bank', 'Property')
Field6  = Field(6,  'Oriental Avenue',         100,  'Bank', 'Property')
Field7  = Field(7,  'Chance',                  0,    'Bank', 'Chance')
Field8  = Field(8,  'Vermont Avenue',          100,  'Bank', 'Property')
Field9  = Field(9,  'Connecticut Avenue',      120,  'Bank', 'Property')
Field10 = Field(10, 'Just Visiting (Jail)',    0,    'Bank', 'None')
Field11 = Field(11, 'St. Charles Place',       140,  'Bank', 'Property')
Field12 = Field(12, 'Electric Company',        150,  'Bank', 'Property')
Field13 = Field(13, 'States Avenue',           140,  'Bank', 'Property')
Field14 = Field(14, 'Virginia Avenue',         160,  'Bank', 'Property')
Field15 = Field(15, 'Pennsylvania Railroad',   200,  'Bank', 'Property')
Field16 = Field(16, 'St. James Place',         180,  'Bank', 'Property')
Field17 = Field(17, 'Community Chest',         0,    'Bank', 'Chest')
Field18 = Field(18, 'Tennessee Avenue',        180,  'Bank', 'Property')
Field19 = Field(19, 'New York Avenue',         200,  'Bank', 'Property')
Field20 = Field(20, 'Free Parking',            0,    'Bank', 'None')
Field21 = Field(21, 'Kentucky Avenue',         220,  'Bank', 'Property')
Field22 = Field(22, 'Chance',                  0,    'Bank', 'Chance')
Field23 = Field(23, 'Indiana Avenue',          220,  'Bank', 'Property')
Field24 = Field(24, 'Illinois Avenue',         240,  'Bank', 'Property')
Field25 = Field(25, 'B. & O. Railroad',        200,  'Bank', 'Property')
Field26 = Field(26, 'Atlantic Avenue',         260,  'Bank', 'Property')
Field27 = Field(27, 'Ventnor Avenue',          260,  'Bank', 'Property')
Field28 = Field(28, 'Water Works',             150,  'Bank', 'Property')
Field29 = Field(29, 'Marvin Gardens',          280,  'Bank', 'Property')
Field30 = Field(30, 'Go To Jail',              0,    'Bank', 'Penalty')
Field31 = Field(31, 'Pacific Avenue',          300,  'Bank', 'Property')
Field32 = Field(32, 'North Carolina Avenue',   300,  'Bank', 'Property')
Field33 = Field(33, 'Community Chest',         0,    'Bank', 'Chest')
Field34 = Field(34, 'Pennsylvania Avenue',     320,  'Bank', 'Property')
Field35 = Field(35, 'Short Line',              200,  'Bank', 'Property')
Field36 = Field(36, 'Chance',                  0,    'Bank', 'Chance')
Field37 = Field(37, 'Park Place',              350,  'Bank', 'Property')
Field38 = Field(38, 'Luxury Tax',              100,  'Bank', 'Penalty')
Field39 = Field(39, 'Broadwalk',               400,  'Bank', 'Property')


#####################################################
list_for_active_stuff = [0, 1, 2, 3, 4, 5, 6]

def ACTIVATOR_FUNCTION(player_name,player_position,player_properties_list,player_money,field_owner,field_price,field_category):

  # for player in players:
    list_for_active_stuff[0] = (player_name)
    list_for_active_stuff[1] = (player_position)
    list_for_active_stuff[2] = (player_properties_list)
    list_for_active_stuff[3] = (player_money)
    list_for_active_stuff[4] = (field_owner)
    list_for_active_stuff[5] = (field_price)
    list_for_active_stuff[6] = (field_category)

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
print(field_name_list)

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
print(field_price_list)

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
print(field_owner_list)

def field_category_list_maker():
    global field_category_list
    field_category_list = [
    Field0.category,
    Field1.category,
    Field2.category,
    Field3.category,
    Field4.category,
    Field5.category,
    Field6.category,
    Field7.category,
    Field8.category,
    Field9.category,
    Field10.category,
    Field11.category,
    Field12.category,
    Field13.category,
    Field14.category,
    Field15.category,
    Field16.category,
    Field17.category,
    Field18.category,
    Field19.category,
    Field20.category,
    Field21.category,
    Field22.category,
    Field23.category,
    Field24.category,
    Field25.category,
    Field26.category,
    Field27.category,
    Field28.category,
    Field29.category,
    Field30.category,
    Field31.category,
    Field32.category,
    Field33.category,
    Field34.category,
    Field35.category,
    Field36.category,
    Field37.category,
    Field38.category,
    Field39.category
    ]
field_category_list_maker()
print(field_category_list)

def BUY_OR_PAY(player, position, properties_list, money, owner, price, category):

  # print(field_name_list)
  # print(field_price_list)
  # print(field_owner_list)
  # print(field_category_list)
  print('******************************************')
  print(player, position, properties_list, money, owner, price, category)
  print('******************************************')
  # print('Hi',player)
  print('You are on field',field_name_list[position])
  # print('Press Enter to roll the dice:')
  # enter_to_roll_the_dice = input()
  # dice_result = dice_roll()
  print('************************************************************************************')
  print('************************************************************************************')
  print('************************************************************************************')
  # print(player, 'rolled:' ,dice_result)
  # position = position + dice_result
  print('Now you are on field', position, ':', field_name_list[position])
  print('******************************************')
  #BUY IF/ELSE
  answer = '0'
  if  field_owner_list[position] == 'Bank': #if field has no ownder yet
      # this has to be corrected, while is not needed maybe? IF is enough?
      while answer != 'Y' or answer != 'N': #while player does not give answer
          if field_category_list[position] != 'Property':
              print('You can not buy this property. It is not for sale.')
              next_player()
          elif field_category_list[position] == 'Property':
              print('This property has no owner yet.')
              print('You can buy this property:', field_name_list[position])
              # answer = input('Do you want to buy it? (Y/N)').upper()
              print('It costs', field_price_list[position])
              answer = input('Do you want to buy it? (Y/N)').upper()
              if answer == 'Y' and money >= field_price_list[position]:
                  print('Your answer was YES and you have enough money')
                  print(player, position, properties_list, money, owner, price, category)
                  money -= price
                  print('Now you pay', field_price_list[position], 'for the property')
                  # https://stackoverflow.com/questions/986006/how-do-i-pass-a-variable-by-reference
                  owner = list_for_active_stuff[0]
                  field_to_be_bought = field_name_list[position]
                  properties_list.append(field_to_be_bought)
                  print(player, position, properties_list, money, owner, price, category)
                  pass
              elif answer == 'Y' and money < field_price_list[position]:
                  print("I'm sorry, you don't have enough money.")
                  print('Next player.')
                  next_player()
              elif answer == 'N':
                  print('Okay, next player.')
                  next_player()
              else:
                  print("Please enter 'N' for 'NO' or 'Y' for 'YES'.")

<<<<<<< HEAD
  elif field_owner_list[position] == Player1.name:
      print('This property is owned by', Player1.name)
      print('Now you have to pay a penalty fee.')



      # print('This property belongs to', field_owner_list[position])


=======
  else:
      print('This property belongs to', field_owner_list[position])
      next_player()
>>>>>>> c73cc3773574971127b72a25c7aac911b488ead6
#####################################################
def next_player():
    if list_for_active_stuff[0] == Player4.name or list_for_active_stuff[0] == 0:

        Player1.intro()
        print('Hi',Player1.name, 'you are in round', Player1.roundnum)
        print('Press Enter to roll the dice:')
        enter_to_roll_the_dice = input()
        dice_result = dice_roll()
        print(Player1.name, 'rolled:' ,dice_result)

        if Player1.position + dice_result <= 39:
            Player1.position += dice_result
        else:
            Player1.money += 200
            Player1.position += dice_result - 40
            Player1.roundnum += 1

        ACTIVATOR_FUNCTION(Player1.name,Player1.position,Player1.properties_list,Player1.money,field_owner_list[Player1.position],field_price_list[Player1.position],field_category_list[Player1.position])
        BUY_OR_PAY(*list_for_active_stuff)

    elif list_for_active_stuff[0] == Player1.name:

        Player2.intro()
        print('Hi',Player2.name, 'you are in round', Player2.roundnum)
        print('Press Enter to roll the dice:')
        enter_to_roll_the_dice = input()
        dice_result = dice_roll()
        print(Player2.name, 'rolled:' ,dice_result)

        if Player2.position + dice_result <= 39:
            Player2.position += dice_result
        else:
            Player2.money += 200
            Player2.position += dice_result - 40
            Player2.roundnum += 1

        ACTIVATOR_FUNCTION(Player2.name,Player2.position,Player2.properties_list,Player2.money,field_owner_list[Player2.position],field_price_list[Player2.position],field_category_list[Player2.position])
        BUY_OR_PAY(*list_for_active_stuff)

    elif list_for_active_stuff[0] == Player2.name:

        Player3.intro()
        print('Hi',Player3.name, 'you are in round', Player3.roundnum)
        print('Press Enter to roll the dice:')
        enter_to_roll_the_dice = input()
        dice_result = dice_roll()
        print(Player3.name, 'rolled:' ,dice_result)

        if Player3.position + dice_result <= 39:
            Player3.position += dice_result
        else:
            Player3.money += 200
            Player3.position += dice_result - 40
            Player3.roundnum += 1

        ACTIVATOR_FUNCTION(Player3.name,Player3.position,Player3.properties_list,Player3.money,field_owner_list[Player3.position],field_price_list[Player3.position],field_category_list[Player3.position])
        BUY_OR_PAY(*list_for_active_stuff)

    elif list_for_active_stuff[0] == Player3.name:

        Player4.intro()
        print('Hi',Player4.name, 'you are in round', Player4.roundnum)
        print('Press Enter to roll the dice:')
        enter_to_roll_the_dice = input()
        dice_result = dice_roll()
        print(Player4.name, 'rolled:' ,dice_result)

        if Player4.position + dice_result <= 39:
            Player4.position += dice_result
        else:
            Player4.money += 200
            Player4.position += dice_result - 40
            Player4.roundnum += 1

        ACTIVATOR_FUNCTION(Player4.name,Player4.position,Player4.properties_list,Player4.money,field_owner_list[Player4.position],field_price_list[Player4.position],field_category_list[Player4.position])
        BUY_OR_PAY(*list_for_active_stuff)
    else:
        print('There is no player left to play with...? :S')

# This works like this, but maybe the player's name money properties etc should be put into a list just like field_name_list and field_price_list?

#####################################################



#####################################################

Player1.intro()
# Player3.intro()
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

################################################################################
############################## THE GAME STARTS #################################
################################################################################

ACTIVATOR_FUNCTION(Player1.name,Player1.position,Player1.properties_list,Player1.money,field_owner_list[Player1.position],field_price_list[Player1.position],field_category_list[Player1.position])
next_player()
print(list_for_active_stuff)

# #This does not work perfectly yet, but it is close.
# BUY_OR_PAY(*list_for_active_stuff)
# print(list_for_active_stuff)
