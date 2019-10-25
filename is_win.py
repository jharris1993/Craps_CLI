#  Routine "is_win"
#
#  This routine handles the win/loose logic for the game.
#  There are two basic rule variants - "Vegas" and "Texas"
#  which can be choosen by the player at the start of the game
#  (Note:  "Texas" rules are my own invention :) )
#
#  (a)  If "come-out" roll:
#       *  A "7" or "11" is rolled, automatic win.
#       *  A "12", "3", or "2" is rolled, automatic loose.
#       *  Anything else is returned as the point to be made.
#
#  (b)  If "rolling for point" and "Vegas" rules:
#       *  A "7" looses.
#       *  Rolling your "point" wins.
#       *  Anything else doesn't count, and the player rolls again.
#
#  (c)  If "rolling for point" and "Texas" rules:
#       *  Both "7" and "2" (snake-eyes) loose
#       *  Rolling your "point" wins.
#          *  Special Case:  If you roll doubles to make your point
#                            you win 2x your normal payout.
#                            (This assumes that "wagering" has been enabled.)
#
#  Parameters:
#  #1:  "Play Mode"
#       0 = "Come-out roll" (default)
#       1 = "Roll for point" (Vegas rules)
#       2 = "Roll for point" (Texas rules)
#  #2:  List (dice) returned from "throw_dice"
#  #3:  point_to_make, (only if play mode != 0 - defaults to 0)
#       If play mode != 0 and point to make = 0, throws exception (test)
#
#  Returns:
#  #1:  "Win Flag"
#       -1 = Loose (Roll = 7)
#       -2 = Snake-Eyes (Texas Rules: Roll = 2)
#        0 = Neither win nor loose. (default)
#            If come-out roll, total = point to make.
#            If rolling for point, you didn't make your point yet.
#        1 = Win (Vegas and Texas)  i.e. You made your point.
#        2 = (Texas rules only) You rolled doubles to make your point.
#  #2  The point to make if plamode = 0
#      The existing point to make if playmode > 0
#
#  Dependencies:  None.
#
def is_win(play_mode=0, dice=[0, 0, 0], point=0):  #  "point" only used if play mode != 0
    """This function takes the play mode and the dice rolled and determines.\n
        if the player has won, (and if so, how), lost, or continues rolling.\n"""
    if play_mode == 0:  # come-out roll
        if dice[2] == 7 or dice[2] == 11:  #  winning "naturals"
            return (1, point)
        elif dice[2] == 12 or dice[2] == 3 or dice[2] == 2:  #  non-winning "naturals"
            return (-1, point)
        else:
            point = dice[2]  #  set point to the total of the two dice
            return (0, point)
    else:
        pass
#
#  play_mode must be "1" or "2" (1 is the default)
#
#  Has the player rolled a loosing roll while rolling for point?
#
    if dice[2] == 7:  #  Automatic loose while rolling for point
        return (-1, point)
    elif dice[2] == 2 and play_mode == 2:  #  Snake-Eyes, (2) in Texas rules, "2" looses
        return (-2, point)
    else:
        pass  # exit "if" block
#
#  dice roll must either win or not equal the desired point.
#
    if dice[2] != point:  # hasn't won or lost yet, keep playing
        return (0, point)

#
#  At this point, (bad pun!) the player's point must have been made
#  We need to determine if Texas or Vegas rules apply and return
#  the appropriate win_flag
#
    if play_mode == 2:  #  Are we playing Texas rules?
        if dice[0] == dice[1]:  # doubles thrown in Texas rules
            return (2, point)
    return (1, point)
