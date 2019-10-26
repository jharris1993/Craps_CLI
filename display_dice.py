# Display dice
# Displays the values returned by throw_dice
# with the appropriate dramatic effect.
#
# Takes the list object returned by throw_dice
# Returns 0
#
import time  #  Needed for time.sleep

def display_dice(mylist):
    """This function implements a craps-style dice-roll display.\n
Expects a list of three elements - throw 1, throw 2 and total.\n"""

    pauses = 0
    while pauses < 3:
        print("Rolling. . . .")
        time.sleep(1)
        pauses = pauses + 1
    time.sleep(1)
    print("\nDie 1 is. . . .", mylist[0])
    time.sleep(2)
    print("Die 2 is. . . .", mylist[1])
    time.sleep(2)
    print("And the total of both dice is:", mylist[2], "\n")
    time.sleep(3)

    return 0
