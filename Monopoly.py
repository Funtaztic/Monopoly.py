##############################################################################
####This should be the digital version of the classic boardgame: Monopoly.####
##############################################################################
#Make it for 1 player first, or start development with multiple players?

##############################################################################
import math

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
# Player(s): what should they be? Functions? Lists?
#Dictionaries? https://docs.python.org/3/tutorial/datastructures.html
# source: https://en.wikipedia.org/wiki/Monopoly_(game)

#Player should be a Class. I don't yet get it, but I think it should be that.

#def player_registration_v2():
#    class player:
#        def token(self):


#This class will create the players, instead of player_registration_v1:
#source: https://jeffknupp.com/blog/2014/06/18/improve-your-python-python-classes-and-object-oriented-programming/
class Player(object):
  money = 100
  position = 0
  in_jail = False

  def __init__(self, name, token):
    self.name = name
    self.token = token

Player1 = Player('Abel','Battleship')



#remove last item from the dict, until number_of_players number of players remain.
#Source: https://www.tutorialspoint.com/python3/python_lists.htm

#racecar
#iron
#top_hat

#Hard-coded version of player as dictionary, money as key, (money)amount as value.
#Money can be modified as seen below.
#-> basic_money_function is not needed anymore?/needs to be modified?
def player_data_init():
    battleship = {
        'money':    150,
        'position': 2,
        'in_jail':  False,}
    print('Battleship money:', battleship['money'])
    battleship['money'] = battleship['money'] + 10
    print('Battleship money + 10')
    print('Battleship money:', battleship['money'])
    print(battleship)

#Source: http://www.compciv.org/guides/python/fundamentals/dictionaries-overview/
# Iterating through key-value pairs with items()
def player_data_print():
    for key in battleship.keys():
        val = battleship[key]
        print(key,':',val)
        # But this is not sorted. It prints the values at random order every time.
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




#Table squares (where the players can go by rolling the dice)
#def square_1():


##############################################################################
##############################################################################
##############################################################################
Field_0 = {
"Name":      "START",
"Color":     "N/A",
"Price":     -200,
"Owner":     "N/A",
}
#---------------------------------------------#
#---------------------------------------------#
Field_1 = {
"Name":      "Mediterranean Avenue",
"Color":     "Brown",
"Price":     60,
"Owner":     "None",
}
#---------------------------------------------#
#---------------------------------------------#
Field_2 = {
"Name":      "Community Chest",
"Color":     "Blue Chest",
"Price":     "N/A",
"Owner":     "N/A",
}
#---------------------------------------------#
#---------------------------------------------#
Field_3 = {
"Name":      "Baltic Avenue",
"Color":     "Brown",
"Price":     60,
"Owner":     "None",
}
#---------------------------------------------#
#---------------------------------------------#
Field_4 = {
"Name":      "Income Tax",
"Color":     "N/A",
"Price":     200,
"Owner":     "N/A",
}

##############################################################################

##############################################################################

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

Player1.money -= Field_0["Price"]
print("Now the player has crossed the START field, and receives 200 money")

print('Player1 money:' + str(Player1.money))
