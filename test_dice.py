# Dice test
# tests function throw_dice
#
import time
import sys
from throw_dice import throw_dice
from display_dice import display_dice
from is_win import is_win

playmode = 0
point = 0
mylist = [0, 0, 0]
bad_throw = 0

mylist = throw_dice(6)
point = mylist[2]
# mylist = [5, 5, 10]
if playmode == 0:
    print("\nCome-out roll. . .")
elif playmode == 1 or playmode  == 2:
    print("\nRolling for your point. . . .")
else:
    print("playmode =", playmode, "Oh Snap!  That's an invalid playmode!")
    sys.exit(1)

display_dice(mylist)
winflag = (is_win(playmode, mylist, point))
if playmode == 0:
    if winflag == -1:
        print("Sorry, you rolled a", mylist[2], "so you loose!")
    elif winflag == 0:
        print("Your point is", mylist[2])
    elif winflag == 1:
        print("Woo Hoo! You rolled a", mylist[2], "so YOU WIN!!")
    else:
        print("winflag =", winflag, "Oh Snap!  That's an invalid winflag!")
        sys.exit(1)
else:
    pass

print("\nPoint to make is", point, "\nYou rolled a", mylist[2])
if winflag == -1:
    if playmode == 2 and mylist[0] == mylist[1]:
        print(winflag, " Snake-Eyes!  You Crapped Out!")
    else:
        print(winflag, " You Loose!")
elif winflag == 0:
    print(winflag, " Nope.  Nothing yet.  Keep goin'!")
elif winflag == 1:
    print(winflag, " You Won!!")
elif winflag == 2:
    print(winflag, " Must be Texas rules - You win Double!!")
else:
    print(winflag, " Oh Snap!  This wasn't supposed to happen. . . .")
