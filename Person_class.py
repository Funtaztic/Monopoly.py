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

Person1 = Person('John',27,'New York',189)
Person2 = Person('James',47,'New York',175)
Person3 = Person('Jeno',21,'New Jersey',199)


Person1.intro()
Person2.intro()
Person3.intro()

Person1.grow()
Person2.grow()
Person3.grow()

Person1.intro()
Person2.intro()
Person3.intro()
