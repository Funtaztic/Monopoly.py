#####################################################
class Player(object):

  def __init__(self,name,money):
    self.name       = name
    self.money      = money
    self.properties_list = []

  def intro(self):
    print('Player name:\t\t', self.name)
    print('Player money:\t\t', self.money)
    print('Player properties:\t', self.properties_list)
    print('******************************************')

  def get(self,new_property):
    self.properties_list.append(new_property)

#####################################################
Player1 = Player('John', 100)
Player2 = Player('James',100)
Player3 = Player('Jeno', 100)
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
#####################################################
#####################################################
Player1.intro()
Player2.intro()
Player3.intro()

# Field1.intro()
# Field2.intro()
# Field3.intro()
#####################################################
Player1.get(Field1.name)
Player2.get(Field2.name)
Player3.get(Field3.name)
Player3.get(Field4.name)
#####################################################
Player1.intro()
Player2.intro()
Player3.intro()

def do_you_have_it(Player_props,Field):
  if Field in Player_props:
    print('you have it')
  else:
    print('you do not have it')

do_you_have_it(Player1.properties_list,Field1.name)
do_you_have_it(Player1.properties_list,Field2.name)
do_you_have_it(Player1.properties_list,Field3.name)
