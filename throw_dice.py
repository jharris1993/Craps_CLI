# Function throw_dice
# takes a parameter of the number of sides
# defaulting to a six-sided die.
#
# returns a list that contains throw_1, throw-2 and total

def throw_dice(num_sides=6):
    """This function implements a generic dice throw.\n
The number of sides, (defaults to 6),\n"""
    import random
    import datetime
#    myseed = int(datetime.datetime.timestamp(datetime.datetime.now())*1000000)
#    random.seed(myseed)

    throw_1 = random.randint(1, num_sides)
    throw_2 = random.randint(1, num_sides)
    total = throw_1 + throw_2
    list1 = [throw_1, throw_2, total]
    return list1
