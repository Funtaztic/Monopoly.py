P1_name  = 'P1'
P1_money = 200
P2_name  = 'P2'
P2_money = 100
P3_name  = 'P3'
P3_money = 40
P4_name  = 'P4'
P4_money = 250

F1_name  = 'BuzaTer'
F1_price = 100

active_player_name  = P1_name
active_player_money = P1_money

active_field_name   = F1_name
active_field_price  = F1_price
active_field_owner  = F1_owner
# function needed to change the player position incremetally with dice_throw()
######################################

def enter():
  enter = input('Press Enter')


def GIGAFUNCTION():
  global active_player_name
  global active_player_money
  global P1_name
  global P1_money
  global P2_name
  global P2_money
  global P3_name
  global P3_money
  global P4_name
  global P4_money
  global active_field_name
  global active_field_price

  if active_player_name == P1_name:
    print('Your turn,', active_player_name, active_player_money)
    active_player_money += 5000
    P1_money = active_player_money

    active_player_name  = P2_name
    active_player_money = P2_money
    enter()
    GIGAFUNCTION()
  elif active_player_name == P2_name:
    print('Your turn,', active_player_name, active_player_money)
    active_player_name  = P3_name
    active_player_money = P3_money
    enter()
    GIGAFUNCTION()
  elif active_player_name == P3_name:
    print('Your turn,', active_player_name, active_player_money)
    active_player_name  = P4_name
    active_player_money = P4_money
    enter()
    GIGAFUNCTION()
  elif active_player_name == P4_name:
    print('Your turn,', active_player_name, active_player_money)
    active_player_name  = P1_name
    active_player_money = P1_money
    enter()
    GIGAFUNCTION()
  else:
    pass

def GIGAFIELD():
  global active_player_name
  global active_player_money
  global P1_name
  global P1_money
  global P2_name
  global P2_money
  global P3_name
  global P3_money
  global P4_name
  global P4_money
  global active_field_name
  global active_field_price
  global active_field_owner

  if active_field_owner == 'N/A':
      player_wants_to_buy = input('Do you want to buy this property?')
      
















GIGAFUNCTION()
print('end')
