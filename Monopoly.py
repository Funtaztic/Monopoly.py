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

#This class will create the players, instead of player_registration_v1:
#source: https://jeffknupp.com/blog/2014/06/18/improve-your-python-python-classes-and-object-oriented-programming/
class Player(object):
  money = 100
  position = 0
  in_jail = False

  def __init__(self, name, token):
    self.name = name
    self.token = token

Player1 = Player('Abel','Ship')
Player2 = Player('Dora','Dog')
Player3 = Player('John','Iron')
Player4 = Player('Chris','Car')



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



#Let's try and manipulate Player1's position through input().

print("Player1's position is " + str(Player1.position))
print("What should be the next position for Player1?")
position_input = input()
Player1.position = position_input

print("Player1's position is " + str(Player1.position))
print("What should be the next position for Player1?")
position_input = input()
Player1.position = position_input
print("Player1's position is " + str(Player1.position))
