# Dice test
# tests function throw_dice
#
import time
from throw_dice import throw_dice
from display_dice import display_dice
from is_win import is_win

playmode = 1
point = 10
mylist = [0, 0, 0]

mylist = throw_dice(6)
mylist = [5, 5, 10]
display_dice(mylist)
winflag = (is_win(playmode, mylist, point))
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
