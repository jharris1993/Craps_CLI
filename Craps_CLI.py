# Dice test
# tests function throw_dice
#
import time
import sys
from throw_dice import throw_dice
from display_dice import display_dice
from is_win import is_win
from display_results import display_results
from keep_playing import keep_playing
from show_doc import show_doc
from show_history import show_history

texas_flag = 0  #  Rules to use: 0 = Vegas, 1 = Texas
playmode = 0  #  Start game on come-out roll
point = 0
mylist = [0, 0, 0]
continue_playing = 1  #  necessary to start the game
keep_going = "n"  #  Don't show rules unless requested
#
#  Offer to show game history
#
print("Would you like to see a brief history")
keep_going = input("of the game of craps? [Y] n\n")
print(keep_going)
if keep_going == "Y" or keep_going == "y" or keep_going == "":
    show_history()  #  keep_going is used as a dummy variable here
else:
    pass
#
#  Offer to show game documentation
#
print(" ")
keep_going = input("Would you like to know how to play the game? [Y] n\n")
print(keep_going)
if keep_going == "Y" or keep_going == "y" or keep_going == "":
    show_doc()  #  keep_going is used as a dummy variable here
else:
    pass
#
#  Begin game play
#
while True:
    keep_going = input("\nWould you like to play using Vegas or Texas rules? ['V'] or 'T'\n")
    if keep_going == "V" or keep_going == "v" or keep_going == "":
        print("Playing using 'Vegas' rules\n")
        texas_flag = 0
        break
    elif keep_going == "T" or keep_going == "t":
        print("Playing using 'Texas' rules\n")
        texas_flag = 1
        break
    else:
        print("Please select either a 'V' or a 'T'")
        continue

while continue_playing == 1:
    mylist = throw_dice(6)  #  returns list of 3 numbers: die1, die2, total
    point = mylist[2]
    # mylist = [5, 5, 10]
    if playmode == 0:
        print("Come-out roll. . . .\n")
        point_to_make = point  #  Assign point if come-out roll, should exist otherwise
    elif playmode == 1:
        print("Rolling for your point using Vegas Rules. . . .\n")
    elif playmode == 2:
        print("Rolling for your point using Texas Rules. . . .\n")
    else:
        print("playmode = ", playmode, "Oh Snap!  That's an invalid playmode!")
        sys.exit(1)

    display_dice(mylist)  #  Display details of dice roll, always returns 0
    win_result = is_win(playmode, mylist, point_to_make)  #  Determine win/loose - list(winflag, point to make)
    winflag = win_result[0]
    point_to_make = win_result[1]
    display_results(playmode, winflag, point_to_make)  #  Display results of the throw
    time.sleep(3)

#    print("\nwinflag =", winflag, " playmode =", playmode, " point =", point, " point_to_make =", point_to_make, " mylist =", mylist, "\n")
#
#  Keep Playing?
#
    old_playmode = playmode  #  preserve old playmode just in case we need it

    play_flag = keep_playing(winflag, playmode, texas_flag)  #  Returns list[go_flag, playmode]
    if play_flag[0] == 1:  #  play_flag[0] = the go flag. play_flag[1] = desired playmode
        playmode = play_flag[1]
        if winflag > 0:  #  Player won at something
            print("Excellent!  These must be lucky dice, so let's keep playing!\n")
            if texas_flag == 1:  #  What rule-set are we playing under?
                print("Playinig using 'Texas' rules.\n")  #  Playinig using "texas" rules
                playmode = 0  #  Reset playmode to restart from the beginning
            else:
                print("Playing using 'Vegas' rules.\n")  #  If not texas, must be "vegas" rules
                playmode = 0  #  Reset playmode to restart from the beginning
                continue
        elif old_playmode == 0:  #  winflag must be 0 because < 0 triggers a different go-flag
        #  If winflag = o and the old playmode is also = 0, then we're rolling for point after come-out
            print("Now let's roll to make your point - Good Luck!\n")
            continue
        else:
            continue
    else:  #  Go flag must be 0 so we ask to continue or not
        keep_going = input("Would you like to play again? [Y] n\n")
        if keep_going == "Y" or keep_going == "y" or keep_going == "":
            playmode = 0
            print(" ")
            continue
        else:
            print("\nThanks for playing!  I hope you come back soon!\n")
            break
#
#  end of program
#
