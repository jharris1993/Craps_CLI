# Dice test
# tests function throw_dice
#
import time
import sys
from throw_dice import throw_dice
from display_dice import display_dice
from is_win import is_win
from display_results import display_results

texas_flag = 0  #  Rules to use: 0 = Vegas, 1 = Texas
playmode = 0  #  Start game on come-out roll
point = 0
mylist = [0, 0, 0]
point_to_make = 10
keep_playing = 1  #  Assume the player will want to keep playing (default)

while keep_playing == 1:
    mylist = throw_dice(6)  #  returns list of 3 numbers: die1, die2, total
    point = mylist[2]
    # mylist = [5, 5, 10]
    if playmode == 0:
        print("\nCome-out roll. . .")
        point_to_make = point  #  Assign point if come-out roll, should exist otherwise
    elif playmode == 1:
        print("\nRolling for your point using Vegas Rules. . . .")
    elif playmode == 2:
        print("\nRolling for your point using Texas Rules. . . .")
    else:
        print("playmode =", playmode, "Oh Snap!  That's an invalid playmode!")
        sys.exit(1)

    display_dice(mylist)  #  Display details of dice roll, always returns 0
    win_result = (is_win(playmode, mylist, point_to_make))  #  Determine win/loose - list(winflag, point to make)
    winflag = win_result[0]
    point_to_make = win_result[1]
    display_results(playmode, winflag, point_to_make, bad_throw_enable=0)  #  Display results of the throw
    print("\nwinflag =", winflag, " playmode =", playmode, " point =", point, " point_to_make =", point_to_make, " mylist =", mylist, "\n")
#
#  Keep Playing?
#
    if playmode == 0:
        if winflag == 1 or winflag == 2:
            print("Wow!  Must be lucky dice - let's keep going!\n")
            continue
        if winflag != -1:
            if texas_flag == 1:
                playmode = 2  #  Continue using *Texas* rules
                continue
            else:
                playmode = 1  #  Continue using *Vegas* rules
                continue
    else:
        if winflag == 1 or winflag == 2:
            print("Wow!  Must be lucky dice - let's keep going!\n")
            continue
        elif winflag == 0:
            print("Don't quit yet - the dice are just getting warm!")
            continue
        else:
            keep_going = input("Do you want to play again? [Y] n")
            if keep_going == "y" or keep_going == "Y" or keep_going == "":
                continue
            else:
                print("That's all folks!  Come back and play again soon!")
                break
#
#  end of program
#
