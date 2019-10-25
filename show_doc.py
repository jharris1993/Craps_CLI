#  show_doc
#
#  Show doc is a small routine that displays what craps is, and what the rules are
#  for those who are not familiar with the game.
#
#  Dependencies:  The "system" method from the "os" standard library
#
#  Parameters:    None
#
#  Returns:       zero (0)
#

from os import system

def show_doc():
    """This function displays what the rules are for those not familiar with the game\n"""
    #
    #  Display the rules
    #
    system('cls')  #  Clear the screen before displaying the rules
    print("""
                    The Game Of Craps
    (command line version - graphical version coming soon!)

This game is a greatly simplified version of "Vegas" craps where many of the
more exotic betting modes and rules have been omitted to make the game easier
to understand and play.

This game has two variants:  "Vegas" and "Texas" craps, with the "Texas"
variant being my own invention to make the game more interesting.
    """)

    input("Press 'enter' to continue\n")
    system('cls')

    print("""
            This game's variation of the Vegas rules.

Normally real Vegas rules are considerably more complicated and can
include exotic bets, various "house rules" and table limits on the minimum
bet you can place at any one table or on any particular type of bet.

This game simplifies these rules by:

1.  Not implementing exotic bets - like betting on a particular roll of the
    dice. Actually, this game does not implement ANY kind of betting yet.
    (However, what you do on the table next to the computer is your own
    business. . . .)

2.  In real craps the player can decide to "yield" the dice after a round
    has finished.  This game assumes that the player wants to continue play
    until he looses and automatically continues.
    """)

    input("Press 'enter' to continue\n")
    system('cls')

    print("""

                        How to play Craps

A round of craps starts when a player is offered the dice by "the stickman"
who is responsible for keeping track of the dice.  If the player accepts
the dice, he starts with what is known as the "come-out" roll.

                        The Come-Out Roll:

The active player, (known as "the shooter"), throws the dice and, depending
on what number comes up, he either wins, looses, or continues to play.

If the player rolls either a "7" or an "11" on the come-out roll, he instantly
wins and can continue to play by starting a new round.

If the player rolls a "12", "3", or "2", he automatically looses and the dice
move to the next player to the right.

If the player rolls any other number, that number becomes his "point", which
is the number he has to roll in a subsequent roll of the dice in order to win.
    """)

    input("Press 'enter' to continue\n")
    system('cls')

    print("""

                      Rolling for your point

If the player doesn't win or loose during the come-out roll, the game moves
to the next phase which is rolling to "make your point".

During this phase, the player rolls the dice and, depending on the number
that comes up, the player wins, looses, or can continue to roll the dice.

If the player rolls a number equal to the point established during the
come-out roll, he wins.

If the player rolls a "7", he looses.

If the player rolls any other number, he keeps the dice and continues to roll
until he either "makes his point" or rolls a 7.
    """)

    input("Press 'enter' to continue\n")
    system('cls')

    print("""

                          "Texas" Rules

What I call "Texas" rules do not exist in real craps.  They are an invention
of mine to add additional interest.

In this game "Texas" rules are just like the modified Vegas rules mentioned
before, except for two changes:

1.  If a player rolls "doubles" to make his point, (i.e. two fives to make
    10), he wins double his wager.

2.  If he rolls a "2", (snake-eyes), when rolling for his point he looses
    as if he'd rolled a "7".

In all other respects, it's played the same as the "Vegas" variant.

Enjoy!
    """)
    input("Press 'enter' to start the game\n")
    system('cls')

    return (0)
#
#  end of function
#
