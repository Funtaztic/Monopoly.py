#####################################################
class Person(object):

  def __init__(self,name,age,town,height):
    self.name   = name
    self.age    = age
    self.town   = town
    self.height = height

  def intro(self):
    print('My name is',self.name)
    print('My age is', self.age)
    print('My town is', self.town)
    print('My height is', self.height, 'cm')
    print('**********************************')

  def grow(self):
    self.height += 10
#####################################################
Person1 = Person('John',27,'New York',189)
Person2 = Person('James',47,'New York',175)
Person3 = Person('Jeno',21,'New Jersey',199)
#####################################################
class Field(object):

  def __init__(self,name,price,owner):
    self.name   = name
    self.price  = price
    self.owner  = owner

  def intro(self):
    print('My name is',self.name)
    print('My price is', self.price)    
    print('My owner is', self.owner)
    print('**********************************')

  def buy(self,new_owner):
    self.owner = new_owner
#####################################################
Field1  = Field('Miskolc',10,'None')
Field2  = Field('Debrecen',15,'None')
Field3  = Field('Pest',20,'None')
#####################################################
Person1.intro()
Person2.intro()
Person3.intro()

Person1.grow()
Person2.grow()
Person3.grow()

Person1.intro()
Person2.intro()
Person3.intro()
#####################################################
Field1.intro()
Field2.intro()
Field3.intro()
#####################################################
print(Person1.name)
Field1.buy(Person1.name)
Field2.buy(Person2.name)
Field3.buy(Person3.name)
#####################################################
Field1.intro()
Field2.intro()
Field3.intro()
