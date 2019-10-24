#  show_doc
#
#  Show doc is a small routine that displays what craps is, and what the rules are
#  for those who are not familiar with the game.
#
#  Dependencies:  None
#
#  Parameters:    None
#
#  Returns:       zero (0)
#
def show_doc():
    """This function displays what craps is, and what the rules are
    for those not familiar with the game\n"""

    keep_going = input("Would you like to see how to play craps\nwith a summary of the rules?[Y] n\n")
#
#  If the player is not interested, branch directly back to the game
#
    if keep_going != "Y" and keep_going != "y" and keep_going != "":
        return
#
#  Display the rules
#
    print("""
            Craps (command line version - graphical version coming soon!)

    Games of chance using dice date back at least 5,000 years; at least thats
    as far back as scientists and archeoligists have found so far. . . .
    "rolling the bones" rocks, or other objects likely dates back to the early
    stone age.

    The game of craps was played as far back as the 13th century - in England
    and it was known as "Hazard".

    The French learned to play Hazard during the Hundred Years War, and it was
    brought to the French settlements in New Orleans sometime during the 18th
    or 19th century by Jean-Bernard Xavier Philippe de Marigny de Mandeville,
    a French nobleman who had learned to play Hazard while visiting England.
    He named it "Crapaud" which comes from the French word "crapaud",
    meaning "toad" - a reference to the people playing it who would hunch over
    the table to get a better view.
    """)
    input("Press 'enter' to continue\n")
    print("""
    The name was shortened into "craps" soon thereafter, but no later than WWII
    when American soldiers played it during the invasion of Europe.

    It has evolved since then into three major variants:  "Vegas", "East Coast",
    and "European" rules; which are all slightly different.

    This game is a greatly simplified version of "Vegas" craps where many of the
    more exotic betting modes and rules have been omitted to make the game easier
    to understand and play.
    """)
    input("Press 'enter' to continue\n")
    print("""
    This game has two variants:  "Vegas" and "Texas" craps, with the "Texas" variant
    being my own invention to make the game more interesting.

                How to play Craps

    A round of craps starts when a player is offered the dice by "the stickman" who is
    responsible for keeping track of the dice.  If the player accepts the dice,
    (which is not required, the dice then move to the next player to the right),
    he starts with what is known as the "come-out" roll.

    He throws the dice and, depending on what number comes up, he either wins, looses
    or continues to play.
    If the player rolls either a "7" or an "11" on the come-out roll, he instantly wins
    and can continue to play by starting a new round.
    If the player rolls a 12, 3, or 2, he automatically looses and the dice move to the
    next player to the right.
    If the player rolls any other number, that number becomes his "point", which is the
    number he has to roll in a subsequent roll of the dice in order to win.
    """)
    input("Press 'enter' to continue\n")
    print("""
                Rolling for your point

    If the player doesn't win or loose during the come-out roll, the game moves to the
    next phase, rolling to "make your point".

    During this phase, the player rolls the dice and, depending on the number that comes
    up, can continue to roll the dice, wins, or looses.
    If the player rolls a number equal to the point established during the come-out roll,
    he wins.
    If the player rolls a "7", he looses.
    If the player rolls any other number, he keeps the dice and continues to roll until
    he either "makes his point" or rolls a 7.
    """)
    input("Press 'enter' to continue\n")
    print("""
                This game's variation on the "Vegas" rules.

    The rules noted before is the most basic variant of the standard "Vegas" rules.

    This game simplifies these rules by:
    Not implementing exotic bets - like betting on a particular roll of the dice.
    (Actually, this game does not implement ANY kind of betting yet.)
    Though in real craps, the player can decide to "yield" the dice at any point
    during the round, (though it is rarely done), this game assumes that the player
    wants to continue to play until he looses and automatically continues.
    """)
    input("Press 'enter' to continue\n")
    print("""
                "Texas" Rules
    "Texas" rules are just like Vegas rules except for two changes:
    1.  If a player rolls "doubles" to make his point, (i.e. two fives to make 10),
        he wins double his wager.
    2.  If he rolls a "2", (snake-eyes), when rolling for his point he looses.
        as if he'd rolled a "7"
    3.  In all other respects, it's played the same as the "Vegas" variant.
    """)
    input("Press 'enter' to start the game\n")
    return (0)
#
#  end of function
#
