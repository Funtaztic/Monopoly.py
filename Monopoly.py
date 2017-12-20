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

basic_money_function()

##############################################################################
# Player(s): what should they be? Functions? Lists?
#Dictionaries? https://docs.python.org/3/tutorial/datastructures.html
# source: https://en.wikipedia.org/wiki/Monopoly_(game)

#racecar
#iron
#top_hat

#Hard-coded version of player as dictionary, money as key, (money)amount as value.
#Money can be modified as seen below.
#-> basic_money_function is not needed anymore?/needs to be modified?

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
for key in battleship.keys():
    val = battleship[key]
    print(key,':',val)
    # But this is not sorted. It prints the values at random order every time.
