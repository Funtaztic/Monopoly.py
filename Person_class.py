#####################################################
class Person(object):

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
Person1 = Person('John', 100)
Person2 = Person('James',100)
Person3 = Person('Jeno', 100)
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
#####################################################
#####################################################
#####################################################
Person1.intro()
Person2.intro()
Person3.intro()

# Field1.intro()
# Field2.intro()
# Field3.intro()
#####################################################
Person1.get(Field1.name)
Person2.get(Field2.name)
Person3.get(Field3.name)
#####################################################
Person1.intro()
Person2.intro()
Person3.intro()
