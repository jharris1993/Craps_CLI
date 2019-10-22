# Dice test
# tests function throw_dice
#
import time
from throw_dice import throw_dice
mylist = throw_dice(6)
print(mylist)
time.sleep(2)
print("Thow 1 is:", mylist[0])
time.sleep(2)
print("Throw 2 is:", mylist[1])
time.sleep(2)
print("The total is:", mylist[2])
