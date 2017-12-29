##############################################################################
####This should be the digital version of the classic boardgame: Monopoly.####
##############################################################################
#Make it for 1 player first, or start development with multiple players?

##############################################################################
import math

ActivePlayer = 'None'
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
  owned_properties = []

  def __init__(self, name, token):
    self.name = name
    self.token = token

#Let's make a player name maker, that uses user input to make class instances.

Player1_input_name = input("Player1, Please enter your name:")
Player1_input_token = input("Player1, Please select a token:")

Player2_input_name = input("Player2, Please enter your name:")
Player2_input_token = input("Player2, Please select a token:")

Player3_input_name = input("Player3, Please enter your name:")
Player3_input_token = input("Player3, Please select a token:")

Player4_input_name = input("Player4, Please enter your name:")
Player4_input_token = input("Player4, Please select a token:")

Player1 = Player(Player1_input_name,Player1_input_token)
Player2 = Player(Player2_input_name,Player2_input_token)
Player3 = Player(Player3_input_name,Player3_input_token)
Player4 = Player(Player4_input_name,Player4_input_token)

print(Player1.name, Player1.token)
print(Player2.name, Player2.token)
print(Player3.name, Player3.token)
print(Player4.name, Player4.token)


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

#MAKE ActivePlayer.money work! var needed! global var!

##############################################################################
def Field_1():
    global Player1
    print("You are on", Field_1.Name)
    if Field_1.Owner == "N/A":
        player_wants_to_buy = input("Do you want to buy it? (Y/N)")
        player_wants_to_buy.upper()
        if player_wants_to_buy == "Y" and Player1.money >= Field_1.Price:
            Player1.money = Player1.money - Field_1.Price
            Field_1.Owner = Player1.Name
            Player1.owned_properties.append(Field_1.Name)
        else:
            print("You don't want to buy, or you don't have enough money.")
    else:
        print("This property is already owned by someone.")

    empty_useless_var = input("If you don't want to do anything, just press Enter.")

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
print("Please press Enter to roll the dice for Player1")
position_input = input()
Player1.position = dice_throw()
print("Player1's position is " + str(Player1.position))
Field_1()
