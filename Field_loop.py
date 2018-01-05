def Field_loop_for_Player1():
  Player1.position += dice_roll()
  if Player1.position == 0:
      Field_0()
  elif Player1.position == 0:
      Field_0()
  elif Player1.position == 1:
      Field_1()
  elif Player1.position == 2:
      Field_2()
  elif Player1.position == 3:
      Field_3()
  elif Player1.position == 4:
      Field_4()
  elif Player1.position == 5:
      Field_5()
  elif Player1.position == 6:
      Field_6()
  elif Player1.position == 7:
      Field_7()
  elif Player1.position == 8:
      Field_8()
  elif Player1.position == 9:
      Field_9()
  elif Player1.position == 10:
      Field_10()
  elif Player1.position == 11:
      Field_11()
  elif Player1.position == 12:
      Field_12()
  elif Player1.position == 13:
      Field_13()
  elif Player1.position == 14:
      Field_14()
  elif Player1.position == 15:
      Field_15()
  elif Player1.position == 16:
      Field_16()
  elif Player1.position == 17:
      Field_17()
  elif Player1.position == 18:
      Field_18()
  elif Player1.position == 19:
      Field_19()
  elif Player1.position == 20:
      Field_20()
  elif Player1.position == 21:
      Field_21()
  elif Player1.position == 22:
      Field_22()
  elif Player1.position == 23:
      Field_23()
  elif Player1.position == 24:
      Field_24()
  elif Player1.position == 25:
      Field_25()
  elif Player1.position == 26:
      Field_26()
  elif Player1.position == 27:
      Field_27()
  elif Player1.position == 28:
      Field_28()
  elif Player1.position == 29:
      Field_29()
  elif Player1.position == 30:
      Field_30()
  elif Player1.position == 31:
      Field_31()
  elif Player1.position == 32:
      Field_32()
  elif Player1.position == 33:
      Field_33()
  elif Player1.position == 34:
      Field_34()
  elif Player1.position == 35:
      Field_35()
  elif Player1.position == 36:
      Field_36()
  elif Player1.position == 37:
      Field_37()
  elif Player1.position == 38:
      Field_38()
  elif Player1.position == 39:
      Field_39()
  elif Player1.position == 40:
      Field_40()

def Field_loop_for_Player2():
  Player2.position += dice_roll()
  if Player2.position == 0:
      Field_0()
  elif Player2.position == 0:
      Field_0()
  elif Player2.position == 1:
      Field_1()
  elif Player2.position == 2:
      Field_2()
  elif Player2.position == 3:
      Field_3()
  elif Player2.position == 4:
      Field_4()
  elif Player2.position == 5:
      Field_5()
  elif Player2.position == 6:
      Field_6()
  elif Player2.position == 7:
      Field_7()
  elif Player2.position == 8:
      Field_8()
  elif Player2.position == 9:
      Field_9()
  elif Player2.position == 10:
      Field_10()
  elif Player2.position == 11:
      Field_11()
  elif Player2.position == 12:
      Field_12()
  elif Player2.position == 13:
      Field_13()
  elif Player2.position == 14:
      Field_14()
  elif Player2.position == 15:
      Field_15()
  elif Player2.position == 16:
      Field_16()
  elif Player2.position == 17:
      Field_17()
  elif Player2.position == 18:
      Field_18()
  elif Player2.position == 19:
      Field_19()
  elif Player2.position == 20:
      Field_20()
  elif Player2.position == 21:
      Field_21()
  elif Player2.position == 22:
      Field_22()
  elif Player2.position == 23:
      Field_23()
  elif Player2.position == 24:
      Field_24()
  elif Player2.position == 25:
      Field_25()
  elif Player2.position == 26:
      Field_26()
  elif Player2.position == 27:
      Field_27()
  elif Player2.position == 28:
      Field_28()
  elif Player2.position == 29:
      Field_29()
  elif Player2.position == 30:
      Field_30()
  elif Player2.position == 31:
      Field_31()
  elif Player2.position == 32:
      Field_32()
  elif Player2.position == 33:
      Field_33()
  elif Player2.position == 34:
      Field_34()
  elif Player2.position == 35:
      Field_35()
  elif Player2.position == 36:
      Field_36()
  elif Player2.position == 37:
      Field_37()
  elif Player2.position == 38:
      Field_38()
  elif Player2.position == 39:
      Field_39()
  elif Player2.position == 40:
      Field_40()

# atom-increment package
# Ctrl+Alt+i
# Ctrl+Alt+j

This should be the basic idea:
    active_player_data = Player1_data
    Field_function()
    Player1_data = active_player_data 
