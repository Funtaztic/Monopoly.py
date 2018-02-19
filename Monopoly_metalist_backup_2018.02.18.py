#TEST: 2 players, 4 fields, money, list of lists, 1 function

import math

def dice_roll():
	from random import randint
	result = (randint(1,6))
	return(result)

metalist = [
# [number, name, money, owner]
	[0,		'Start,',		0,	'Player1'],
	[1,		'Field1',		10,	'Player1'],
	[2,		'Field2', 	10,	'Player1'],
	[3,		'Field3', 	10,	'Player1'],
	[4,		'Field4', 	10,	'Player1'],
	[5,		'Field5', 	10,	'Player1'],
	[6,		'Field6', 	10,	'Player1'],
	[7,		'Field7', 	10,	'Player1'],
	[8,		'Field8', 	10,	'Player1'],
	[9,		'Field9', 	10,	'Player1'],
	[10,	'Field10',	10,	'Bank'],
	[11,	'Field11',	10,	'Bank'],
	[12,	'Field12',	10,	'Bank'],
	[13,	'Field13',	10,	'Bank'],
	[14,	'Field14',	10,	'Bank'],
	[15,	'Field15',	10,	'Bank'],
	[16,	'Field16',	10,	'Bank'],
	[17,	'Field17',	10,	'Bank'],
	[18,	'Field18',	10,	'Bank'],
	[19,	'Field19',	10,	'Bank'],
	[20,	'Field20',	10,	'Bank'],
	[21,	'Field21',	10,	'Bank'],
	[22,	'Field22',	10,	'Bank'],
	[23,	'Field23',	10,	'Bank'],
	[24,	'Field24',	10,	'Bank'],
	[25,	'Field25',	10,	'Bank'],
	[26,	'Field26',	10,	'Bank'],
	[27,	'Field27',	10,	'Bank'],
	[28,	'Field28',	10,	'Bank'],
	[29,	'Field29',	10,	'Bank'],
	[30,	'Field30',	10,	'Bank'],
	[31,	'Field31',	10,	'Bank'],
	[32,	'Field32',	10,	'Bank'],
	[33,	'Field33',	10,	'Bank'],
	[34,	'Field34',	10,	'Bank'],
	[35,	'Field35',	10,	'Bank'],
	[36,	'Field36',	10,	'Bank'],
	[37,	'Field37',	10,	'Bank'],
	[38,	'Field38',	10,	'Bank'],
	[39,	'Field39',	10,	'Bank'],
	
	
	]
# [number,	 name,		price,	 owner]
# [0,				'Start',			0,	'Bank'],

# player_list (a list of info about the players) = [position, name, money]
player_1_list = [0,'Player1',100]
player_2_list = [0,'Player2',100]

# properties list for each player
proper_1_list = []
proper_2_list = []

# player_n_list[0] = Position
# player_n_list[1] = Name
# player_n_list[2] = Money

def f():
	answer = 0
	while answer != 1 or answer != 2:
		print('------------------------------------------------------------------------------')
		print(player_1_list[1], 'press Enter to roll the dice.')
		roll = input()
		dice_result = dice_roll()
		print(player_1_list[1], 'you rolled:', dice_result)
		
		#dice throw, player movement and crossing-start-money
		if player_1_list[0] + dice_result <= 39:
			player_1_list[0] += dice_result
		else:
			player_1_list[2] += 200
			player_1_list[0] += dice_result - 40
		print(player_1_list[1], 'you are on field number', player_1_list[0], ':', metalist[player_1_list[0]][1], 'and you have', player_1_list[2], 'money')
		
		# metalist[player_1_list[0]][1] = based on the position of the player, find the active field's name
		# metalist[player_1_list[0]][2] = based on the position of the player, find the active field's price
		# metalist[player_1_list[0]][3] = based on the position of the player, find the active field's owner
		
		#if active player owns this place already, he can build. 
		#elif: other player owns the place, active player has to pay (based on price * houses)
		#elif: nobody owns the place, it can be bought by active player.
		#else: if active player does not want to buy it, it goes to an auction.
		
		#if active player owns this place already, he can build. 
		if metalist[player_1_list[0]][3] == player_1_list[0]:
			print(player_1_list[1], 'you own this place. Do you want to build? BETA')
		
		#elif: other player owns the place, active player has to pay (based on price * houses)
		#elif metalist[player_1_list[0]][3] == player_2_list[0] or metalist[player_1_list[0]][3] == 'Bank':
			
		
		#elif: nobody owns the place, it can be bought by active player.
		elif metalist[player_1_list[0]][3] == 'Bank':
			print('This place is owned by the Bank.')
			print('Do you want to buy', metalist[player_1_list[0]][1], '?')
			print('1. Yes')
			print('2. No')
	
			answer=input()
			if answer == '1':
				print('Player 1 has these properties:', proper_1_list)
				print(metalist[player_1_list[0]][3])
				#player money -= field price
				player_1_list[2] -= metalist[player_1_list[0]][2]
				#bought property goes into player's property list
				proper_1_list.append(metalist[player_1_list[0]][1])
				print('Player 1 has these properties:', proper_1_list)
				#player who paid, becomes the new owner of the property
				metalist[player_1_list[0]][3] = player_1_list[1]
				print(metalist[player_1_list[0]][3])
			elif answer == '2':
				#player moves 1 field forward
	
				player_1_list[0] += 1
			else:
				print('Please select from the options.')
			
			print('------------------------------------------------------------------------------')
			print("Player2's turn would be here")
		#else: if active player does not want to buy it, it goes to an auction.
	# 	else:
		 # s
			

	# enter=input("Press Enter")
	# f()

#The game starts
f()
