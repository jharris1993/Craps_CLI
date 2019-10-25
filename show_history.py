#  show_history
#
#  This function displays a brief history of the game of craps
#
#  Dependencies:  The "system" method from the "os" standard library
#
#  Parameters:    None
#
#  Returns:       zero (0)
#

from os import system

def show_history():
    """This function displays a brfief history of the game of craps\n"""
    #
    #  Display the history of the game
    #
    system('cls')  #  Clear the screen before displaying the rules
    print("""

                A brief history of the game of Craps

Games of chance using dice date back at least 5,000 years.  At least that's
as far back as scientists and archaeologists have found evidence of dice
games - so far. . . .

"Rolling the bones", rocks, or other objects likely dates back to the early
stone age.

A game similar to the modern version of craps was played as far back as
the 13th century and in England it was known as "Hazard".

The French learned to play Hazard during the Hundred Years War.  It was
brought to the French settlements in New Orleans sometime during the 18th
or 19th century by Jean-Bernard Xavier Philippe de Marigny de Mandeville,
a French nobleman, who had learned to play Hazard while visiting England.

He named it "Crapaud" which comes from the French word "crapaud",
meaning "toad" - a reference to the people playing it who would hunch over
the table to get a better view.
    """)

    input("Press 'enter' to continue\n")
    system('cls')

    print("""

The name was shortened into "craps" soon thereafter, but no later than WWII
when American soldiers played it during the invasion of Europe.

It has evolved since then into three major variants:  "Vegas", "East Coast",
and "European" rules; which are all slightly different.

    """)

    input("Press 'enter' to continue\n")
    system('cls')

    print("""
                Where to go for more information

Interested?  Craps can be fun to play if you know the rules and are
courteous to the other players.

I based my information about the history of Craps on:
https://www.bestonlinecasinos.com/craps/history/

A fairly concise version of the rules for Craps can be found at:
https://www.bestonlinecasinos.com/craps/rules/

This site has a number of articles on things like "the best and worst bets"
(https://www.bestonlinecasinos.com/craps/bets/) along with other important
tips on things like Craps etiquette, etc.

If you decide to play real craps, spend some time and learn all you can
about the game before you begin.  Casinos will gladly offer you copies
of their craps rules and there are numerous on-line sites that describe
the best and worst ways to play craps too.

Enjoy!
    """)

    input("Press 'enter' to start the game\n")
    system('cls')

    return (0)
#
#  end of function
#

