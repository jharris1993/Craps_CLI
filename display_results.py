#  Display Results
#  Displays the results of the throw after processing
#  by is_win.
#
#  Parameters:
#  1.  Win flag result from is_win. (required - will fail if !exist)
#  2.  "Point" - The point to make if continueing to roll. (required - will fail if !exist)
#  3.  Flag to enable "bad throws" (optional to implement "cracked dice")
#
#  Returns:
#    0:  Normal return
#    1:  Invalid Win flag
#    To-Do:  Throw exception?  display fail message and terminate outer program?
#    2:  "Cracked Dice" (bad throw, if enabled via bad-throw flag)
#  Dependencies:
#    Library "random"  (Random number generation to generate the probibility of cracked dice)
#    Library "datetime"  (Used to generate a (somewhat) random seed for the random number generator)

def display_results(playmode, winflag, point, bad_throw_enable=0):
    """This function takes the result of is_win, and based on that result displays the appriopriate
    win, loose, doubles, or keep playing message\n"""
    import random
    import datetime
    import sys

    cracked_dice = 0  #  Variable for random functon to determine if "cracked dice" were thrown
#
#  seed random number generator
#
    myseed = int(datetime.datetime.timestamp(datetime.datetime.now())*1000000)
    random.seed(myseed)
#
#  Optional "Cracked Dice" test if the flag to enable "bad throws" is enabled
#
    if bad_throw_enable == 1:  #  "Cracked-Dice" outcomes are allowed
        cracked_dice = random.randint(1, 10)  # Appx 1 in 10 throws will be cracked
        if cracked_dice == 10:
            print("Cracked Dice! Throw again. . . .\n")
            return 2
    else:
        pass  #  "'formally' close the 'if' statement.  Maybe not necessary, but. . ."
#
#  Normal game progression begins here
#
    if winflag == -1 and point == 2 and playmode == 2:
        print("Snake-Eyes!  You crapped out!!n")
        return 0
    if winflag == -1:
        print("Sorry, you loose. . . .\n")
        return 0
    elif winflag == 0 and playmode == 0:
        print("Your come-out roll is", point)
        print("This is the number, (your 'point'), that you need to win\n")
    elif winflag == 0:
        print("Your point is", point, "  Roll again. . .")
        return 0
    elif winflag == 1 and playmode == 0:
        print("You rolled either a '7' or '11' on your come-out roll")
        print("so you *automatically win*!!\n")
        return 0
    elif winflag == 1:
        print("You Win!!\n")
        return 0
    elif winflag == 2:
        print("Woo Hoo!  You win twice the amount!!\n")
        return 0
    else:  #  Invalid winflag - this should never happen (yea. . . right!)
        try:
            if winflag < 0 or winflag > 2:
                raise Exception('winflag should not be < -1 or > 2. The value of winflag was: {}'.format(winflag))
        except ValueError:
            print("Invalid value for winflag."),
#            prompt = "This should never happen - please report a bug."
#
#  end of function
#